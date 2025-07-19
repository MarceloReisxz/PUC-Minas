import pygame
import tkinter as tk
from tkinter import simpledialog
import math

# -------- TP1 - MARCELO REIS --------

# Janela, Fonte e Dimensoes
pygame.init()
pygame.display.set_caption('TP-1 - Marcelo Reis - CG')
fonte = pygame.font.SysFont("arial", 13)
LARGURA, ALTURA = 1600, 900
# Centro da tela
MEIO_X, MEIO_Y = LARGURA // 2, ALTURA // 2  
tela = pygame.display.set_mode((LARGURA, ALTURA))

# Variaveis globais para uso
xmin, ymin = 0, 0 
xmax, ymax = 0, 0
pontoJanela1 = None
pontoJanela2 = None
recebeuPontoJanela2 = False        
linhasBresenham = [] 
linhasDDA = []
circunferencias = []
funcaoSelecionada = None
pontoInicial = None
pontoFinal = None
recebeuPontoFinal = False
botoes = []
pontos = []

# Cores (RGB)
ROXO = (106, 106, 208)
BRANCO = (255, 255, 255)
PRETO = (0, 0, 0)
ROXO_ESCURO = (58, 58, 196)
VERMELHO = (255, 0, 0)
VERDE = (0, 255, 0)
AZUL = (0, 0, 255)
AMARELO = (255, 255, 0)
coresDisponiveis = [PRETO, AZUL, VERDE, VERMELHO, ROXO_ESCURO, AMARELO]
corSelecionada = PRETO
janelaSelecionada = None

# Cria os eixos cartesianos na tela
def preencheBranco():
    tela.fill(BRANCO)

# Converte coordenadas para o plano cartesiano
def telaParaCartesiano(x, y):
    x_c = x - MEIO_X
    y_c = MEIO_Y - y
    return x_c, y_c

# Converte coordenadas para coordenadas de tela
def cartesianoParaTela(x, y):
    x_t = x + MEIO_X
    y_t = MEIO_Y - y
    return x_t, y_t

# Plota um pixel
def plotaPixel(x, y, cor=None):
    if cor is None:
        cor = corSelecionada
    x_t, y_t = cartesianoParaTela(x, y)
    if 0 <= x_t < LARGURA and 0 <= y_t < ALTURA:
        tela.set_at((int(x_t), int(y_t)), cor)

# Cria todos os pontos
def criaPontos():
    for ponto in pontos:
        plotaPixel(ponto[0], ponto[1])

# Cria todas as linhas Bresenham
def criaLinhasBresenham():
    for linha in linhasBresenham:
        x0, y0 = linha[0]
        x1, y1 = linha[1]
        if xmin != xmax and ymin != ymax and janelaSelecionada == 'Liang-Barsky':
            liang(x0, y0, x1, y1)
        elif xmin != xmax and ymin != ymax and janelaSelecionada == 'Cohen-Sutherland':
            cohen_sutherland(x0, y0, x1, y1)
        else:
            linhaBresenham(x0, y0, x1, y1)

# Cria todas as linhas DDA
def criaLinhasDDA():
    for linha in linhasDDA:
        x0, y0 = linha[0]
        x1, y1 = linha[1]
        if xmin != xmax and ymin != ymax and janelaSelecionada == 'Liang-Barsky':
            liang(x0, y0, x1, y1)
        elif xmin != xmax and ymin != ymax and janelaSelecionada == 'Cohen-Sutherland':
            cohen_sutherland(x0, y0, x1, y1)
        else:
            linhaDDA(x0, y0, x1, y1)

# Cria todas as circunferências
def criaCircunferencias():
    for circ in circunferencias:
        xc, yc, raio = circ
        circunferenciaBresenham(xc, yc, raio)

