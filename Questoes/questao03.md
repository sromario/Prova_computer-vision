# Principais estruturas de dados ultizadas pelo opencv para representar imagem e video:

Vamos fazer essa análise como se estivessemos formando um código, com passos e explicando cada funcionalidade e seu papel.


**-Mat(matriz):**
esse é o primeiro passo do nosso código, Mat(matriz) tem a função de ler nossa imagem, armazenando informações como pixeis, altura, largura e tipo de dado.

exemplo: ```img = cv2.imread('farol.jpg')```


**-VideoCapture:**
No próximo passo, vamos simular que agora quero abrir um vídeo ou até minha webcam. Para isso  usamos a classe VideoCapture para captura do vídeo ou câmeras. então, após definir uma váriavel e atribuir a classe video capture, iremos chamar Mat para ler e armazenar informações sobre webcam. 

exemplo: ```webcam = cv2.VideoCapture(0)``` 
         ```img = webcam.read()```
            

**-VideoWriter:**
já no tericeiro passo, vamos supor que agora eu queira salvar meu vídeo da webcam ou fazer uma modificação em uma imagem anterior, recortando alguns pontos, e desejo salvar a imagem. Então, para tal, usarei o VideoWriter.

exemplo: ```recorte = img[y:y+h, x:x+w] #recortando objeto da imagem original cv2.imwrite(f'recortes/recorte{numOB}.jpg',recorte) #salvando imagem com nome e numero```

Vale lembrar que essa classe também tem função de simular escrever um arquivo de video, gerar os quadros de video.

**-Rect (Retângulo):**
vamos agora adicionar retângulos em áreas espécificas. Suponhamos que eu tenha uma imagem com 03 (três) objetos e queira separá-los e formar uma nova imagem com eles de forma individual; para isso eu posso usar o rect para ter dimensão deles e inseri-los em retângulos. Logo, essa função pode ser útil para casos como o acima, onde eu precisei delimitar uma determinada área, para então salvar essa nova imagem com o .writer

exemplo: ```for x,y,l,a in objetos: cv2.rectangle(img,(x,y),(x+l,y+a),(255,0,0),2) ```

assim, eu consigo colocar o retângulo dentro dos parâmetros passados.

**-Size:**
agora vamos imaginar que eu queira realizar todos esses procedimentos acima, mas ainda assim estou com uma tela muito grande e isso atrapalha minha visualização na hora de trabalhar. Então, eu posso dar um size nessa imagem ou vídeo e diminuir suas dimensões, ou até aumentar em casos contrários ao meu.

exemplo:  ```imagemRedim = cv2.resize(imagem,(600,640))```

**-Scalar:**
para finalizar eu queria que meu retângulo estivesse com outra cor. Como posso fazer isso? Usando o scalar podemos brincar com a base de dados visuais ao mudar a cor do retângulo, linhas ou textos.

exemplo: ```cv2.rectangle(img,(50,50),(200,200),(255,0,0),3)```

Aqui eu atribuí retângulo no eixo 50 até 200, cor 255 (azul) e largura 3, e essa cor pode variar de acordo com a sua indicação.



# Qual principal direfença entre uma matriz numpy e demais classes do opencv?


A matriz NumPy (numpy.ndarray) segue sendo muito boa em conjunto com OpenCV, por ser uma poderosa biblioteca que caminha ao lado do OpenCV para o desenvolvimento computacional, porém o segundo conta com boas ferramentas próprias também, como o caso do Mat (matriz). No entanto, o conjunto NumPy tem mais foco no que tange dados numéricos e computação numérica, seguindo mais com o numpy.ndarray. Já os próprios do OpenCV seguem com um foco mais para o processamento de imagens, um exemplo disso é que não temos algo similar ao VideoCapture no próprio NumPy, mas podemos usar em conjunto com o OpenCV e fazer algo mais eficiente.

exemplo: ret, frame = cap.read()

Aqui nós temos um read () que faz parte do VideoCapture, mas temos o ret como um indicador de sucesso e temos o frame para o quadro de vídeo como um NumPy array. Com isso, o frame pode agir tanto como manipulação de arrays multidimensionais, como processamento de imagem,  análise de dados, etc.

Logo ambos têm seus pontos de foco no que tange às áreas de atuação. Então, irá depender da análise do desenvolvedor entender o que mais se aplica a sua necessidade. Geralmente usa-se uma OpenCV para manipulação de imagem e NumPy para operações numéricas, e combinadas são essenciais para desenvolvimentos de projetos em visão computacional

# Qual a importância de compreender essas estruturas ao trabalhar com algoritmos de visão computacional?

A compreensão das estruturas da visão computacional é essencial para o sucesso do desenvolvimento e implementação do seu trabalho. Para além do conhecimento dos questionamentos acima, expostos no nosso passo a passo, vale ressaltar que ter esses fundamentos é crucial para definir o propósito real do projeto, além da melhor escolha das ferramentas que, consequentemente, traz mais sucesso ao desenvolver.
