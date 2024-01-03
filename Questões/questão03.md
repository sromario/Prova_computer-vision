# Principais estruturas de dados ultizadas pelo opencv para representar imagem e video:

Vamos fazer essa análise como se estivessemos formamdo um código, com passos e explicando cada funcionalida e seu papel.


**-Mat(matriz):**
Esse é o primeiro passo do nosso código, Mat(matriz) é tem a função de ler nossa imagem, armazenando informações como: pixeis, altura, largura e tipo de dado.

exemplo: ```img = cv2.imread('farol.jpg')```


**-VideoCapture:**
No próximo passo, vamos simular que agora quero abrir um vídeo ou até minha webcam. Para isso  usamos a classe VideoCapture para captura do vídeo ou câmeras. então, após definir uma váriavel e atribuir a classe video capture, iremos chamar Mat para ler e armazenar informações sobre webcam. 

exemplo: ```webcam = cv2.VideoCapture(0)``` 
         ```img = webcam.read()```
            

**-VideoWriter:**
Nesse terceiro passo, supomos que agora eu queira salvar meu vídeo da webcam, ou fiz uma modificação em uma imagem anterior, recortando alguns pontos e quero salvar. Então, usarei o videoWriter para salvar esse novo frame.

exemplo: ```recorte = img[y:y+h, x:x+w] #recortando objeto da imagem original cv2.imwrite(f'recortes/recorte{numOB}.jpg',recorte) #salvando imagem com nome e numero```

Esse exemplo é de simular uma imagem, onde eu queria retirar alguns objetos e depois salvar a nova imagem.

**-Rect (Retângulo):**
Vamos agora adicionar retângulos em áreas espécificas, suposmos que tenho uma imagem com 3(três) objetos e quero separalos e forma uma nova imagem com eles de forma individual, posso usar o rect para ter dimensão deles e inserir-los em retângulos. Logo, essa função pode ser útil para casos como o acima, onde eu precisei delimitar uma determinada área, para então salvar essa nova imagem com o .writer.

exemplo: ```for x,y,l,a in objetos: cv2.rectangle(img,(x,y),(x+l,y+a),(255,0,0),2) ```

assim, eu consigo colocar o retângulo dentro dos parâmetros passados.

**-Size:**
Agora vamos imaginar que eu quero realizar todos esses procedimentos acima, mas ainda sim estou com uma tela muito grande e isso atrapalha minha visualização na hora de trabalhar. Então, eu posso dar um size nessa imagem ou vídeo e diminuir suas dimensões, ou até aumentar em casos contrários ao meu.

exemplo:  ```imagemRedim = cv2.resize(imagem,(600,640))```

**-Scalar:**
Para finalizar, eu queria que meu retângulo estivesse com outra cor, como posso fazer isso? usando o scalar podemos brincar com a base de dados visuais, podemos mudar cor do retângulo, linhas ou textos.

exemplo: ```cv2.rectangle(img,(50,50),(200,200),(255,0,0),3)```

aqui eu atribuir retangulo no eixo 50 até 200, cor 255(azul) e largura 3. e essa cor pode variar de acordo com a sua indicação.



# Qual principal direfença entre uma matriz numpy e demais classes do opencv?

A matriz numpy(numpy.ndarray) segue sendo muito boa em conjunto com opencv, é uma poderosa biblioteca que caminha em conjunto com opencv para o desenvolvimento computacional. Mas, o opencv conta com boas ferramentas próprias também, como o caso do mat(matriz). Contudo, o conjunto numpy tem mais foco no que tange dados númericos, computação núnmerica segue mais com numpy.ndarray. no entanto, o mat segue com um foco mais para o processamento de imagens.

Logo, ambos tem seus pontos de foco, no que tange áreas de atuação. então, irá depender da análise do desenvolvedor entender o que mais se aplica a sua necessidade

# Qual a importância de compreender essas estruturas ao trabalhar com algoritmos de visão computacional?

Compreender as estruturas de dados ao trabalhar com algoritmos de visão computacional é crucial para o sucesso do desenvolvimento e implementação do seu trabalho. Além de todo conhecimeento que construimos com nossos passos, Aqui estão algumas razões pelas quais é importante ter um entendimento sólido dessas estruturas:

    -Manipulação Eficiente de Dados;
    -Integração com Bibliotecas Específicas;
    -Eficiência em Operações Numéricas;
    -Otimização de Algoritmos;
    -Aplicação de Técnicas de Processamento de Imagem.
    -desing dos dados