# Cria os botões na tela
def criaBotoes():
    botoes = []
    opcoes = [
        'Plotar Pixel',
        'Transladar',
        'Rotacionar',
        'Escalar',
        'Reflexão X',
        'Reflexão Y',
        'Reflexão XY',
        'Linha DDA',
        'Linha Bresenham',
        'Circunferência',
        'Liang-Barsky',
        'Cohen-Sutherland',
        'Limpar Tela'
    ]
    # Posição dos botões
    x, y = 0, 0
    largura_botao, altura_botao = 115, 40 

    for opcao in opcoes:
        retangulo = pygame.Rect(x, y, largura_botao, altura_botao)
        if opcao == funcaoSelecionada:
            cor_botao = ROXO_ESCURO  # Cor do botão selecionado
        else:
            cor_botao = ROXO  # Cor normal do botão
            
        pygame.draw.rect(tela, cor_botao, retangulo)
        texto = fonte.render(opcao, True, BRANCO)
        tela.blit(texto, (x + 10, y + 10))
        
        # Adiciona o botão à lista de botões para detecção de clique
        botoes.append((retangulo, opcao))
        # Atualiza a posição do próximo botão
        x += largura_botao + 5
    
    # Adiciona lista de botões de cor
    for cor in coresDisponiveis:
        retangulo_cor = pygame.Rect(x, y, 50, 50)
        pygame.draw.rect(tela, cor, retangulo_cor)
        botoes.append((retangulo_cor, cor))
        y += 55

    return botoes

def selecionarJanela(posicaoMouse):
    global xmin, ymin, xmax, ymax, pontoJanela1, pontoJanela2, recebeuPontoJanela2
    if not pontoJanela1:
        pontoJanela1 = telaParaCartesiano(*posicaoMouse)
        recebeuPontoJanela2 = True
    elif recebeuPontoJanela2:
        pontoJanela2 = telaParaCartesiano(*posicaoMouse)
        # Define a janela de recorte
        xmin = min(pontoJanela1[0], pontoJanela2[0])
        ymin = min(pontoJanela1[1], pontoJanela2[1])
        xmax = max(pontoJanela1[0], pontoJanela2[0])
        ymax = max(pontoJanela1[1], pontoJanela2[1])
        pontoJanela1 = None
        pontoJanela2 = None
        recebeuPontoJanela2 = False
        desenhaJanelaRecorte()
        
def desenhaJanelaRecorte():
    global linhasDDA
    global funcaoSelecionada
    if xmin != xmax and ymin != ymax:
        # Lado inferior
        linhaDDA(xmin, ymin, xmax, ymin, VERMELHO)
        linhasDDA.append(((xmin, ymin), (xmax, ymin)))

        # Lado direito
        linhaDDA(xmax, ymin, xmax, ymax, VERMELHO)
        linhasDDA.append(((xmax, ymin), (xmax, ymax)))

        # Lado superior
        linhaDDA(xmax, ymax, xmin, ymax, VERMELHO)
        linhasDDA.append(((xmax, ymax), (xmin, ymax)))

        # Lado esquerdo
        linhaDDA(xmin, ymax, xmin, ymin, VERMELHO)
        linhasDDA.append(((xmin, ymax), (xmin, ymin)))
        
        funcaoSelecionada = None
        atualizaTela()

def codigoRegiao(x, y):
    code = 0
    if x < xmin:
        code |= 1  # Esquerda
    elif x > xmax:
        code |= 2  # Direita
    if y < ymin:
        code |= 4  # Abaixo
    elif y > ymax:
        code |= 8  # Acima
    return code

def cohen_sutherland(x1, y1, x2, y2, cor=None):
    aceite = False
    feito = False

    while not feito:
        c1 = codigoRegiao(x1, y1)
        c2 = codigoRegiao(x2, y2)

        if c1 == 0 and c2 == 0:
            aceite = True
            feito = True
        elif (c1 & c2) != 0:
            feito = True
        else:
            cfora = c1 if c1 != 0 else c2

            if cfora & 1:  # Limite esquerdo
                xint = xmin
                yint = y1 + (y2 - y1) * (xmin - x1) / (x2 - x1)
            elif cfora & 2:  # Limite direito
                xint = xmax
                yint = y1 + (y2 - y1) * (xmax - x1) / (x2 - x1)
            elif cfora & 4:  # Limite inferior
                yint = ymin
                xint = x1 + (x2 - x1) * (ymin - y1) / (y2 - y1)
            elif cfora & 8:  # Limite superior
                yint = ymax
                xint = x1 + (x2 - x1) * (ymax - y1) / (y2 - y1)

            if cfora == c1:
                x1, y1 = xint, yint
            else:
                x2, y2 = xint, yint

    if aceite:
        if funcaoSelecionada == 'Linha DDA':
            linhaDDA(x1, y1, x2, y2, cor)
        elif funcaoSelecionada == 'Linha Bresenham':
            linhaBresenham(x1, y1, x2, y2, cor)
        else:
            linhaDDA(x1, y1, x2, y2, cor)

