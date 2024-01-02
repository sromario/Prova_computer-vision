import cv2


img = cv2.imread('objetos.jpg') #chamar a imagem 
img = cv2.resize(img,(600,500)) #redimensionar o tamnho dela, para caber na tela
imgCinza = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY) #transformar a imagem em cinza
imgcanny = cv2.Canny(imgCinza,30,200) #extrair os contornos da imagem
imgClose = cv2.morphologyEx(imgcanny,cv2.MORPH_CLOSE,(7,7)) #morfologia de closing para ter um fechamento melhor de cada objeto

contornos,hierarquia = cv2.findContours(imgClose,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_NONE) #separar os contornos dando as cordenadas dos contornos


for i in contornos: #para percorrer os contornos achados
    #cv2.drawContours(img,i,-1,(255,0,0),2)** #para desenhar os contornos na imagem
    x,y,w,h = cv2.boundingRect(i) #para passar o contorno em cordenadas para as váriaveis 
    cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2) #criar o retangulo com as cordenadas
    

cv2.imshow('original', img)
#cv2.imshow('cinza', imgCinza)
#cv2.imshow('canny', imgcanny)
cv2.waitKey(0)