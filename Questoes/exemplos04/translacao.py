"""Translação da questão 04"""

# pylint: disable=no-member
import cv2
import numpy as np

def translacao(image, tx, ty):
    """"FUNCÃO PARA REALIZAR TRANSLAÇÃO"""

    # dimensões da imagem
    rows, cols = image.shape[:2]

    # matriz de translação
    matriz_translacao = np.float32([[1, 0, tx], [0, 1, ty]])

    # translação usando a função warpAffine
    img_transladada = cv2.warpAffine(image, matriz_translacao, (cols, rows))

    return img_transladada

# Carrega uma imagem de exemplo
img = cv2.imread('farol.jpg')

# Define os valores de translação (aqui, movemos 50 pixels para a direita e 30 pixels para baixo)
HORIZONTAL = 50
VERTICAL = 30

# Aplica a translação
img_translada = translacao(img,HORIZONTAL, VERTICAL)

# Exibe as imagens original e transladada
cv2.imshow('Imagem', img)
cv2.imshow('Imagem transladada', img_translada)
cv2.waitKey(0)
cv2.destroyAllWindows()
