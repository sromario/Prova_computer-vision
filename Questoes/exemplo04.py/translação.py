import cv2
import numpy as np

def translacao(image, tx, ty):

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
horizontal = 50
vertical = 30

# Aplica a translação
img_translada = translacao(img,horizontal, vertical)

# Exibe as imagens original e transladada
cv2.imshow('Imagem', img)
cv2.imshow('Imagem transladada', img_translada)
cv2.waitKey(0)
cv2.destroyAllWindows()
