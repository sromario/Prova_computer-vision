import cv2

img = cv2.imread('farol.jpg') #para ler a imagem, chamando o caminho

imgCinza = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY) # trasforma imagem da variavel img em cinza 

imgBlur =cv2.blur(imgCinza,(3,3)) #para suavizar a imagem com filtro 3x3

_,th1 = cv2.threshold(imgCinza,127,255,cv2.THRESH_BINARY) #binarizar a imgCinza e suavizada, Pixels com intensidade maior que 127 serão definidos como brancos, e pixels com intensidade menor ou igual a 127 serão definidos como pretos. e 255 a intensidade

cv2.imshow('imagem cinza0', imgCinza) #para exibir a imagem depois de cinza 
cv2.imshow('imagem cinzaSuavizada', imgBlur) #para exibir a imagem depois de cinza e suavizada 
cv2.imshow('imagem final', th1) #para exibir a imagem depois de cinza, suavizada e binarizada

caminho = 'Questão01/' #o caminho da pasta que a imagem vai parar
cv2.imwrite(f'{caminho}nova.jpg',th1) #salvando foto nova
print('imagem salva com sucesso')
cv2.waitKey(0) #para travar o frame na tela e encerrar programa com qualquer tecla
