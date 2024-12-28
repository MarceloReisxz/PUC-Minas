import tkinter as tk
from tkinter import filedialog, messagebox
from tkinter import Toplevel
import numpy as np
import matplotlib.pyplot as plt
import scipy.io
import cv2
from PIL import Image, ImageTk
from skimage.filters import sobel_h, sobel_v
from skimage.feature import graycomatrix, graycoprops
import os
import csv

""" Integrantes: Henrique de Almeida Diniz e Marcelo Reis Esteves 
NT = 3 """

class ImageApp:
    def __init__(self, root):

        self.csv_file = "roi_data.csv"

        # Define os cabeçalhos do CSV 
        self.csv_cabecalho = [
            "Filename", "Clase", "Figado ROI Top-Left", "Rim ROI Top-Left", "HI",
            "Coarseness", "Contrast", "Directionality", "Roughness", "Line-Likeness", "Regularity",
            "Homogeneity_d1", "Entropy_d1",
            "Homogeneity_d2", "Entropy_d2",
            "Homogeneity_d4", "Entropy_d4",
            "Homogeneity_d8", "Entropy_d8"
        ]

        # Verifica se o arquivo CSV existe; se não, cria com o cabeçalho completo
        if not os.path.exists(self.csv_file):
            with open(self.csv_file, mode='w', newline='') as file:
                writer = csv.writer(file)
                writer.writerow(self.csv_cabecalho)
        else:
            with open(self.csv_file, mode='r', newline='') as file:
                reader = csv.reader(file)
                existing_headers = next(reader, [])
            if not all(header in existing_headers for header in self.csv_cabecalho):
                with open(self.csv_file, mode='r', newline='') as file:
                    rows = list(csv.reader(file))
                with open(self.csv_file, mode='w', newline='') as file:
                    writer = csv.writer(file)
                    writer.writerow(self.csv_cabecalho)
                    writer.writerows(rows[1:])  

        self.root = root
        self.root.title("Visualizador de Imagens")

        self.roi_label = tk.Label(self.root, text="Menu Principal", bg='#5d46e2', font=('Arial', 14, 'bold'), fg='#FFFFFF')
        self.roi_label.pack(fill=tk.X)

        self.index_atual = None

        self.histogram_label = tk.Label(root)
        self.histogram_label.pack()

        self.image_frame = tk.Frame(root)
        self.image_frame.pack(pady=50)

        self.btn_anterior = tk.Button(
            self.image_frame, text="←", command=self.imagem_anterior, state=tk.DISABLED, width=5, height=2,
            bg='#5d46e2', fg='white', disabledforeground='#A9A9A9', font=('Arial', 18, 'bold')
        )

        self.btn_proximo = tk.Button(
            self.image_frame, text="→", command=self.proxima_imagem, state=tk.DISABLED, width=5, height=2,
            bg='#5d46e2', fg='white', disabledforeground='#A9A9A9', font=('Arial', 18, 'bold')
        )

        self.image_label = tk.Label(self.image_frame)

        self.btn_carregar = tk.Button(
            root, text="Carregar Imagem", command=self.carregar_imagem, width=30, height=1,
            bg='#5d46e2', fg='white', disabledforeground='#A9A9A9', font=('Arial', 12, 'bold')
        )
        self.btn_carregar.pack(pady=10, padx=20)

        self.btn_histograma = tk.Button(
            root, text="Mostrar Histograma", command=self.mostrar_histograma, state=tk.DISABLED, width=30, height=1,
            bg='#5d46e2', fg='white', disabledforeground='#A9A9A9', font=('Arial', 12, 'bold')
        )
        self.btn_histograma.pack(pady=10, padx=20)

        self.btn_recortar = tk.Button(
            root, text="Recortar ROI", command=self.recortar_rois, state=tk.DISABLED, width=30, height=1,
            bg='#5d46e2', fg='white', disabledforeground='#A9A9A9', font=('Arial', 12, 'bold')
        )
        self.btn_recortar.pack(pady=10, padx=20)

        self.btn_carregar_rois = tk.Button(
            root, text="Carregar ROIs", command=self.carregar_rois, width=30, height=1,
            bg='#5d46e2', fg='white', font=('Arial', 12, 'bold')
        )
        self.btn_carregar_rois.pack(pady=10, padx=20)

        self.btn_mostrar_roi = tk.Button(
            root, text="Visualizar ROIs", command=self.mostrar_roi, state=tk.NORMAL, width=30, height=1,
            bg='#5d46e2', fg='white', font=('Arial', 12, 'bold')
        )
        self.btn_mostrar_roi.pack(pady=10, padx=20)

        self.btn_ajuda = tk.Button(self.root, text="Ajuda", command=self.mostrar_menu_ajuda, width=30, height=1, 
                                bg='#5d46e2', fg='white', font=('Arial', 12, 'bold'))
        self.btn_ajuda.pack(pady=10, padx=20)

        self.image = None
        self.image_path = ""
        self.images = []
        self.index_atual = 0
        self.rois = []
        self.roi_index = 0
        self.current_roi_type = "normalizadas" 

        self.quantidade_zoom = 1.0
        self.base_image = None

        self.image_label.bind("<MouseWheel>", self.zoom)

    def carregar_imagem(self):
        file_path = filedialog.askopenfilename(filetypes=[("Arquivos de Imagem", "*.mat;*.jpg;*.png")])
        
        if file_path:
            self.image_path = file_path
            if file_path.lower().endswith('.mat'):
                self.images = self.ler_imagem(file_path)
            else:
                img = Image.open(file_path).convert('L')  
                self.images = [np.array(img)]
            
            if self.images:
                self.index_atual = 0
                self.base_image = self.images[self.index_atual]
                self.mostrar_imagem(self.base_image)
                numero_paciente = self.index_atual // 10
                print(f"Índice da imagem inicial: {self.index_atual}, Paciente: {numero_paciente}")
                self.roi_label.config(text=f" Menu Principal - Paciente: {numero_paciente}")
                self.btn_anterior.config(state=tk.NORMAL)
                self.btn_proximo.config(state=tk.NORMAL)
                self.btn_recortar.config(state=tk.NORMAL)
                self.btn_histograma.config(state=tk.NORMAL)
                self.btn_anterior.pack(padx=20, side=tk.LEFT)
                self.btn_proximo.pack(padx=20, side=tk.RIGHT)
                self.image_label.pack()

    def ler_imagem(self, path):
        data = scipy.io.loadmat(path)
        data_array = data['data']
        images = []
        for i in range(data_array.shape[1]):
            for j in range(10): 
                images.append(data_array[0, i][3][j])  
        return images

    def mostrar_imagem(self, img):
        img = Image.fromarray(img)
        img = img.resize((300, 300), Image.LANCZOS)  
        img_tk = ImageTk.PhotoImage(img)
        self.image_label.config(image=img_tk)
        self.image_label.image = img_tk

    def imagem_anterior(self):
        if self.images:
            self.index_atual = (self.index_atual - 1) % len(self.images)
            self.base_image = self.images[self.index_atual]
            self.quantidade_zoom = 1.0
            self.mostrar_imagem(self.base_image)
            numero_paciente = self.index_atual // 10 
            print(f"Imagem anterior, índice: {self.index_atual}, Paciente: {numero_paciente}")
            self.roi_label.config(text=f"Menu Principal - Paciente: {numero_paciente}")

    def proxima_imagem(self):
        if self.images:
            self.index_atual = (self.index_atual + 1) % len(self.images)
            self.base_image = self.images[self.index_atual]
            self.quantidade_zoom = 1.0
            self.mostrar_imagem(self.base_image)
            numero_paciente = self.index_atual // 10 
            print(f"Próxima imagem, índice: {self.index_atual}, Paciente: {numero_paciente}")
            self.roi_label.config(text=f"Menu Principal - Paciente: {numero_paciente}")

    def mostrar_histograma(self):
        if self.images:
            self.plotar_histograma(self.images[self.index_atual])

    def plotar_histograma(self, img):
        plt.figure()
        plt.hist(img.ravel(), bins=256, range=[0, 256], color='gray')
        plt.title('Histograma de Tons de Cinza')
        plt.xlabel('Intensidade de Pixel')
        plt.ylabel('Número de Pixels')
        plt.ylim([0, 3000])
        plt.show()

    def plotar_histograma_roi(self, img):
        plt.figure()
        plt.hist(img.ravel(), bins=256, range=[0, 256], color='gray')
        plt.title('Histograma de Tons de Cinza')
        plt.xlabel('Intensidade de Pixel')
        plt.ylabel('Número de Pixels')
        plt.ylim([0, 200])
        plt.show()    

    def recortar_rois(self):
        if self.images:

            def get_roi_tamanhoFixo(event, x, y, flags, param):
                if event == cv2.EVENT_LBUTTONDOWN:
                    param['roi_point'] = (x, y)
                    param['clicked'] = True 


            def selecionar_roi_tamanhoFixo(window_name):
                img = self.images[self.index_atual]
                param = {'clicked': False}
                cv2.namedWindow(window_name)
                cv2.setMouseCallback(window_name, get_roi_tamanhoFixo, param)
                cv2.imshow(window_name, img)

                while not param['clicked']:
                    cv2.waitKey(1)

                cv2.destroyWindow(window_name)

                x, y = param['roi_point']
                x1 = max(0, min(x - 14, img.shape[1] - 28))
                y1 = max(0, min(y - 14, img.shape[0] - 28))
                return x1, y1, 28, 28

            # Selecionar a primeira ROI (Fígado)
            roi_figado_coords = selecionar_roi_tamanhoFixo("Selecione a ROI do Fígado")
            if roi_figado_coords is None:
                messagebox.showerror("Erro", "Nenhum ponto selecionado para a ROI do Fígado.")
                return
            x1, y1, w1, h1 = roi_figado_coords

            # Selecionar a segunda ROI (Córtex Renal)
            roi_rim_coords = selecionar_roi_tamanhoFixo("Selecione a ROI do Córtex Renal")
            if roi_rim_coords is None:
                messagebox.showerror("Erro", "Nenhum ponto selecionado para a ROI do Córtex Renal.")
                return
            x2, y2, w2, h2 = roi_rim_coords

            img = self.images[self.index_atual]

            roi_figado = img[y1:y1+h1, x1:x1+w1]
            roi_rim = img[y2:y2+h2, x2:x2+w2]

            # Calcular a média dos tons de cinza das ROIs
            media_figado = np.mean(roi_figado)
            media_rim = np.mean(roi_rim)

            if media_rim == 0:
                messagebox.showerror("Erro", "A média dos tons de cinza da ROI do rim é zero. Não é possível calcular o HI.")
                return

            # Calcular o Índice Hepatorenal (HI)
            HI = media_figado / media_rim

            messagebox.showinfo("Índice Hepatorenal (HI)", f"O valor do HI é: {HI:.4f}")

            # Ajustar os tons de cinza da ROI do fígado
            figado_roi_ajustada = roi_figado * HI
            figado_roi_ajustada = np.round(figado_roi_ajustada)
            figado_roi_ajustada = np.clip(figado_roi_ajustada, 0, 255).astype(np.uint8)

            # Salvar a ROI do fígado ajustada em um diretório
            numero_paciente = self.index_atual // 10  
            image_numero = self.index_atual % 10     
            paciente_str = f"{numero_paciente:02d}"
            image_str = f"{image_numero}"

            filename = f"ROI_{paciente_str}_{image_str}.png"

            output_dir = "rois_figado"
            os.makedirs(output_dir, exist_ok=True) 
            filepath = os.path.join(output_dir, filename)
            cv2.imwrite(filepath, figado_roi_ajustada)

            if numero_paciente <= 16:
                paciente_class = "Saudavel"
            else:
                paciente_class = "Esteatose"

            # Adicionar dados ao arquivo CSV com campos de características vazios
            with open(self.csv_file, mode='a', newline='') as file:
                writer = csv.writer(file)
                writer.writerow([
                    filename,
                    paciente_class,
                    f"({x1}, {y1})",
                    f"({x2}, {y2})",
                    f"{HI:.4f}",
                    "",  # Coarseness
                    "",  # Contrast
                    "",  # Directionality
                    "",  # Roughness
                    "",  # Line-Likeness
                    "",  # Regularity
                    "",  # Homogeneity_d1
                    "",  # Entropy_d1
                    "",  # Homogeneity_d2
                    "",  # Entropy_d2
                    "",  # Homogeneity_d4
                    "",  # Entropy_d4
                    "",  # Homogeneity_d8
                    ""   # Entropy_d8
                ])

            # Desenhar retângulos na imagem original
            img_com_rois = cv2.cvtColor(img, cv2.COLOR_GRAY2BGR)
            cv2.rectangle(img_com_rois, (x1, y1), (x1+w1, y1+h1), (0, 255, 0), 2) 
            cv2.rectangle(img_com_rois, (x2, y2), (x2+w2, y2+h2), (0, 255, 0), 2) 

            cv2.imshow("Imagem com ROIs", img_com_rois)
            cv2.waitKey(0)
            cv2.destroyAllWindows()

            messagebox.showinfo("ROIs Recortadas", "As ROIs foram recortadas e o HI foi calculado com sucesso!")
            self.btn_mostrar_roi.config(state=tk.NORMAL)

    def carregar_rois(self):
        file_paths = filedialog.askopenfilenames(title="Selecione as ROIs", filetypes=[("Arquivos de Imagem", "*.png;*.jpg;*.jpeg;*.bmp")])
        if file_paths:
            output_dir = "ROIs_carregadas"
            os.makedirs(output_dir, exist_ok=True) 

            for file_path in file_paths:
                filename = os.path.basename(file_path)
                destination = os.path.join(output_dir, filename)
                cv2.imwrite(destination, cv2.imread(file_path))

            messagebox.showinfo("Sucesso", f"{len(file_paths)} ROIs foram carregadas com sucesso!")

    def zoom(self, event, roi=False):
        if event.delta > 0:
            self.quantidade_zoom *= 1.1
        else:
            self.quantidade_zoom /= 1.1

        self.quantidade_zoom = max(0.5, min(self.quantidade_zoom, 10.0))

        if roi:
            self.atualiza_zoom(self.rois[self.roi_index][0])
        else:
            self.atualiza_zoom(self.base_image)

    def atualiza_zoom(self, img_array):
        img = Image.fromarray(img_array)
        if img.width * self.quantidade_zoom > 300 and img.height * self.quantidade_zoom > 300:
            novo_tamanho = (int(img.width * self.quantidade_zoom), int(img.height * self.quantidade_zoom)) 
        else: 
            novo_tamanho = (300, 300)
        img = img.resize(novo_tamanho, Image.LANCZOS)
        img_tk = ImageTk.PhotoImage(img)
        self.image_label.config(image=img_tk)
        self.image_label.image = img_tk

    def mostrar_roi(self):
        def selecionar_tipo_roi():
            tipo_roi = tk.StringVar(value="normalizadas")

            janela_tipo = tk.Toplevel(self.root)
            janela_tipo.title("Selecionar Tipo de ROI")

            tk.Label(janela_tipo, text="Selecione o tipo de ROIs para visualizar:", font=('Arial', 12)).pack(pady=10)

            tk.Radiobutton(janela_tipo, text="ROIs do fígado normalizadas", variable=tipo_roi, value="normalizadas", font=('Arial', 12)).pack(anchor=tk.W)
            tk.Radiobutton(janela_tipo, text="ROIs carregadas", variable=tipo_roi, value="carregadas", font=('Arial', 12)).pack(anchor=tk.W)

            def confirmar_selecao():
                self.current_roi_type = tipo_roi.get()
                janela_tipo.destroy()
                self.carregar_rois_para_visualizar()

            tk.Button(janela_tipo, text="Confirmar", command=confirmar_selecao, bg='#5d46e2', fg='white', font=('Arial', 12)).pack(pady=10)

        selecionar_tipo_roi()

    def carregar_rois_para_visualizar(self):
        if self.current_roi_type == "normalizadas":
            roi_dir = "rois_figado"
        else:
            roi_dir = "ROIs_carregadas"

        if not os.path.exists(roi_dir):
            messagebox.showerror("Erro", f"Nenhuma ROI encontrada no diretório {roi_dir}.")
            return

        roi_files = [f for f in os.listdir(roi_dir) if f.endswith('.png')]
        if not roi_files:
            messagebox.showerror("Erro", f"Nenhuma ROI encontrada no diretório {roi_dir}.")
            return

        self.rois = []
        for filename in roi_files:
            filepath = os.path.join(roi_dir, filename)
            roi_image = cv2.imread(filepath, cv2.IMREAD_GRAYSCALE)
            if self.current_roi_type == "normalizadas":
                parts = filename.replace('ROI_', '').replace('.png', '').split('_')
                numero_paciente = int(parts[0])
                image_numero = int(parts[1])
                roi_info = f"Imagem {image_numero}"
            else:
                numero_paciente = "Carregada"
                roi_info = filename
            self.rois.append((roi_image, numero_paciente, roi_info))

        if self.rois:
            self.roi_index = 0
            self.create_roi_menu()

    def create_roi_menu(self):
        self.limpar_tela()

        self.roi_label = tk.Label(self.root, text="Visualizando ROIs", bg='#5d46e2', font=('Arial', 18, 'bold'), fg='#FFFFFF')
        self.roi_label.pack(fill=tk.X)

        self.image_frame = tk.Frame(self.root)
        self.image_frame.pack(pady=50)

        self.btn_anterior_roi = tk.Button(
            self.image_frame, text="←", command=self.roi_anterior, state=tk.NORMAL, width=5, height=2, 
            bg='#5d46e2', fg='white', disabledforeground='#A9A9A9', font=('Arial', 18, 'bold')
        )
        self.btn_anterior_roi.pack(padx=20, side=tk.LEFT)

        self.btn_proximo_roi = tk.Button(
            self.image_frame, text="→", command=self.proxima_roi, state=tk.NORMAL, width=5, height=2, 
            bg='#5d46e2', fg='white', disabledforeground='#A9A9A9', font=('Arial', 18, 'bold')
        )
        self.btn_proximo_roi.pack(padx=20, side=tk.RIGHT)

        self.image_label = tk.Label(self.image_frame)
        self.image_label.pack()

        self.btn_histograma_roi = tk.Button(
            self.root, text="Histograma da ROI", command=self.mostrar_histograma_roi, width=30, height=2, 
            bg='#5d46e2', fg='white', font=('Arial', 12, 'bold')
        )
        self.btn_histograma_roi.pack(pady=10, padx=20)

        self.histograma_matriz = tk.Button(
            self.root, text="Matrizes de Co-ocorrência da ROI", command=self.calcula_matrizCoOcorrencia, width=30, height=2, 
            bg='#5d46e2', fg='white', font=('Arial', 12, 'bold')
        )
        self.histograma_matriz.pack(pady=10, padx=20)

        self.btn_caracteriza = tk.Button(
            self.root, text="Caracterizar", command=self.caracteriza, width=30, height=2, 
            bg='#5d46e2', fg='white', font=('Arial', 12, 'bold')
        )
        self.btn_caracteriza.pack(pady=10, padx=20)

        self.btn_voltar_menu = tk.Button(
            self.root, text="Voltar às Imagens", command=self.voltar_menu, width=30, height=2, 
            bg='#5d46e2', fg='white', font=('Arial', 12, 'bold')
        )
        self.btn_voltar_menu.pack(pady=10, padx=20)

        self.btn_ajuda = tk.Button(self.root, text="Ajuda", command=self.mostrar_menu_ajuda_ROI, width=30, height=2, 
                                bg='#5d46e2', fg='white', font=('Arial', 12, 'bold'))
        self.btn_ajuda.pack(pady=10, padx=20)

        self.display_roi(self.rois[self.roi_index])

        self.quantidade_zoom = 1.0

        self.image_label.bind("<MouseWheel>", lambda event: self.zoom(event, True))

    def display_roi(self, roi_data):
        roi_image, numero_paciente, roi_info = roi_data
        self.roi_label.config(text=f"ROI do Paciente: {numero_paciente} - {roi_info}")
        roi_img = Image.fromarray(roi_image)
        roi_img = roi_img.resize((300, 300), Image.LANCZOS)
        roi_tk = ImageTk.PhotoImage(roi_img)
        self.image_label.config(image=roi_tk)
        self.image_label.image = roi_tk

    def roi_anterior(self):
        if self.rois:
            self.roi_index = (self.roi_index - 1) % len(self.rois)
            self.display_roi(self.rois[self.roi_index])

    def proxima_roi(self):
        if self.rois:
            self.roi_index = (self.roi_index + 1) % len(self.rois)
            self.display_roi(self.rois[self.roi_index])

    def mostrar_histograma_roi(self):
        if self.rois:
            roi_image = self.rois[self.roi_index][0]
            
            if len(roi_image.shape) == 3: 
                roi_gray = cv2.cvtColor(roi_image, cv2.COLOR_BGR2GRAY)
            else:
                roi_gray = roi_image
            
            self.plotar_histograma_roi(roi_gray)

    def voltar_menu(self):
        self.limpar_tela()
        self.create_menu()

    def create_menu(self):
        self.roi_label = tk.Label(self.root, text="Menu Principal", bg='#5d46e2', font=('Arial', 16, 'bold'), fg='#FFFFFF')
        self.roi_label.pack(fill=tk.X)

        numero_paciente = self.index_atual // 10 
        self.roi_label.config(text=f"Menu Principal - Paciente: {numero_paciente}")

        self.histogram_label = tk.Label(self.root)
        self.histogram_label.pack()

        self.image_frame = tk.Frame(self.root)
        self.image_frame.pack(pady=50)

        self.btn_anterior = tk.Button(
            self.image_frame, text="←", command=self.imagem_anterior, state=tk.NORMAL, width=5, height=2, 
            bg='#5d46e2', fg='white', disabledforeground='#A9A9A9', font=('Arial', 18, 'bold')
        )
        self.btn_anterior.pack(padx=20, side=tk.LEFT)

        self.btn_proximo = tk.Button(
            self.image_frame, text="→", command=self.proxima_imagem, state=tk.NORMAL, width=5, height=2, 
            bg='#5d46e2', fg='white', disabledforeground='#A9A9A9', font=('Arial', 18, 'bold')
        )
        self.btn_proximo.pack(padx=20, side=tk.RIGHT)

        self.image_label = tk.Label(self.image_frame)
        self.image_label.pack()
        self.image_frame.pack(pady=50)

        self.btn_carregar = tk.Button(
            self.root, text="Carregar Imagem", command=self.carregar_imagem, width=30, height=2, 
            bg='#5d46e2', fg='white', font=('Arial', 12, 'bold')
        )
        self.btn_carregar.pack(pady=10, padx=20)

        self.btn_histograma = tk.Button(
            self.root, text="Mostrar Histograma", command=self.mostrar_histograma, state=tk.NORMAL, width=30, height=2, 
            bg='#5d46e2', fg='white', font=('Arial', 12, 'bold')
        )
        self.btn_histograma.pack(pady=10, padx=20)

        self.btn_recortar = tk.Button(
            self.root, text="Recortar ROI", command=self.recortar_rois, state=tk.NORMAL, width=30, height=2, 
            bg='#5d46e2', fg='white', font=('Arial', 12, 'bold')
        )
        self.btn_recortar.pack(pady=10, padx=20)

        self.btn_carregar_rois = tk.Button(
            self.root, text="Carregar ROIs", command=self.carregar_rois, width=30, height=2,
            bg='#5d46e2', fg='white', font=('Arial', 12, 'bold')
        )
        self.btn_carregar_rois.pack(pady=10, padx=20)

        self.btn_mostrar_roi = tk.Button(
            self.root, text="Visualizar ROIs", command=self.mostrar_roi, state=tk.NORMAL, width=30, height=2, 
            bg='#5d46e2', fg='white', font=('Arial', 12, 'bold')
        )
        self.btn_mostrar_roi.pack(pady=10, padx=20)

        self.btn_ajuda = tk.Button(self.root, text="Ajuda", command=self.mostrar_menu_ajuda, width=30, height=2, 
                                bg='#5d46e2', fg='white', font=('Arial', 12, 'bold'))
        self.btn_ajuda.pack(pady=10, padx=20)
        
        self.mostrar_imagem(self.images[self.index_atual])
        self.quantidade_zoom = 1.0
        self.image_label.bind("<MouseWheel>", self.zoom)

    def mostrar_menu_ajuda(self):
        janela_ajuda = Toplevel(self.root)
        janela_ajuda.title("Ajuda")

        texto_ajuda = (
            "Botões do Menu Principal:\n\n"
            "1. Carregar Imagem: Carrega uma nova imagem ou conjunto de imagens.\n\n"
            "2. Mostrar Histograma: Exibe o histograma da imagem em exibição.\n\n"
            "3. Recortar ROI: Clique duas vezes na imagem para selecionar duas áreas de 28x28 pixels, com o clique como centro.\nA primeira seleção é para o fígado e a segunda é para o córtex renal.\n\n"
            "4. Carregar ROIs: Permite carregar ROIs externas para visualização.\n\n"
            "5. Visualizar ROIs: Exibe as Regiões de Interesse (ROIs) geradas ou carregadas.\n\n"
        )

        ajuda_label = tk.Label(janela_ajuda, text=texto_ajuda, padx=20, pady=20, font=('Arial', 12), justify=tk.LEFT)
        ajuda_label.pack(anchor=tk.W)

        btn_fechar = tk.Button(janela_ajuda, text="Fechar", command=janela_ajuda.destroy, bg='#5d46e2', fg='white', font=('Arial', 12))
        btn_fechar.pack(pady=10)

    def mostrar_menu_ajuda_ROI(self):
        janela_ajuda = Toplevel(self.root)
        janela_ajuda.title("Ajuda")

        texto_ajuda = (
            "Botões do Menu das ROIs:\n\n"
            "1. Histograma da ROI: Exibe o histograma da ROI em exibição.\n\n"
            "2. Matrizes de Co-ocorrência: Calcula e exibe 4 GLCM radiais Ci onde i=1,2,4,8 pixels, para a ROI em exibição.\n\n"
            "3. Caracterizar: Calcula e exibe os Descritores de Tamura para a ROI em exibição.\n\n"
            "4. Voltar às Imagens: Retorna para o menu principal.\n\n"
            "Nota: Se estiver visualizando ROIs carregadas, os resultados não serão armazenados no CSV.\n"
        )

        ajuda_label = tk.Label(janela_ajuda, text=texto_ajuda, padx=20, pady=20, font=('Arial', 12), justify=tk.LEFT)
        ajuda_label.pack(anchor=tk.W)

        btn_fechar = tk.Button(janela_ajuda, text="Fechar", command=janela_ajuda.destroy, bg='#5d46e2', fg='white', font=('Arial', 12))
        btn_fechar.pack(pady=10)

    def caracteriza(self):
        roi_image, numero_paciente, roi_info = self.rois[self.roi_index]

        if len(roi_image.shape) == 3:
            roi_gray = cv2.cvtColor(roi_image, cv2.COLOR_BGR2GRAY)
        else:
            roi_gray = roi_image

        # Calcular os Descritores de Tamura 
        coarseness = self.calcula_coarseness(roi_gray)
        contrast = self.calcula_contrast(roi_gray)
        directionality = self.calcula_directionality(roi_gray)
        roughness = self.calcula_roughness(coarseness, contrast)
        line_likeness = self.calcula_line_likeness(roi_gray)
        regularity = self.calcula_regularity(coarseness, contrast, directionality, line_likeness)

        message = (
            f"Descritores de Tamura para o paciente nº {numero_paciente} {roi_info}:\n"
            f"Coarseness: {coarseness:.4f}\n"
            f"Contrast: {contrast:.4f}\n"
            f"Directionality: {directionality:.4f}\n"
            f"Roughness: {roughness:.4f}\n"
            f"Line-Likeness: {line_likeness:.4f}\n"
            f"Regularity: {regularity:.4f}"
        )
        messagebox.showinfo("Tamura Descriptors", message)

        # Se estiver trabalhando com ROIs normalizadas, atualiza o CSV
        if self.current_roi_type == "normalizadas":
            filename = f"ROI_{numero_paciente:02d}_{self.rois[self.roi_index][2].split()[-1]}.png"
            features = {
                "Coarseness": f"{coarseness:.4f}",
                "Contrast": f"{contrast:.4f}",
                "Directionality": f"{directionality:.4f}",
                "Roughness": f"{roughness:.4f}",
                "Line-Likeness": f"{line_likeness:.4f}",
                "Regularity": f"{regularity:.4f}"
            }
            self.atualiza_linha_csv(filename, features)

    def calcula_coarseness(self, image):
        altura, largura = image.shape
        kmax = int(np.floor(np.log2(min(altura, largura))))
        kmax = min(kmax, 4) 
        A = []
        for k in range(kmax + 1):
            tamanho_janela = 2 ** k
            kernel = np.ones((tamanho_janela, tamanho_janela), dtype=np.float32) / (tamanho_janela ** 2)
            A_k = cv2.filter2D(image.astype('float32'), -1, kernel)
            A.append(A_k)
        E_h = []
        E_v = []
        for k in range(kmax):
            step = 2 ** k
            direita = A[k][:, step:]
            esquerda = A[k][:, :-step]
            E_h_k = np.pad(np.abs(direita - esquerda), ((0, 0), (step, 0)), 'constant')
            E_h.append(E_h_k)
            baixo = A[k][step:, :]
            cima = A[k][:-step, :]
            E_v_k = np.pad(np.abs(baixo - cima), ((step, 0), (0, 0)), 'constant')
            E_v.append(E_v_k)
        E = np.zeros((kmax, altura, largura))
        for k in range(kmax):
            E[k, :, :] = np.maximum(E_h[k], E_v[k])
        kbests = np.argmax(E, axis=0)
        Sbest = 2 ** kbests
        coarseness = np.mean(Sbest)
        return coarseness

    def calcula_contrast(self, imagem):
        imagem = imagem.astype('float32')
        media = np.mean(imagem)
        desvio_padrao = np.std(imagem)
        quarto_momento_central = np.mean((imagem - media) ** 4)
        if desvio_padrao ** 4 == 0:
            kurtose = 0
        else:
            kurtose = quarto_momento_central / (desvio_padrao ** 4)
        if kurtose == 0:
            contraste = 0
        else:
            contraste = desvio_padrao / (kurtose ** 0.25)
        return contraste


    def calcula_directionality(self, imagem, numero_bins=36):
        if len(imagem.shape) == 3:
            cinza = cv2.cvtColor(imagem, cv2.COLOR_BGR2GRAY)
        else:
            cinza = imagem.copy()
        
        grad_x = cv2.Sobel(cinza, cv2.CV_64F, 1, 0, ksize=3)
        grad_y = cv2.Sobel(cinza, cv2.CV_64F, 0, 1, ksize=3)
        
        magnitude = np.sqrt(grad_x**2 + grad_y**2)
        orientacao = np.arctan2(grad_y, grad_x) 
        
        orientacao_graus = (np.degrees(orientacao) + 180) % 180
        
        hist, bordas = np.histogram(orientacao_graus, bins=numero_bins, range=(0, 180), weights=magnitude)
        
        hist_normalizado = hist / np.sum(hist) if np.sum(hist) != 0 else hist
        
        centros_bins = (bordas[:-1] + bordas[1:]) / 2
        
        orientacao_media = np.sum(centros_bins * hist_normalizado)
        
        variancia = np.sum(((centros_bins - orientacao_media) ** 2) * hist_normalizado)
        
        direcionalidade = 1 - (variancia / (90**2))
        
        direcionalidade = np.clip(direcionalidade, 0, 1)
        
        return direcionalidade

    def calcula_roughness(self, coarseness, contrast):
        roughness = coarseness + contrast
        return roughness

    def calcula_line_likeness(self, gray_img):
        Gx = sobel_h(gray_img)  
        Gy = sobel_v(gray_img)  
        orientacao = np.arctan2(Gy, Gx)
        orientacao_graus = np.degrees(orientacao) % 180 

        N = 16  
        limites_bins = np.linspace(0, 180, N + 1)
        orientacoes_quantizadas = np.digitize(orientacao_graus, limites_bins) - 1  

        orientacoes_quantizadas = orientacoes_quantizadas.astype(np.uint8)

        distances = [1]  
        angles = [0, np.pi/4, np.pi/2, 3*np.pi/4]  

        glcm = graycomatrix(
            orientacoes_quantizadas,
            distances=distances,
            angles=angles,
            levels=N,
            symmetric=True,
            normed=True
        )

        P = np.mean(glcm, axis=(2, 3))  

        theta = (limites_bins[:-1] + limites_bins[1:]) / 2 
        theta_rad = np.radians(theta)

        theta_i, theta_j = np.meshgrid(theta_rad, theta_rad)

        termo_cos = np.cos(2 * (theta_i - theta_j)) ** 2

        line_likeness_value = np.sum(P * termo_cos)

        return line_likeness_value

    
    def calcula_regularity(self, coarseness, contrast, directionality, line_likeness):
        total = coarseness + contrast + directionality + line_likeness
        if total == 0:
            return 0
        normalized_coarseness = coarseness / total
        normalized_contrast = contrast / total
        normalized_directionality = directionality / total
        normalized_line_likeness = line_likeness / total
        
        regularity_value = 1 - np.std([normalized_coarseness, normalized_contrast, normalized_directionality, normalized_line_likeness])
        return regularity_value

    def calcula_matrizCoOcorrencia(self):
        roi_image, numero_paciente, roi_info = self.rois[self.roi_index]

        if len(roi_image.shape) == 3:  
            roi_gray = cv2.cvtColor(roi_image, cv2.COLOR_BGR2GRAY)
        else:
            roi_gray = roi_image

        distancias = [1, 2, 4, 8]
        angulos = np.deg2rad(np.arange(0, 360, 1))  

        features = {}
        for d in distancias:
            glcm = graycomatrix(roi_gray, distances=[d], angles=angulos, levels=256, symmetric=True, normed=True)

            glcm_acumulada = np.sum(glcm, axis=3) 

            glcm_acumulada_normalizada = glcm_acumulada / np.sum(glcm_acumulada)

            glcm_acumulada_normalizada = glcm_acumulada_normalizada[:, :, :, np.newaxis]  

            homogeneity = graycoprops(glcm_acumulada_normalizada, 'homogeneity')[0, 0]

            glcm_nonzero = glcm_acumulada_normalizada[glcm_acumulada_normalizada > 0]
            entropy = -np.sum(glcm_nonzero * np.log2(glcm_nonzero))

            homogeneity_rounded = round(homogeneity, 4)
            entropy_rounded = round(entropy, 4)

            features[f"Homogeneity_d{d}"] = f"{homogeneity_rounded}"
            features[f"Entropy_d{d}"] = f"{entropy_rounded}"

            plt.figure(figsize=(5, 5))
            plt.imshow(glcm_acumulada_normalizada[:, :, 0, 0], cmap='gray')  
            plt.title(f"GLCM Acumulada - Distância {d}")
            plt.colorbar()
            plt.show()

         
            messagebox.showinfo("Propriedades", f"Distância: {d}\nHomogeneidade: {homogeneity_rounded}\nEntropia: {entropy_rounded}")

        # Se estiver trabalhando com ROIs normalizadas, atualiza o CSV
        if self.current_roi_type == "normalizadas":
            filename = f"ROI_{numero_paciente:02d}_{self.rois[self.roi_index][2].split()[-1]}.png"
            self.atualiza_linha_csv(filename, features)

    def limpar_tela(self):
        for widget in self.root.winfo_children():
            widget.destroy()

    def atualiza_linha_csv(self, filename, features):
        with open(self.csv_file, mode='r', newline='') as file:
            reader = csv.DictReader(file)
            rows = list(reader)
            fieldnames = reader.fieldnames

        row_found = False
        for row in rows:
            if row['Filename'] == filename:
                for key, value in features.items():
                    if key in fieldnames:
                        row[key] = value
                row_found = True
                break

        if not row_found:
            messagebox.showerror("Erro", f"Arquivo {filename} não encontrado no CSV.")
            return
        
        with open(self.csv_file, mode='w', newline='') as file:
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(rows)

if __name__ == "__main__":
    root = tk.Tk()
    app = ImageApp(root)
    root.mainloop()
