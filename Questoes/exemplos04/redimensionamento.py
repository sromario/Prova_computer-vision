"""Redimensionamento da questão 04"""

# pylint: disable=no-member
import cv2

# Ler a imagem
img = cv2.imread('farol.jpg')

# Definir as novas dimensões desejadas (largura, altura)
NOVA_LARGURA = 400
NOVA_ALTURA = 300

# redimensionar
img_redimensionada = cv2.resize(img, (NOVA_LARGURA, NOVA_ALTURA))

# Exibir as imagens
cv2.imshow('Imagem ', img)
cv2.imshow('Imagem redimensionada', img_redimensionada)
cv2.waitKey(0)
cv2.destroyAllWindows()
