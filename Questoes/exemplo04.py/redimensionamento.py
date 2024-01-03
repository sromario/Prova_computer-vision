import cv2

# Ler a imagem
img = cv2.imread('farol.jpg')

# Definir as novas dimensões desejadas (largura, altura)
nova_largura = 400
nova_altura = 300

# redimensionar
img_redimensionada = cv2.resize(img, (nova_largura, nova_altura))

# Exibir as imagens
cv2.imshow('Imagem ', img)
cv2.imshow('Imagem redimensionada', img_redimensionada)
cv2.waitKey(0)
cv2.destroyAllWindows()