def cliptest(p, q, u1, u2):
    result = True
    if p == 0 and q < 0:
        result = False
    elif p < 0:
        r = q / p
        if r > u2[0]:
            result = False
        elif r > u1[0]:
            u1[0] = r
    elif p > 0:
        r = q / p
        if r < u1[0]:
            result = False
        elif r < u2[0]:
            u2[0] = r
    return result

def liang(x1, y1, x2, y2, cor=None):
    global xmin, ymin, xmax, ymax
    dx = x2 - x1
    dy = y2 - y1
    u1 = [0.0]
    u2 = [1.0]

    if cliptest(-dx, x1 - xmin, u1, u2):  # Teste para borda esquerda
        if cliptest(dx, xmax - x1, u1, u2):  # Teste para borda direita
            if cliptest(-dy, y1 - ymin, u1, u2):  # Teste para borda inferior
                if cliptest(dy, ymax - y1, u1, u2):  # Teste para borda superior
                    if u2[0] < 1:
                        x2 = x1 + dx * u2[0]
                        y2 = y1 + dy * u2[0]
                    if u1[0] > 0:
                        x1 = x1 + dx * u1[0]
                        y1 = y1 + dy * u1[0]

                    if funcaoSelecionada == 'Linha DDA':
                        linhaDDA(x1, y1, x2, y2, cor)
                    elif funcaoSelecionada == 'Linha Bresenham':
                        linhaBresenham(x1, y1, x2, y2, cor)
                    else:
                        linhaDDA(x1, y1, x2, y2, cor)

# ------------- Transformações geométricas -------------

# Translação -> pontos
def transladaPontos(pontos, dx, dy):
    novos_pontos = []
    for x, y in pontos:
        x_novo = x + dx
        y_novo = y + dy
        novos_pontos.append((x_novo, y_novo))
    return novos_pontos

# Translação -> linhas
def transladaLinhas(linhas, dx, dy):
    novas_linhas = []
    for linha in linhas:
        (x0, y0), (x1, y1) = linha
        x0_novo = x0 + dx
        y0_novo = y0 + dy
        x1_novo = x1 + dx
        y1_novo = y1 + dy
        novas_linhas.append(((x0_novo, y0_novo), (x1_novo, y1_novo)))
    return novas_linhas

# Translação -> circunferências
def transladaCircunferencias(circunferencias, dx, dy):
    novas_circunferencias = []
    for circ in circunferencias:
        xc, yc, raio = circ
        xc_novo = xc + dx
        yc_novo = yc + dy
        novas_circunferencias.append((xc_novo, yc_novo, raio))
    return novas_circunferencias

# Rotação -> pontos
def rotacionaPontos(pontos, angulo):
    novos_pontos = []
    rad = math.radians(angulo)  
    cos_ang = math.cos(rad)
    sin_ang = math.sin(rad)
    for x, y in pontos:
        x_novo = x * cos_ang - y * sin_ang
        y_novo = x * sin_ang + y * cos_ang
        novos_pontos.append((x_novo, y_novo))
    return novos_pontos

# Rotação -> linhas
def rotacionaLinhas(linhas, angulo):
    novas_linhas = []
    rad = math.radians(angulo)
    cos_ang = math.cos(rad)
    sin_ang = math.sin(rad)
    for linha in linhas:
        (x0, y0), (x1, y1) = linha
        x0_novo = x0 * cos_ang - y0 * sin_ang
        y0_novo = x0 * sin_ang + y0 * cos_ang
        x1_novo = x1 * cos_ang - y1 * sin_ang
        y1_novo = x1 * sin_ang + y1 * cos_ang
        novas_linhas.append(((x0_novo, y0_novo), (x1_novo, y1_novo)))
    return novas_linhas

