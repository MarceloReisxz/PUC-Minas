import tkinter as tk
from tkinter import filedialog, messagebox
from tkinter import Toplevel
from tkinter import simpledialog
import numpy as np
import matplotlib.pyplot as plt
import scipy.io
import cv2
from PIL import Image, ImageTk
from skimage.filters import sobel_h, sobel_v
from skimage.feature import graycomatrix, graycoprops
import os
import csv
import pandas as pd
import numpy as np
import seaborn as sns
from xgboost import XGBClassifier
from sklearn.metrics import accuracy_score, confusion_matrix, recall_score, precision_score
import random
import joblib
import tensorflow as tf
from tensorflow.keras.applications import VGG16
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Flatten, Dropout
from tensorflow.keras.preprocessing.image import load_img, img_to_array
from sklearn.metrics import confusion_matrix, accuracy_score
from tensorflow.keras.optimizers import Adam
import time


class ImageApp:
    def __init__(self, root):

        self.csv_file = "roi_data.csv"

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
            self.image_frame, text="←", command=self.imagem_anterior, state=tk.DISABLED, width=5, height=1,
            bg='#5d46e2', fg='white', disabledforeground='#A9A9A9', font=('Arial', 18, 'bold')
        )

        self.btn_proximo = tk.Button(
            self.image_frame, text="→", command=self.proxima_imagem, state=tk.DISABLED, width=5, height=1,
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
        
        self.btn_classificadores = tk.Button(
            self.root, text="Classificadores", command=self.tela_classificadores, width=30, height=1,
            bg='#5d46e2', fg='white', font=('Arial', 12, 'bold')
        )
        self.btn_classificadores.pack(pady=10)

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
        
        self.model_file = 'vgg16_model.h5'
        self.epochs = 4
        self.batch_size = 16  


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

            # Seleciona a primeira ROI (Fígado)
            roi_figado_coords = selecionar_roi_tamanhoFixo("Selecione a ROI do Fígado")
            if roi_figado_coords is None:
                messagebox.showerror("Erro", "Nenhum ponto selecionado para a ROI do Fígado.")
                return
            x1, y1, w1, h1 = roi_figado_coords

            # Seleciona a segunda ROI (Córtex Renal)
            roi_rim_coords = selecionar_roi_tamanhoFixo("Selecione a ROI do Córtex Renal")
            if roi_rim_coords is None:
                messagebox.showerror("Erro", "Nenhum ponto selecionado para a ROI do Córtex Renal.")
                return
            x2, y2, w2, h2 = roi_rim_coords

            img = self.images[self.index_atual]

            roi_figado = img[y1:y1+h1, x1:x1+w1]
            roi_rim = img[y2:y2+h2, x2:x2+w2]

            # Calcula a média dos tons de cinza das ROIs
            media_figado = np.mean(roi_figado)
            media_rim = np.mean(roi_rim)

            if media_rim == 0:
                messagebox.showerror("Erro", "A média dos tons de cinza da ROI do rim é zero. Não é possível calcular o HI.")
                return

            # Calcula o Índice Hepatorenal (HI)
            HI = media_figado / media_rim

            messagebox.showinfo("Índice Hepatorenal (HI)", f"O valor do HI é: {HI:.4f}")

            # Ajusta os tons de cinza da ROI do fígado
            figado_roi_ajustada = roi_figado * HI
            figado_roi_ajustada = np.round(figado_roi_ajustada)
            figado_roi_ajustada = np.clip(figado_roi_ajustada, 0, 255).astype(np.uint8)

            # Salva a ROI do fígado ajustada em um diretório
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

            # Adiciona dados ao arquivo CSV com campos de características vazios
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
            self.image_frame, text="←", command=self.roi_anterior, state=tk.NORMAL, width=5, height=1, 
            bg='#5d46e2', fg='white', disabledforeground='#A9A9A9', font=('Arial', 18, 'bold')
        )
        self.btn_anterior_roi.pack(padx=20, side=tk.LEFT)

        self.btn_proximo_roi = tk.Button(
            self.image_frame, text="→", command=self.proxima_roi, state=tk.NORMAL, width=5, height=1, 
            bg='#5d46e2', fg='white', disabledforeground='#A9A9A9', font=('Arial', 18, 'bold')
        )
        self.btn_proximo_roi.pack(padx=20, side=tk.RIGHT)

        self.image_label = tk.Label(self.image_frame)
        self.image_label.pack()

        self.btn_histograma_roi = tk.Button(
            self.root, text="Histograma da ROI", command=self.mostrar_histograma_roi, width=30, height=1, 
            bg='#5d46e2', fg='white', font=('Arial', 12, 'bold')
        )
        self.btn_histograma_roi.pack(pady=10, padx=20)

        self.histograma_matriz = tk.Button(
            self.root, text="Matrizes de Co-ocorrência da ROI", command=self.calcula_matrizCoOcorrencia, width=30, height=1, 
            bg='#5d46e2', fg='white', font=('Arial', 12, 'bold')
        )
        self.histograma_matriz.pack(pady=10, padx=20)

        self.btn_caracteriza = tk.Button(
            self.root, text="Caracterizar", command=self.caracteriza, width=30, height=1, 
            bg='#5d46e2', fg='white', font=('Arial', 12, 'bold')
        )
        self.btn_caracteriza.pack(pady=10, padx=20)

        self.btn_voltar_menu = tk.Button(
            self.root, text="Voltar às Imagens", command=self.voltar_menu, width=30, height=1, 
            bg='#5d46e2', fg='white', font=('Arial', 12, 'bold')
        )
        self.btn_voltar_menu.pack(pady=10, padx=20)

        self.btn_ajuda = tk.Button(self.root, text="Ajuda", command=self.mostrar_menu_ajuda_ROI, width=30, height=1, 
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
            self.image_frame, text="←", command=self.imagem_anterior, state=tk.NORMAL, width=5, height=1, 
            bg='#5d46e2', fg='white', disabledforeground='#A9A9A9', font=('Arial', 18, 'bold')
        )
        self.btn_anterior.pack(padx=20, side=tk.LEFT)

        self.btn_proximo = tk.Button(
            self.image_frame, text="→", command=self.proxima_imagem, state=tk.NORMAL, width=5, height=1, 
            bg='#5d46e2', fg='white', disabledforeground='#A9A9A9', font=('Arial', 18, 'bold')
        )
        self.btn_proximo.pack(padx=20, side=tk.RIGHT)

        self.image_label = tk.Label(self.image_frame)
        self.image_label.pack()
        self.image_frame.pack(pady=50)

        self.btn_carregar = tk.Button(
            self.root, text="Carregar Imagem", command=self.carregar_imagem, width=30, height=1, 
            bg='#5d46e2', fg='white', font=('Arial', 12, 'bold')
        )
        self.btn_carregar.pack(pady=10, padx=20)

        self.btn_histograma = tk.Button(
            self.root, text="Mostrar Histograma", command=self.mostrar_histograma, state=tk.NORMAL, width=30, height=1, 
            bg='#5d46e2', fg='white', font=('Arial', 12, 'bold')
        )
        self.btn_histograma.pack(pady=10, padx=20)

        self.btn_recortar = tk.Button(
            self.root, text="Recortar ROI", command=self.recortar_rois, state=tk.NORMAL, width=30, height=1, 
            bg='#5d46e2', fg='white', font=('Arial', 12, 'bold')
        )
        self.btn_recortar.pack(pady=10, padx=20)

        self.btn_carregar_rois = tk.Button(
            self.root, text="Carregar ROIs", command=self.carregar_rois, width=30, height=1,
            bg='#5d46e2', fg='white', font=('Arial', 12, 'bold')
        )
        self.btn_carregar_rois.pack(pady=10, padx=20)

        self.btn_mostrar_roi = tk.Button(
            self.root, text="Visualizar ROIs", command=self.mostrar_roi, state=tk.NORMAL, width=30, height=1, 
            bg='#5d46e2', fg='white', font=('Arial', 12, 'bold')
        )
        self.btn_mostrar_roi.pack(pady=10, padx=20)
        
        self.btn_classificadores = tk.Button(
            self.root, text="Classificadores", command=self.tela_classificadores, width=30, height=1,
            bg='#5d46e2', fg='white', font=('Arial', 12, 'bold')
        )
        self.btn_classificadores.pack(pady=10)

        self.btn_ajuda = tk.Button(self.root, text="Ajuda", command=self.mostrar_menu_ajuda, width=30, height=1, 
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
            "6. Classificadores: Implemente classificadores para testar, treinar e avaliar as ROIs.\n\n"
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
    
    def calcula_glcm_properties(self, gray_img, distance):
            numero_bins = 16

            grad_x = cv2.Sobel(gray_img, cv2.CV_64F, 1, 0, ksize=3)
            grad_y = cv2.Sobel(gray_img, cv2.CV_64F, 0, 1, ksize=3)
            magnitude = np.sqrt(grad_x**2 + grad_y**2)
            orientacao = np.arctan2(grad_y, grad_x)
            orientacao_graus = (np.degrees(orientacao) + 180) % 180  # Normaliza para [0, 180)

            limites_bins = np.linspace(0, 180, numero_bins + 1)
            orientacoes_quantizadas = np.digitize(orientacao_graus, limites_bins) - 1
            orientacoes_quantizadas = np.clip(orientacoes_quantizadas, 0, numero_bins - 1).astype(np.uint8)

            angles = [0]

            glcm = graycomatrix(
                orientacoes_quantizadas,
                distances=[distance],
                angles=angles,
                levels=numero_bins,
                symmetric=True,
                normed=True
            )

            homogeneity = graycoprops(glcm, 'homogeneity')[0, 0]

            glcm_nonzero = glcm[glcm > 0]
            entropy = -np.sum(glcm_nonzero * np.log2(glcm_nonzero))

            return homogeneity, entropy
    
    def calcula_line_likeness(self, gray_img):
        Gx = sobel_h(gray_img)  
        Gy = sobel_v(gray_img)  
        orientacao = np.arctan2(Gy, Gx)
        orientacao_graus = np.degrees(orientacao) % 180
        
        N = 4
        limites_bins = np.linspace(0, 180, N + 1)
        orientacoes_quantizadas = np.digitize(orientacao_graus, limites_bins) - 1

        orientacoes_quantizadas = np.clip(orientacoes_quantizadas, 0, N - 1).astype(np.uint8)

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

        # Correção aqui: remover o quadrado
        termo_cos = np.cos(2 * (theta_i - theta_j))

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
    
    def tela_classificadores(self):
        self.limpar_tela()

        tk.Label(self.root, text="Classificadores", bg='#5d46e2', font=('Arial', 16, 'bold'), fg='#FFFFFF').pack(fill=tk.X)
        tk.Frame(root).pack(pady=50)

        btn_xgboost = tk.Button(
            self.root, text="XGBoost", command=self.executar_xgboost, width=30, height=1,
            bg='#5d46e2', fg='white', font=('Arial', 12, 'bold')
        )
        btn_xgboost.pack(pady=10)

        btn_profundo = tk.Button(
            self.root, text="Profundo", command=self.executar_vgg16, width=30, height=1,
            bg='#5d46e2', fg='white', font=('Arial', 12, 'bold')
        )
        btn_profundo.pack(pady=10)

        btn_comparar = tk.Button(
            self.root, text="Comparar", command=self.comparar_matrizes, width=30, height=1,
            bg='#5d46e2', fg='white', font=('Arial', 12, 'bold')
        )
        btn_comparar.pack(pady=10)

        btn_classificar_imagem_xgboost = tk.Button(
            self.root, text="Classificar Imagem com XGBoost", command=self.classificar_imagem_xgboost, width=30, height=1,
            bg='#5d46e2', fg='white', font=('Arial', 12, 'bold')
        )
        btn_classificar_imagem_xgboost.pack(pady=10)
        
        btn_classificar_imagem_vgg = tk.Button(
            self.root, text="Classificar Imagem com VGG16", command=self.classificar_imagem_vgg16, width=30, height=1,
            bg='#5d46e2', fg='white', font=('Arial', 12, 'bold')
        )
        btn_classificar_imagem_vgg.pack(pady=10)

        btn_voltar = tk.Button(
            self.root, text="Voltar", command=self.voltar_menu, width=30, height=1,
            bg='#5d46e2', fg='white', font=('Arial', 12, 'bold')
        )
        btn_voltar.pack(pady=10)

    def parametros(self):
        root = tk.Tk()
        root.withdraw()

        semente = simpledialog.askinteger("Semente Aleatória", "Digite a semente aleatória:", minvalue=0)
        
        if semente is None:
            semente = 42

        return semente

    def executar_vgg16(self):
        roi_directory = 'rois_figado'

        # Carrega as imagens e organiza por pacientes
        def load_images(roi_directory):
            data = []
            labels = []
            groups = []

            for file in sorted(os.listdir(roi_directory)):
                if file.endswith(".png"):
                    path = os.path.join(roi_directory, file)
                    patient_num, roi_num = map(int, file.replace("ROI_", "").replace(".png", "").split("_"))
                    label = 0 if patient_num <= 16 else 1  # 0 = Saudável, 1 = Esteatose

                    img = load_img(path, target_size=(224, 224))
                    img_array = img_to_array(img)

                    data.append(img_array)
                    labels.append(label)
                    groups.append(patient_num)
            return np.array(data), np.array(labels), np.array(groups)


        def create_model():
            base_model = VGG16(weights="imagenet", include_top=False, input_shape=(224, 224, 3))
            # Congela todas as camadas inicialmente
            base_model.trainable = False
            
            # Descongela as últimas 4 camadas para fine-tuning
            for layer in base_model.layers[-4:]:
                layer.trainable = True

            model = Sequential([
                base_model,
                Flatten(),
                Dense(256, activation='relu'),
                Dropout(0.5),
                Dense(1, activation='sigmoid')
            ])

            model.compile(optimizer=Adam(learning_rate=0.0001), loss='binary_crossentropy', metrics=['accuracy'])
            return model

        model_file = 'vgg16_model.h5'

        data, labels, groups = load_images(roi_directory)

        # Normalização dos dados
        data = data / 255.0

        inicio_tempo = time.time()

        # Verifica se o modelo já existe
        if os.path.exists(model_file):
            print("Modelo existente encontrado. Carregando o modelo...")
            model = tf.keras.models.load_model(model_file)

            y_pred = (model.predict(data) > 0.5).astype("int32")
            accuracy = accuracy_score(labels, y_pred)
            print(f"Acurácia do modelo carregado: {accuracy:.4f}")


            cm = confusion_matrix(labels, y_pred)
            self.plotar_matriz_confusao(cm, title="Matriz de Confusão do Modelo Carregado")


            TP = cm[0, 0]
            FP = cm[0, 1]
            FN = cm[1, 0]
            TN = cm[1, 1]
            sensitivity = TP / (TP + FN) if (TP + FN) > 0 else 0
            specificity = TN / (TN + FP) if (TN + FP) > 0 else 0
            self.exibir_resultados(accuracy * 100, sensitivity * 100, specificity * 100)
            fim_tempo = time.time()
            tempo_total = fim_tempo - inicio_tempo
            print(f"Tempo total de execução: {tempo_total:.2f} segundos")

        else:
            print("Modelo não encontrado. Iniciando treinamento...")
            from sklearn.model_selection import LeaveOneGroupOut
            logo = LeaveOneGroupOut()
            accuracy_list = []
            confusion_matrices = []
            histories = []

            os.makedirs('confusions_VGG16', exist_ok=True)

            for fold, (train_index, test_index) in enumerate(logo.split(data, labels, groups=groups)):
                print(f"\nFold {fold + 1}/{len(np.unique(groups))}")
                X_train, X_test = data[train_index], data[test_index]
                y_train, y_test = labels[train_index], labels[test_index]
                test_patient = groups[test_index[0]]


                print(f"Fold {fold + 1}")
                print(f"Paciente de teste: {test_patient}")
                print(f"Número de amostras de treinamento: {X_train.shape[0]}")
                print(f"Número de amostras de teste: {X_test.shape[0]}")
                print(f"Distribuição de classes no treinamento: {np.bincount(y_train)}")
                print(f"Distribuição de classes no teste: {np.bincount(y_test)}")

                print(f"Indices de treinamento (exemplo): {train_index[:5]} ... {train_index[-5:]}")
                print(f"Indices de teste (exemplo): {test_index[:5]} ... {test_index[-5:]}")
                print("-" * 50)

                # Cria um novo modelo para este fold
                model = create_model()

                # Treinamento
                history = model.fit(X_train, y_train, epochs=self.epochs, batch_size=self.batch_size,
                                    validation_data=(X_test, y_test), verbose=1)
                histories.append(history)

                # Avaliação
                y_pred = (model.predict(X_test) > 0.5).astype("int32")
                accuracy = accuracy_score(y_test, y_pred)
                cm = confusion_matrix(y_test, y_pred, labels=[0, 1])

                accuracy_list.append(accuracy)
                confusion_matrices.append(cm)

                print(f"Teste para paciente {test_patient} - Acurácia: {accuracy:.4f}")

                save_path = os.path.join('confusions_VGG16', f'confusion_matrix_fold_{fold + 1}.png')
                self.plotar_matriz_confusao(cm, title=f"Matriz de Confusão - Fold {fold + 1}", save_path=save_path)


            # Média das matrizes de confusão
            media_conf_matrix = np.sum(confusion_matrices, axis=0)

            TP = media_conf_matrix[0, 0]
            FP = media_conf_matrix[0, 1]
            FN = media_conf_matrix[1, 0]
            TN = media_conf_matrix[1, 1]

            sensitivity = TP / (TP + FN) if (TP + FN) > 0 else 0
            specificity = TN / (TN + FP) if (TN + FP) > 0 else 0
            avg_accuracy = np.mean(accuracy_list)

            self.plotar_matriz_confusao(media_conf_matrix, title="Matriz de Confusão Média")

            matriz_final_filename = f"MatrizFinal_{self.epochs}_epochs_{self.batch_size}_batchSize.png"
            matriz_final_path = os.path.join('confusions_VGG16', matriz_final_filename)
            self.plotar_matriz_confusao(media_conf_matrix, title="Matriz de Confusão Média", save_path=matriz_final_path)
            print(f"Matriz de Confusão Média salva como {matriz_final_path}")


            matriz_final_filename_csv = f"MatrizFinal_{self.epochs}_epochs_{self.batch_size}_batchSize.csv"
            matriz_final_path_csv = os.path.join('confusions_VGG16', matriz_final_filename_csv)

            np.savetxt(matriz_final_path_csv, media_conf_matrix, delimiter=',', fmt='%d', header='TN,FP,FN,TP', comments='')

            print(f"Matriz de Confusão Média salva como {matriz_final_path_csv} (CSV)")

            self.exibir_resultados(avg_accuracy * 100, sensitivity * 100, specificity * 100)

            # Plotar as curvas de aprendizado médias
            # Coletar as acurácias por época
            all_acc = []
            all_val_acc = []
            for history in histories:
                acc = history.history['accuracy']
                val_acc = history.history['val_accuracy']
                all_acc.append(acc)
                all_val_acc.append(val_acc)

            # Encontrar o número máximo de épocas entre todos os folds
            max_epochs = max([len(acc) for acc in all_acc])

            # Preencher sequências
            for i in range(len(all_acc)):
                acc = all_acc[i]
                val_acc = all_val_acc[i]
                if len(acc) < max_epochs:
                    pad_length = max_epochs - len(acc)
                    acc += [acc[-1]] * pad_length
                    val_acc += [val_acc[-1]] * pad_length
                    all_acc[i] = acc
                    all_val_acc[i] = val_acc

            # Calcular as médias das acurácias por época
            mean_acc = np.mean(all_acc, axis=0)
            mean_val_acc = np.mean(all_val_acc, axis=0)

            plt.figure()
            plt.plot(range(1, max_epochs+1), mean_acc, label='Acurácia de Treino')
            plt.plot(range(1, max_epochs+1), mean_val_acc, label='Acurácia de Validação')
            plt.title('Curvas de Aprendizado Médias')
            plt.xlabel('Épocas')
            plt.ylabel('Acurácia')
            plt.legend()
            plt.show()

            fim_tempo = time.time()
            tempo_total = fim_tempo - inicio_tempo
            print(f"Tempo total de execução: {tempo_total:.2f} segundos")

            print("Treinando o modelo no conjunto de dados completo...")
            model = create_model()
            history = model.fit(data, labels, epochs=self.epochs, batch_size=self.batch_size, verbose=1)
            # Salvar o modelo
            print("Treinamento concluído. Salvando o modelo...")
            model.save(model_file)
            print("Modelo salvo com sucesso.")


            messagebox.showinfo("Treinamento Concluído", "O treinamento do modelo profundo foi concluído com sucesso!")



    def executar_xgboost(self):
        #Define semente
        semente_aleatoria = self.parametros()

        csv_path = "./roi_data.csv"
        df = pd.read_csv(csv_path)

        #Coleta colunas e divide os pacientes
        haralick_columns = ["Homogeneity_d1", "Entropy_d1", "Homogeneity_d2", "Entropy_d2",
                            "Homogeneity_d4", "Entropy_d4", "Homogeneity_d8", "Entropy_d8"]
        nt_columns = ["Contrast", "Coarseness", "Directionality", "Roughness", "Line-Likeness" , "Regularity"]
        X = df[haralick_columns + nt_columns]
        y = df['Clase'].map({'Saudavel': 0, 'Esteatose': 1})
        df['Paciente'] = df['Filename'].str.extract(r'ROI_(\d+)_')[0].astype(int)

        random.seed(semente_aleatoria)
        pacientes = random.sample(list(df['Paciente'].unique()), len(df['Paciente'].unique()))
        accuracies = []
        conf_matrices = []

        for paciente in pacientes:
            
            test_mask = df['Paciente'] == paciente
            X_train = X[~test_mask]
            y_train = y[~test_mask]
            X_test = X[test_mask]
            y_test = y[test_mask]

            model = XGBClassifier(eval_metric='logloss', random_state=semente_aleatoria)
            model.fit(X_train, y_train)
            joblib.dump(model, "xgboost_model.pkl")
            y_pred = model.predict(X_test)

            acc = accuracy_score(y_test, y_pred)
            conf_matrix = confusion_matrix(y_test, y_pred, labels=[0, 1])

            accuracies.append(acc)
            conf_matrices.append(conf_matrix)

            print(f"Paciente: {paciente}")

        #Calcula matriz e caracteristicas
        media_conf_matrix = sum(conf_matrices)
        TP = media_conf_matrix[0, 0]
        FP = media_conf_matrix[0, 1]
        FN = media_conf_matrix[1, 0]
        TN = media_conf_matrix[1, 1]

        sensitivity = TP / (TP + FN) if (TP + FN) > 0 else 0
        specificity = TN / (TN + FP) if (TN + FP) > 0 else 0

        self.plotar_matriz_confusao(media_conf_matrix)

        self.exibir_resultados(np.mean(accuracies) * 100, 
                            sensitivity * 100,
                            specificity * 100)

    def exibir_resultados(self, acuracia, sensibilidade, especificidade):
        resultados_window = tk.Toplevel(self.root)
        resultados_window.title("Resultados do Modelo")

        label_acuracia = tk.Label(resultados_window, text=f"Acurácia Média: {acuracia:.4f}",
                                font=('Arial', 12), anchor="w")
        label_acuracia.pack(pady=5)

        label_sensibilidade = tk.Label(resultados_window,
                                                text=f"Sensibilidade Média: {sensibilidade:.4f}",
                                                font=('Arial', 12), anchor="w")
        label_sensibilidade.pack(pady=5)

        label_especificidade = tk.Label(resultados_window,
                                        text=f"Especificidade Média: {especificidade:.4f}",
                                        font=('Arial', 12), anchor="w")
        label_especificidade.pack(pady=5)

        btn_fechar = tk.Button(resultados_window, text="Fechar", command=resultados_window.destroy,
                            width=20, height=1, bg='#5d46e2', fg='white', font=('Arial', 12, 'bold'))
        btn_fechar.pack(pady=20)

    def plotar_matriz_confusao(self, conf_matrix, title="Matriz de Confusão", save_path=None):
        plt.figure(figsize=(6, 4))
        sns.heatmap(conf_matrix, annot=True, fmt='d', cmap="Blues",
                    xticklabels=['Saudável', 'Esteatose'], yticklabels=['Saudável', 'Esteatose'])
        plt.title(title)
        plt.ylabel("Real")
        plt.xlabel("Previsto")
        if save_path:
            plt.savefig(save_path)
            plt.close()
        else:
            plt.show()
    
    def classificar_imagem_xgboost(self):
        file_path = filedialog.askopenfilename(filetypes=[("Imagens", "*.png;*.jpg;*.jpeg")])
        if not file_path:
            return 

        filename = os.path.basename(file_path)
        
        csv_path = "./roi_data.csv"
        df = pd.read_csv(csv_path)
        
        row = df[df['Filename'] == filename]
        if row.empty:
            messagebox.showerror("Erro", f"O arquivo '{filename}' não foi encontrado na planilha.")
            return

        haralick_columns = ["Homogeneity_d1", "Entropy_d1", "Homogeneity_d2", "Entropy_d2",
                            "Homogeneity_d4", "Entropy_d4", "Homogeneity_d8", "Entropy_d8"]
        nt_columns = ["Contrast", "Coarseness", "Directionality", "Roughness", "Line-Likeness" , "Regularity"]
        extracted_features = row[haralick_columns + nt_columns].iloc[0].values

        X_input = pd.DataFrame([extracted_features], columns=haralick_columns + nt_columns)
        
        model = joblib.load("xgboost_model.pkl")
        
        pred = model.predict(X_input)
        classe = "Saudável" if pred[0] == 0 else "Esteatose"
        
        tk.messagebox.showinfo("Resultado", f"A classe prevista para a imagem é: {classe}")


    def comparar_matrizes(self):
        imagem_xgboost = Image.open("./Matriz_final_xgboost.png")
        """ imagem_vgg = Image.open("imagem_vgg.png") """

        janela_xgboost = Toplevel(self.root)
        janela_xgboost.title("Matriz Final XGBoost")

        """ janela_vgg = Toplevel(self.root)
        janela_vgg.title("Outra Imagem") """

        largura, altura = 500, 400
        imagem_xgboost = imagem_xgboost.resize((largura, altura))
        """ imagem_vgg = imagem_vgg.resize((largura, altura)) """

        img_xgboost = ImageTk.PhotoImage(imagem_xgboost)
        """ img_outra = ImageTk.PhotoImage(imagem_vgg) """

        label_xgboost = tk.Label(janela_xgboost, image=img_xgboost)
        label_xgboost.pack()

        """ label_vgg = tk.Label(janela_vgg, image=img_outra)
        label_vgg.pack() """

        label_xgboost.image = img_xgboost
        """ label_vgg.image = img_outra """


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

        # Se for para ROIs normalizadas, atualiza o CSV
        if self.current_roi_type == "normalizadas":
            filename = f"ROI_{numero_paciente:02d}_{self.rois[self.roi_index][2].split()[-1]}.png"
            self.atualiza_linha_csv(filename, features)

    def classificar_imagem_vgg16(self):
        model_file = 'vgg16_model.h5'
        if not os.path.exists(model_file):
            messagebox.showerror("Erro", "Modelo VGG16 não encontrado. Por favor, treine o modelo primeiro.")
            return

        file_path = filedialog.askopenfilename(title="Selecione uma imagem para classificar",
                                               filetypes=[("Arquivos de Imagem", "*.jpg;*.png;*.jpeg;*.bmp")])
        if not file_path:
            return

        try:
            img = load_img(file_path, target_size=(224, 224))
            img_array = img_to_array(img)
            img_array = img_array / 255.0  # Normaliza
            img_array = np.expand_dims(img_array, axis=0)  # Adiciona batch

            model = tf.keras.models.load_model(model_file)

            pred = model.predict(img_array)
            class_label = "Saudável" if pred[0][0] < 0.5 else "Esteatose"
            confidence = pred[0][0] if pred[0][0] >= 0.5 else 1 - pred[0][0]
            confidence_percent = confidence * 100

            messagebox.showinfo("Resultado da Classificação", f"A imagem foi classificada como: {class_label}\n"
                                                              f"Confiança: {confidence_percent:.2f}%")
        except Exception as e:
            messagebox.showerror("Erro", f"Ocorreu um erro ao classificar a imagem:\n{str(e)}")
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
