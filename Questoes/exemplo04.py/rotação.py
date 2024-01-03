import cv2
import numpy as np

img =cv2.imread('farol.jpg')#para ler a imagem, chamando o caminho.

#converter para cinza
imgCinza = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)

#binarizar imagem
_,th1 = cv2.threshold(imgCinza,127,255,cv2.THRESH_BINARY)

#encontrar contornos da iamgem binarizada
contornos,hierarquia = cv2.findContours(th1,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_NONE)


# Calcular a média das orientações dos contornos
angulos = [cv2.minAreaRect(cnt)[-1] for cnt in contornos]
angulo_medio = np.mean(angulos)


# Converter o ângulo para graus
angulo_graus = np.degrees(angulo_medio)

# Rotacionar a imagem para corrigir a orientação
altura, largura = img.shape[:2]
ponto_central = (largura // 2, altura // 2)
matriz_rotacao = cv2.getRotationMatrix2D(ponto_central, angulo_graus, 1.0)
imgRotacionada = cv2.warpAffine(th1, matriz_rotacao, (largura, altura), flags=cv2.INTER_LINEAR)



cv2.imshow('imagem', img) #para exibir a imagem na tela
cv2.imshow('imagem cinza', imgRotacionada) #para exibir a imagem de outra cor na tela
cv2.waitKey(0) #para travar o frame na tela