# Rotação -> circunferências
def rotacionaCircunferencias(circunferencias, angulo):
    novas_circunferencias = []
    rad = math.radians(angulo)
    cos_ang = math.cos(rad)
    sin_ang = math.sin(rad)
    for circ in circunferencias:
        xc, yc, raio = circ
        xc_novo = xc * cos_ang - yc * sin_ang
        yc_novo = xc * sin_ang + yc * cos_ang
        novas_circunferencias.append((xc_novo, yc_novo, raio))
    return novas_circunferencias

# Escala -> pontos
def escalaPontos(pontos, sx, sy):
    novos_pontos = []
    for x, y in pontos:
        x_novo = x * sx
        y_novo = y * sy
        novos_pontos.append((x_novo, y_novo))
    return novos_pontos

# Escala -> linhas
def escalaLinhas(linhas, sx, sy):
    novas_linhas = []
    for linha in linhas:
        (x0, y0), (x1, y1) = linha
        x0_novo = x0 * sx
        y0_novo = y0 * sy
        x1_novo = x1 * sx
        y1_novo = y1 * sy
        novas_linhas.append(((x0_novo, y0_novo), (x1_novo, y1_novo)))
    return novas_linhas

# Escala -> circunferências
def escalaCircunferencias(circunferencias, sx, sy):
    novas_circunferencias = []
    s_media = (sx + sy) / 2
    for circ in circunferencias:
        xc, yc, raio = circ
        xc_novo = xc * sx
        yc_novo = yc * sy
        raio_novo = raio * s_media
        novas_circunferencias.append((xc_novo, yc_novo, raio_novo))
    return novas_circunferencias

# Reflexão -> pontos
def refletePontos(pontos, eixo):
    novos_pontos = []
    for x, y in pontos:
        # Reflexão -> eixo X
        if eixo == 'x':
            novos_pontos.append((x, -y))
        # Reflexão -> eixo Y   
        elif eixo == 'y':
            novos_pontos.append((-x, y))
        # Reflexão -> eixos X e Y    
        elif eixo == 'xy':
            novos_pontos.append((-x, -y))   
    return novos_pontos

# Reflexão -> linhas
def refleteLinhas(linhas, eixo):
    novas_linhas = []
    for linha in linhas:
        (x0, y0), (x1, y1) = linha
        if eixo == 'x':
            x0_novo, y0_novo = x0, -y0
            x1_novo, y1_novo = x1, -y1
        elif eixo == 'y':
            x0_novo, y0_novo = -x0, y0
            x1_novo, y1_novo = -x1, y1
        elif eixo == 'xy':
            x0_novo, y0_novo = -x0, -y0
            x1_novo, y1_novo = -x1, -y1
        novas_linhas.append(((x0_novo, y0_novo), (x1_novo, y1_novo)))
    return novas_linhas

# Reflexão -> circunferências
def refleteCircunferencias(circunferencias, eixo):
    novas_circunferencias = []
    for circ in circunferencias:
        xc, yc, raio = circ
        if eixo == 'x':
            xc_novo, yc_novo = xc, -yc
        elif eixo == 'y':
            xc_novo, yc_novo = -xc, yc
        elif eixo == 'xy':
            xc_novo, yc_novo = -xc, -yc
        novas_circunferencias.append((xc_novo, yc_novo, raio))
    return novas_circunferencias

# Algoritmo DDA
def linhaDDA(x0, y0, x1, y1, cor=None):
    if cor is None:
        cor = corSelecionada
    x0, y0 = int(x0), int(y0)
    x1, y1 = int(x1), int(y1)
    dx = x1 - x0
    dy = y1 - y0
    passos = max(abs(dx), abs(dy))
    if passos == 0:
        plotaPixel(x0, y0, cor)
        return
    incremento_x = dx / passos
    incremento_y = dy / passos
    x, y = x0, y0
    for _ in range(passos + 1):
        plotaPixel(round(x), round(y), cor)
        x += incremento_x
        y += incremento_y

