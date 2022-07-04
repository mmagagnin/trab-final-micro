from cv2 import *

stream=VideoCapture(0)

def matrizInv(m):
    mInv=[]
    i=0
    j=0
    while j<8:
        mInv.append([])
        while i<5:
            mInv[j].append(m[i][j])
            i+=1
        i=0
        j+=1
    return mInv

def matrizLuzes(mInv):
    mLuzes=[]
    i=0
    while i<len(mInv):
        if i%2==0:
            mLuzes.append(mInv[i])
        else:
            mLuzes.append(mInv[i][::-1])
        i+=1
    return mLuzes

def criaString(m):
    s="posicao:"
    for lista in m:
        for bolinha in lista:
            if bolinha==None:
                s+="W"
            elif bolinha=="azul":
                s+="B"
            elif bolinha=="preto":
                s+="X"
            elif bolinha=="vermelho":
                s+="R"
            elif bolinha=="verde":
                s+="G"
            elif bolinha=="laranja":
                s+="O"
    return s

while True:
    _, imagem = stream.read()
   
    linhas = 5
    colunas = 8
    tamanho = 60
   
   
   
    #tabuleiro matriz
    matriz=[[None,None,None,None,None,None,None,None],
            [None,None,None,None,None,None,None,None],
            [None,None,None,None,None,None,None,None],
            [None,None,None,None,None,None,None,None],
            [None,None,None,None,None,None,None,None],
            ]

#        
    imagemHSV = cvtColor(imagem,COLOR_BGR2HSV)
   
    dCores={"vermelho":{"escuro":(0,100,70),"claro":(10,255,255)}}
   
#"amarelo":{{"escuro":(),"claro":()}},"azul":{{"escuro":(),"claro":()}},"verde":{{"escuro":(),"claro":()}},"rosa":{{"escuro":(),"claro":()}},"roxo":{{"escuro":(),"claro":()}}
    for cor,dCor in dCores.items():
        mascara = inRange(imagemHSV,dCor["escuro"],dCor["claro"])
        imagem2 = bitwise_and(imagem, imagem, mask=mascara)
        imshow("Janela1",imagem2)
        contornos,_ = findContours(mascara,RETR_TREE,CHAIN_APPROX_SIMPLE)
       
       
    #detecta quando uma bolinha vermelha entra no campo da camera
        for contorno in contornos:
            x,y,comprimento,altura = boundingRect(contorno)
            if comprimento*altura>=3000:
                coordx=(x-60)//60
                coordy=(y-60)//60
                if coordx<=8 and coordy<=5:
                    rectangle(imagem,pt1=(x,y),pt2=(x+comprimento,y+altura),color=(240,250,70),thickness=2)
                    #putText(imagem,("VERMELHO: Linha: "+str(coordy+1)+", Coluna: "+str(coordx+1)),(20,30),color=(0,0,255),fontFace=FONT_HERSHEY_SIMPLEX,fontScale=1,thickness=4)
                    print(cor+" - Linha: "+str(coordy+1)+", Coluna: "+str(coordx+1))
                    matriz[coordy][coordx]=cor
                    print(matriz)

       
    #desenhando tabuleiro
    i=0
    x1=60
    y1=60
   
    while i<colunas:
        rectangle(imagem,pt1=(x1,y1),pt2=(x1+tamanho,(linhas+1)*tamanho),color=(90,90,90),thickness=3)
        x1+=tamanho
        i+=1
#        
    j=0
    x1=60
    y1=60
    while j<linhas:
        rectangle(imagem,pt1=(x1,y1),pt2=((colunas+1)*tamanho,y1+tamanho),color=(240,50,70),thickness=3)
        y1+=tamanho
        j+=1

    imshow("Minha Janela",imagem)
   
   
    if waitKey(1) & 0xFF == ord("q"):
        break
   
   
stream.release()
destroyAllWindows()