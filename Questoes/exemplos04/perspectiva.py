"""Perspectiva da questão 04"""

# pylint: disable=no-member
import cv2
import numpy as np

#chama a imagem
img = cv2.imread('gato.jpeg')

pont_origem = np.float32([[84,69], [513,77], [113, 358], [542,366]]) #pontos de origem
pont_destino = np.float32([[0,0], [480,0], [0,300], [480,300]]) #pontos de destino

M = cv2.getPerspectiveTransform(pont_origem, pont_destino)
#recebe os pontos de origem e destino para calcular a matriz m

perspectiva = cv2.warpPerspective(img, M, (480,300)) #aplica a transformação na imagem


#exibir imagem original e com perspectiva
cv2.imshow('Img', img)
cv2.imshow('img perspectiva', perspectiva)
cv2.waitKey(0)
cv2.destroyAllWindows()