# Algoritmo Bresenham
def linhaBresenham(x0, y0, x1, y1, cor=None):
    if cor is None:
        cor = corSelecionada
    x0, y0 = int(x0), int(y0)
    x1, y1 = int(x1), int(y1)
    dx = x1 - x0
    dy = y1 - y0
    x = x0
    y = y0
    if dx > 0:
        xincr = 1
    else:
        xincr = -1
        dx = -dx
    if dy > 0:
        yincr = 1
    else:
        yincr = -1
        dy = -dy
    plotaPixel(x, y, cor)
    if dx > dy:
        p = 2 * dy - dx
        c1 = 2 * dy
        c2 = 2 * (dy - dx)
        for _ in range(dx):
            x += xincr
            if(p < 0):
                p += c1
            else:
                p += c2
                y += yincr
            plotaPixel(x, y, cor)
    else:
        p = 2 * dx - dy
        c1 = 2 * dx
        c2 = 2 * (dx - dy)
        for _ in range(dy):
            y += yincr
            if(p < 0):
                p += c1
            else:
                p += c2
                x += xincr
            plotaPixel(x, y, cor)

# Algoritmo Circunferencia Bresenham
def circunferenciaBresenham(xc, yc, raio, cor=None):
    if cor is None:
        cor = corSelecionada
    x = 0
    y = raio
    d = 3 - 2 * raio
    plotarCircunferenciaSimetrica(xc, yc, x, y, cor)
    while y >= x:
        x += 1
        if d > 0:
            y -= 1
            d = d + 4 * (x - y) + 10
        else:
            d = d + 4 * x + 6
        plotarCircunferenciaSimetrica(xc, yc, x, y, cor)

# Plota Circunferencia
def plotarCircunferenciaSimetrica(xc, yc, x, y, cor=None):
    if cor is None:
        cor = corSelecionada
    plotaPixel(xc + x, yc + y, cor)
    plotaPixel(xc - x, yc + y, cor)
    plotaPixel(xc + x, yc - y, cor)
    plotaPixel(xc - x, yc - y, cor)
    plotaPixel(xc + y, yc + x, cor)
    plotaPixel(xc - y, yc + x, cor)
    plotaPixel(xc + y, yc - x, cor)
    plotaPixel(xc - y, yc - x, cor)
    plotaPixel(xc + x, yc + y)
    plotaPixel(xc - x, yc + y)
    plotaPixel(xc + x, yc - y)
    plotaPixel(xc - x, yc - y)
    plotaPixel(xc + y, yc + x)
    plotaPixel(xc - y, yc + x)
    plotaPixel(xc + y, yc - x)
    plotaPixel(xc - y, yc - x)

# Limpa as informações da Tela
def limpaTela():
    global xmin, ymin, xmax, ymax, pontoJanela1, pontoJanela2, recebeuPontoJanela2
    pontos.clear()
    linhasBresenham.clear()
    linhasDDA.clear()
    circunferencias.clear()
    xmin, ymin = 0, 0  
    xmax, ymax = 0, 0  
    pontoJanela1 = None
    pontoJanela2 = None
    recebeuPontoJanela2 = False

# Atualiza as informações da Tela
def atualizaTela():
    global botoes
    preencheBranco()               
    botoes = criaBotoes() # Cria os botões e atualiza a lista de botões
    criaPontos() # Cria os pontos armazenados
    criaLinhasBresenham() # Cria as linhas Bresenham
    criaLinhasDDA() # Cria as linhas DDA
    criaCircunferencias() # Cria as circunferências

# Recebe o fator de Escala   
def obterFatorEscala():
    root = tk.Tk()
    root.withdraw()
    try:
        fator = float(simpledialog.askstring("Fator de Escala", "Digite o fator de escala:"))
        return fator
    except (ValueError, TypeError):
        print("Valor inválido! Digite um número.")
        return None

# Recebe o fator de Rotação 
def obterFatorRotacao():
    root = tk.Tk()
    root.withdraw()
    try:
        angulo = float(simpledialog.askstring("Ângulo de Rotação", "Digite o ângulo de rotação (em graus):"))
        return angulo
    except (ValueError, TypeError):
        print("Valor inválido! Digite um número.")
        return None

# Recebe o fator de Translação
def obterFatorTranslacao():
    root = tk.Tk()
    root.withdraw()
    try:
        dx = float(simpledialog.askstring("Translação em X", "Digite o valor de translação em X:"))
        dy = float(simpledialog.askstring("Translação em Y", "Digite o valor de translação em Y:"))
        return dx, dy
    except (ValueError, TypeError):
        print("Valor inválido! Digite um número.")
        return None, None

