# Transformações geométricas disponíveis no OpenCV.

**-Translação:**
A translação é uma ferramenta que desloca objetos ou pontos em uma imagem, de modo mais prático ela pode mover para cima, para baixo, lado direito e esquerdo. 

Funciona da seguinte forma: T(x,y)=(x+tx,y+ty)

Cada ponto na imagem é deslocado por txtx na direção horizontal e tyty na direção vertical
Exemplo prático: Reconhecimento facial

exemplo de uso: Um sistema de vigilância que rastreia um objeto em movimento em um corredor.


**-Rotação:**
A rotação é uma ferramenta usada para rotacionar imagens ou pontos necessarios, onde você delimita o angulo de rotação, calcula a matriz de rotação e aplica.

exemplo: 
angulo_rotacao = 45
matriz_rotacao = cv2.getRotationMatrix2D((largura / 2, altura / 2), angulo_rotacao, 1)
imagem_rotacionada = cv2.warpAffine(imagem, matriz_rotacao, (largura, altura))


exemplo de uso: correção de Fotografia de documentos ou quadros onde a orientação não está correta.


**-Redimensionamento:**
O redimensionamento serve para alterar dimensões da imagem, podendo tanto diminuir como aumentar apartir do seu tamanho original.

exemplo de uso: Treinamento de uma rede neural convolucional (CNN) para classificação de imagens.


**-Perspectiva:**
A perspectiva muda o ponto de referencia da visão, normalmente é usada para corrigir distorções causadas por angulos de visão

exemplo: 

Definir os pontos de origem e destino para a transformação de perspectiva
pontos_origem = np.float32([[x1, y1], [x2, y2], [x3, y3], [x4, y4]])
pontos_destino = np.float32([[0, 0], [largura, 0], [0, altura], [largura

Calcular a matriz de perspectiva
matriz_perspectiva = cv2.getPerspectiveTransform(pontos_origem, pontos_destino)

Aplicar a transformação de perspectiva à imagem
imagem_transformada = cv2.warpPerspective(imagem, matriz_perspectiva, (largura, altura))

exemplo de uso:Digitalização de uma página de um livro onde a perspectiva não é frontal.


# Matrizes de transformação

Matrizes de transformação são utilizadas para representar operações geométricas, de translação, rotação, escala e perspectiva. Cada transformação tem uma matriz associada que define como as coordenadas dos pontos da imagem são alteradas durante a transformação.

Translação (Tx, Ty);

Rotação (θθ);

Escalamento (Sx, Sy):

Perspectiva (PxPx​ e PyPy​);