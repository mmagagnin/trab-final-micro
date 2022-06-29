from cv2 import *

stream=VideoCapture(0)

while True:
    _, imagem = stream.read()
   
    linhas = 7
    colunas = 8
    tamanho = 60
   
    #desenhando tabuleiro
    i=0
    x1=0
    while i<linhas:
        rectangle(imagem,pt1=(x1,0),pt2=(x1+tamanho,linhas*tamanho),color=(90,90,90),thickness=3)
        x1+=tamanho
        i+=1
       
    j=0
    y1=0
    while j<colunas-1:
        rectangle(imagem,pt1=(0,y1),pt2=(colunas*tamanho,y1+tamanho),color=(90,90,90),thickness=3)
        y1+=tamanho
        j+=1
       
    imagemHSV = cvtColor(imagem,COLOR_BGR2HSV)
    laranja_escuro=(0,90,255)
    laranja_claro=(0,230,255)
    mascara = inRange(imagemHSV,laranja_escuro,laranja_claro)
   
    contornos,_ = findContours(mascara,RETR_TREE,CHAIN_APPROX_SIMPLE)
   
    #detecta quando uma bolinha laranja entra no campo da camera
    for contorno in contornos:
        x,y,comprimento,altura = boundingRect(contorno)
        #print(x,y)
        coordx=x//60
        coordy=y//60
        print("Coordenadas: ("+str(coordx+1)+","+str(coordy+1)+")")
       

    imshow("Minha Janela",imagem)
   
    if waitKey(1) & 0xFF == ord("q"):
        break
   
stream.release()
destroyAllWindows()