# Processa eventos na tela
def processarEventos():
    global controle, funcaoSelecionada, pontoInicial, pontoFinal, recebeuPontoFinal
    global ehBresenham, ehDDA, janelaSelecionada
    
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            controle = False
        elif evento.type == pygame.MOUSEBUTTONDOWN:
            processarCliqueMouse(evento)
        elif evento.type == pygame.KEYDOWN:
            processarTeclaPressionada(evento)

# Processa clique na tela
def processarCliqueMouse(evento):
    global funcaoSelecionada, pontoInicial, pontoFinal, recebeuPontoFinal
    global ehBresenham, ehDDA
    global pontos, linhasDDA, linhasBresenham, circunferencias, funcaoSelecionada

    posicaoMouse = pygame.mouse.get_pos()
    clicou_em_botao = processarBotoes(posicaoMouse)
    
    if funcaoSelecionada == 'Limpar Tela':
        limpaTela()
    elif funcaoSelecionada in ['Escalar', 'Rotacionar']:
        aplicarTransformacao()
    elif funcaoSelecionada == 'Reflexão X':
        pontos = refletePontos(pontos, 'x')
        linhasBresenham = refleteLinhas(linhasBresenham, 'x')
        linhasDDA = refleteLinhas(linhasDDA, 'x')
        circunferencias = refleteCircunferencias(circunferencias, 'x')
        funcaoSelecionada = None
    elif funcaoSelecionada == 'Reflexão Y':
        pontos = refletePontos(pontos, 'y')
        linhasBresenham = refleteLinhas(linhasBresenham, 'y')
        linhasDDA = refleteLinhas(linhasDDA, 'y')
        circunferencias = refleteCircunferencias(circunferencias, 'y')
        funcaoSelecionada = None
    elif funcaoSelecionada == 'Reflexão XY':
        pontos = refletePontos(pontos, 'xy')
        linhasBresenham = refleteLinhas(linhasBresenham, 'xy')
        linhasDDA = refleteLinhas(linhasDDA, 'xy')
        circunferencias = refleteCircunferencias(circunferencias, 'xy')
        funcaoSelecionada = None
    elif funcaoSelecionada == 'Transladar':
        transladarAll()
    elif not clicou_em_botao:
        processarCliqueCanvas(posicaoMouse)

# Processa clique nos botões
def processarBotoes(posicaoMouse):
    global funcaoSelecionada, corSelecionada
    
    for retangulo, opcao in botoes:
        if retangulo.collidepoint(posicaoMouse):
            if opcao in coresDisponiveis:
                corSelecionada = opcao
            else:
                pygame.draw.rect(tela, ROXO_ESCURO, retangulo)
                funcaoSelecionada = opcao
                resetarPontos()
            return True
    return False

# Aplica transformações geométricas
def aplicarTransformacao():
    global funcaoSelecionada
    
    if funcaoSelecionada == 'Escalar':
        fator = obterFatorEscala()
        if fator is not None:
            escalarAll(fator)
    elif funcaoSelecionada == 'Rotacionar':
        angulo = obterFatorRotacao()
        if angulo is not None:
            rotacionarAll(angulo)
    
    funcaoSelecionada = None

# Processa clique nos botões via função
def processarCliqueCanvas(posicaoMouse):
    global pontoInicial, pontoFinal, recebeuPontoFinal, ehBresenham, ehDDA, janelaSelecionada
    
    x_c, y_c = telaParaCartesiano(*posicaoMouse)
    
    if funcaoSelecionada == 'Plotar Pixel':
        pontos.append((x_c, y_c))
    elif funcaoSelecionada == 'Liang-Barsky':
        janelaSelecionada = 'Liang-Barsky'
        selecionarJanela(posicaoMouse)
    elif funcaoSelecionada == 'Cohen-Sutherland':
        janelaSelecionada = 'Cohen-Sutherland'
        selecionarJanela(posicaoMouse)
    elif funcaoSelecionada in ['Linha DDA', 'Linha Bresenham']:
        linha(x_c, y_c)
    elif funcaoSelecionada == 'Circunferência':
        circunferencia(x_c, y_c)
    elif funcaoSelecionada == 'Transladar':
        transladarAll(x_c, y_c)
    else:
        pontos.append((x_c, y_c))

# Processa teclas pressionadas
def processarTeclaPressionada(evento):
    global funcaoSelecionada, pontoInicial, pontoFinal, recebeuPontoFinal
    
    if evento.key == pygame.K_ESCAPE:
        funcaoSelecionada = None
        resetarPontos()

# Chama função de linhas
def linha(x_c, y_c):
    global pontoInicial, pontoFinal, recebeuPontoFinal, ehBresenham, ehDDA
    
    if not pontoInicial:
        ehBresenham = funcaoSelecionada == 'Linha Bresenham'
        ehDDA = funcaoSelecionada == 'Linha DDA'
        pontoInicial = (x_c, y_c)
        recebeuPontoFinal = True
    elif recebeuPontoFinal:
        pontoFinal = (x_c, y_c)
        if ehBresenham:
            linhasBresenham.append((pontoInicial, pontoFinal))
        if ehDDA:
            linhasDDA.append((pontoInicial, pontoFinal))
        resetarPontos()

# Chama função de circunferencia
def circunferencia(x_c, y_c):
    global pontoInicial, pontoFinal, recebeuPontoFinal
    
    if not pontoInicial:
        pontoInicial = (x_c, y_c)
        recebeuPontoFinal = True
    elif recebeuPontoFinal:
        pontoFinal = (x_c, y_c)
        raio = int(math.hypot(pontoFinal[0] - pontoInicial[0], pontoFinal[1] - pontoInicial[1]))
        circunferencias.append((pontoInicial[0], pontoInicial[1], raio))
        resetarPontos()

# Função para resetar pontos
def resetarPontos():
    global pontoInicial, pontoFinal, recebeuPontoFinal, ehBresenham, ehDDA
    
    pontoInicial = None
    pontoFinal = None
    recebeuPontoFinal = False
    ehBresenham = False
    ehDDA = False

# Chama função de translação todos elementos
def transladarAll():
    global pontos, linhasBresenham, linhasDDA, circunferencias, funcaoSelecionada
    
    dx, dy = obterFatorTranslacao()
    if dx is not None and dy is not None:
        pontos = transladaPontos(pontos, dx, dy)
        linhasBresenham = transladaLinhas(linhasBresenham, dx, dy)
        linhasDDA = transladaLinhas(linhasDDA, dx, dy)
        circunferencias = transladaCircunferencias(circunferencias, dx, dy)
        funcaoSelecionada = None
        atualizaTela()

# Chama função de escalar todos elementos
def escalarAll(fator):
    global pontos, linhasBresenham, linhasDDA, circunferencias
    
    pontos = escalaPontos(pontos, fator, fator)
    linhasBresenham = escalaLinhas(linhasBresenham, fator, fator)
    linhasDDA = escalaLinhas(linhasDDA, fator, fator)
    circunferencias = escalaCircunferencias(circunferencias, fator, fator)

# Chama função de rotação todos elementos
def rotacionarAll(angulo):
    global pontos, linhasBresenham, linhasDDA, circunferencias
    
    pontos = rotacionaPontos(pontos, angulo)
    linhasBresenham = rotacionaLinhas(linhasBresenham, angulo)
    linhasDDA = rotacionaLinhas(linhasDDA, angulo)
    circunferencias = rotacionaCircunferencias(circunferencias, angulo)

# Chama função de transladar
def transladar(dx, dy):
    global pontos, linhasBresenham, linhasDDA, circunferencias
    
    pontos = transladaPontos(pontos, dx, dy)
    linhasBresenham = transladaLinhas(linhasBresenham, dx, dy)
    linhasDDA = transladaLinhas(linhasDDA, dx, dy)
    circunferencias = transladaCircunferencias(circunferencias, dx, dy)

def main():
    global controle
    
    controle = True
    while controle:
        atualizaTela()
        processarEventos()
        pygame.display.flip()
    
    pygame.quit()

if __name__ == '__main__':
    main()