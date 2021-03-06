#BIBLIOTECAS
import tkinter as tk
import json
import pygame
from pygame import mixer
from threading import Timer
import time
import threading
from serial import Serial
from threading import Thread, Timer
from time import sleep
import cv2

#meu_serial = Serial("COM14", baudrate=9600)

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
    return s+"\n"

def envio(m):
    mInv=matrizInv(m)
    mLuzes=matrizLuzes(mInv)
    envio=criaString(mLuzes)
    sleep(2)
    
    meu_serial.write(envio.encode("UTF-8"))
    return True


def roda_camera():
    stream=cv2.VideoCapture(0)

    TAMANHO_BOLINHA = 500;

    global matriz
    global lDic
    matriz=[]
    global timer
    timer = None
    meu_serial = Serial("COM14", baudrate=9600, timeout=0.01)

    # def matrizInv(m):
    #     mInv=[]
    #     i=0
    #     j=0
    #     while j<8:
    #         mInv.append([])
    #         while i<5:
    #             mInv[j].append(m[i][j])
    #             i+=1
    #         i=0
    #         j+=1
    #     return mInv
    # 

    def envia_matriz():
        print(matriz)
    #     s=enviaLeds(matriz)
    #     print(s)
        timer= Timer(2, envia_matriz)
        timer.start()
        return
    envia_matriz()

    def vInicialDic(matriz):
        lDic=[]
        i=0
        for linha in matriz:
            lDic.append([])
            for posicao in linha:
                lDic[i].append({"corAntiga":None,"corAtual":None,"contagem":0})
            i+=1
        return lDic

    def atualizaContagemDic(d):
        if d["corAntiga"]==d["corAtual"]:
            d["contagem"]+=1
            if d["contagem"]==5:
                return True
        else:
            d["corAntiga"]=d["corAtual"]
            d["contagem"]=0

    def atualizaLdeDic(matrizNova,lD):
        linha=0
        for row in matrizNova:
            coluna=0
            for bolinha in row:
                lD[linha][coluna]["corAtual"]=matrizNova[linha][coluna]
                if atualizaContagemDic(lD[linha][coluna]):
                    return True
                coluna+=1
            linha+=1

    while True:
        _, imagem = stream.read()

        linhas = 5
        colunas = 8
        tamanho = 70



        #tabuleiro matriz
        matriz=[[None,None,None,None,None,None,None,None],
                [None,None,None,None,None,None,None,None],
                [None,None,None,None,None,None,None,None],
                [None,None,None,None,None,None,None,None],
                [None,None,None,None,None,None,None,None],
                ]

        lDic=vInicialDic(matriz)

    #        
        imagemHSV = cv2.cvtColor(imagem,cv2.COLOR_BGR2HSV)

        dCores={
                "Amarelo":{"escuro":(10, 100, 10),"claro":(25, 255, 255)},
                "Verde":{"escuro":(50,200,10),"claro":(90,255,120)},
                "Vermelho":{"escuro":(0,100,40),"claro":(10,255,255)},
                "Azul":{"escuro":(87,70,170),"claro":(110,210,255)},
                "Preto":{"escuro":(110,215,10),"claro":(125,255,215)},
                "Rosa":{"escuro":(145,80,2),"claro":(190,200,255)},
                "Roxo":{"escuro":(115,35,40),"claro":(130,235,250)}

                }
        #,"azul":{"escuro":(130,250,20),"claro":(115,200,255)}}
    #
    #"amarelo":{{"escuro":(0,25,0),"claro":(0,35,0)}},"verde":{{"escuro":(),"claro":()}},"rosa":{{"escuro":(),"claro":()}},"roxo":{{"escuro":(),"claro":()}}
        for (cor,dCor) in dCores.items():
            mascara = cv2.inRange(imagemHSV,dCor["escuro"],dCor["claro"])
            imagem2 = cv2.bitwise_and(imagem, imagem, mask=mascara)
            cv2.imshow("Janela1",imagem2)
            contornos,_ = cv2.findContours(mascara,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)


        #detecta quando uma bolinha vermelha entra no campo da camera
            for contorno in contornos:
                x,y,comprimento,altura = cv2.boundingRect(contorno)
                if comprimento*altura>=TAMANHO_BOLINHA:
                    coordx=(x-50)//50
                    coordy=(y-50)//50
                    if coordx<=7 and coordy<=4 and coordx>=0 and coordy>=0:
                        cv2.rectangle(imagem,pt1=(x,y),pt2=(x+comprimento,y+altura),color=(240,250,70),thickness=2)
                        #putText(imagem,("VERMELHO: Linha: "+str(coordy+1)+", Coluna: "+str(coordx+1)),(20,30),color=(0,0,255),fontFace=FONT_HERSHEY_SIMPLEX,fontScale=1,thickness=4)
                        #print(cor+" - Linha: "+str(coordy+1)+", Coluna: "+str(coordx+1))
                        matriz[coordy][coordx]=cor
                        #envio(matriz)

    #                     if atualizaLdeDic(matriz,lDic):
    #                         print("LALALALA")
    #                         print(matriz)



        #desenhando tabuleiro
        i=0
        x1=50
        y1=50

        while i<colunas:
            cv2.rectangle(imagem,pt1=(x1,y1),pt2=(x1+tamanho,(linhas+1)*tamanho),color=(90,90,90),thickness=3)
            x1+=tamanho
            i+=1
    #        
        j=0
        x1=50
        y1=50
        while j<linhas:
            cv2.rectangle(imagem,pt1=(x1,y1),pt2=((colunas+1)*tamanho,y1+tamanho),color=(240,50,70),thickness=3)
            y1+=tamanho
            j+=1

        cv2.imshow("Minha Janela",imagem)


        if cv2.waitKey(1) & 0xFF == ord("q"):
            break
    
        #sleep(5)


    stream.release()
    destroyAllWindows()

#threading
def thread_delay(thread_name, delay):
    count = 0
    while count < 3000:
        time.sleep(delay)
        count += 1
        print(thread_name, '-------->', time.time())


#t1 = threading.Thread(target=roda_camera, args=('t1', 1))
t1 = threading.Thread(target=roda_camera, args=())

t1.start()
#Abrindo o json

with open("Dadosescolhidos.json", "r") as arquivo:
    data = json.load(arquivo)
    print(data)
    print(data['instrumentos']['box 1'])

#MIXER

pygame.mixer.init(44100,-16,3,10)
pygame.mixer.set_num_channels(32)


#AUDIOS

#TROMPETE

tdo=pygame.mixer.Sound(file='trom_Do.wav')
tre=pygame.mixer.Sound(file='trom_Re.wav')
tmi=pygame.mixer.Sound(file='trom_Mi.wav')
tfa=pygame.mixer.Sound(file='trom_Fa.wav')
tsol=pygame.mixer.Sound(file='trom_Sol.wav')
tla=pygame.mixer.Sound(file='trom_La.wav')
tsi=pygame.mixer.Sound(file='trom_Si.wav')

trompete={"D??":tdo,"R??":tre,"Mi":tmi,"Fa":tfa,"Sol":tsol,"La":tla,"Si":tsi}

#DRUMS

snare=pygame.mixer.Sound(file='snare.wav')
kick=pygame.mixer.Sound(file='kick.wav')
hihat=pygame.mixer.Sound(file='hi-hat.wav')
clap=pygame.mixer.Sound(file='clap.wav')
sino=pygame.mixer.Sound(file='sino.wav')
moresnare=pygame.mixer.Sound(file='moresnare.wav')
triangulo=moresnare=pygame.mixer.Sound(file='triangulo.wav')

drums={"D??":snare,"R??":kick,"Mi":hihat,"Fa":clap,"Sol":sino,"La":moresnare,"Si":triangulo}

#BAIXO

soundb1=pygame.mixer.Sound(file='baixo1.wav')
b1raw_array_ = soundb1.get_raw()
soundb2=pygame.mixer.Sound(file='baixo2.wav')
b2raw_array_ = soundb2.get_raw()
soundb3=pygame.mixer.Sound(file='baixo3.wav')
b3raw_array_ = soundb3.get_raw()

baixo={"D??":b1raw_array_[6350000:6500000],
       "R??":b2raw_array_[6350000:6500000],
       "Mi":b3raw_array_[9350000:9500000],
       "Fa":b1raw_array_[9600000:9750000],
       "Sol":b2raw_array_[9600000:9750000],
       "La":b2raw_array_[4350000:4500000],
       "Si":b3raw_array_[6350000:6500000]}



#VIOL??O

soundv1=pygame.mixer.Sound(file='viola1.wav')
v1raw_array_ = soundv1.get_raw()
soundv2=pygame.mixer.Sound(file='viola2.wav')
v2raw_array_ = soundv2.get_raw()
soundv3=pygame.mixer.Sound(file='viola3.wav')
v3raw_array_ = soundv3.get_raw()

viola={"D??":v1raw_array_[6420000:6570000],
       "R??":v3raw_array_[6270000:6420000],
       "Mi":v2raw_array_[6250000:6400000],
       "Fa":v1raw_array_[9600000:9750000],
       "Sol":v3raw_array_[9400000:9550000],
       "La":v1raw_array_[13420000:13570000],
       "Si":v2raw_array_[13420000:13570000]}

# PIANO

soundp = pygame.mixer.Sound(file='escalamaior.wav')
praw_array_ = soundp.get_raw()
piano = {"D??":praw_array_[100000:250000],
         "R??":praw_array_[300000:450000],
         "Mi":praw_array_[450000:600000],
         "Fa":praw_array_[620000:770000],
         "Sol":praw_array_[800000:950000],
         "La":praw_array_[1000000:1150000],
         "Si":praw_array_[1150000:1300000]}



#Interface coding

#INSTRUMENTS
janela = tk.Tk()
janela.title("Projeto de Gridi")
janela.geometry("800x800")

escolha1 = tk.Label(janela, text="Escolha o instrumento:")
escolha1.place(x=20, y=5)

instrumento1 = tk.StringVar(value= data["instrumentos"]["box 1"])
campo_instrumento = tk.OptionMenu(janela, instrumento1, "(selecione)", "Viol??o", "Baixo", "Piano", "Bateria", "Trompete")

campo_instrumento.config(width=10)
campo_instrumento.place(x=20, y=55)

instrumento2 = tk.StringVar(value= data["instrumentos"]["box 2"])
campo_instrumento = tk.OptionMenu(janela, instrumento2, "(selecione)", "Viol??o", "Baixo", "Piano", "Bateria", "Trompete")

campo_instrumento.config(width=10)
campo_instrumento.place(x=20, y=105)

instrumento3 = tk.StringVar(value= data["instrumentos"]["box 3"])
campo_instrumento = tk.OptionMenu(janela, instrumento3, "(selecione)", "Viol??o", "Baixo", "Piano", "Bateria", "Trompete")

campo_instrumento.config(width=10)
campo_instrumento.place(x=20, y=155)

instrumento4 = tk.StringVar(value= data["instrumentos"]["box 4"])
campo_instrumento = tk.OptionMenu(janela, instrumento4, "(selecione)", "Viol??o", "Baixo", "Piano", "Bateria", "Trompete")

campo_instrumento.config(width=10)
campo_instrumento.place(x=20, y=205)

instrumento5 = tk.StringVar(value= data["instrumentos"]["box 5"])
campo_instrumento = tk.OptionMenu(janela, instrumento5, "(selecione)", "Viol??o", "Baixo", "Piano", "Bateria", "Trompete")

campo_instrumento.config(width=10)
campo_instrumento.place(x=20, y=255)

escolha2 = tk.Label(janela, text="Associe uma nota a cada cor!")
escolha2.place(x=300, y=5)


#COLORS AND TONES

#Vermelho

vermelho = tk.Label(janela, bg = "red", text="   ",)
vermelho.place(x=300, y=55)

nota = tk.StringVar(value= data["cores"]["Vermelho"])  
campo_nota = tk.OptionMenu(janela, nota, "(selecione)", "do", "re", "mi", "fa", "sol", "la", "si")
campo_nota.config(width=10)
campo_nota.place(x=350, y=55)

#Azul

azul = tk.Label(janela, bg = "blue", text="   ",)
azul.place(x=300, y=105)

nota2 = tk.StringVar(value= data["cores"]["Azul"])  
campo_nota2 = tk.OptionMenu(janela, nota2, "(selecione)", "do", "re", "mi", "fa", "sol", "la", "si")
campo_nota2.config(width=10)
campo_nota2.place(x=350, y=105)

#Roxo

roxo = tk.Label(janela, bg = "purple", text="   ",)
roxo.place(x=300, y=155)

nota3 = tk.StringVar(value= data["cores"]["Roxo"])  
campo_nota3 = tk.OptionMenu(janela, nota3, "(selecione)","do", "re", "mi", "fa", "sol", "la", "si")
campo_nota3.config(width=10)
campo_nota3.place(x=350, y=155)

#Verde

verde = tk.Label(janela, bg = "green", text="   ",)
verde.place(x=300, y=205)

nota4 = tk.StringVar(value= data["cores"]["Verde"])  
campo_nota4 = tk.OptionMenu(janela, nota4, "(selecione)", "do", "re", "mi", "fa", "sol", "la", "si")
campo_nota4.config(width=10)
campo_nota4.place(x=350, y=205)

#Amarelo

amarelo = tk.Label(janela, bg = "yellow", text="   ",)
amarelo.place(x=300, y=255)

nota5 = tk.StringVar(value= data["cores"]["Amarelo"])  
campo_nota5 = tk.OptionMenu(janela, nota5, "(selecione)", "do", "re", "mi", "fa", "sol", "la", "si")
campo_nota5.config(width=10)
campo_nota5.place(x=350, y=255)

#Rosa

rosa = tk.Label(janela, bg = "pink", text="   ")
rosa.place(x=300, y= 305)

nota6 = tk.StringVar(value= data["cores"]["Rosa"])  
campo_nota6 = tk.OptionMenu(janela, nota6, "(selecione)","do", "re", "mi", "fa", "sol", "la", "si")
campo_nota6.config(width=10)
campo_nota6.place(x=350, y=305)

#Preto

preto = tk.Label(janela, bg = "black", text="   ")
preto.place(x= 300, y= 355)

nota7 = tk.StringVar(value= data["cores"]["Preto"])  
campo_nota7 = tk.OptionMenu(janela, nota7, "(selecione)", "do", "re", "mi", "fa", "sol", "la", "si")
campo_nota7.config(width=10)
campo_nota7.place(x=350, y=355)

#LISTAS
instrumentos = [instrumento1, instrumento2, instrumento3, instrumento4, instrumento5]
notas = {"Vermelho": nota, "Azul": nota2, "Roxo": nota3, "Verde": nota4, "Amarelo": nota5, "Rosa": nota6, "Preto": nota7}
#notas = data[cores].get()

#Botoes Velocidade
def velocidadeatual(novovalor):
    global vel
    vel = float(novovalor)


global vel
vel = 0.2
velocidade = tk.DoubleVar(value = data["Velocidades"]["Velocidade"])
vel = velocidade.get()
scale = tk.Scale(janela, from_=0.2, to=1, resolution=0.2, command = velocidadeatual)
scale.place(x=550, y=80)
l1 = tk.Label(janela, text= "Velocidade:")
l1.place(x=550, y= 50)




#Desenho com matriz
'''
gridi = tk.Canvas(janela, bg="blue", height=600, width=200)
coord = 10, 50, 240, 210
oval = gridi.create_polygon(200, 600, 700, 600, 700, 900, 200, 900)
'''



#SAVING CHOSEN DATA

def salvar_dados():
    print("\n*** Escolhas selecionadas pelo usu??rio.***")
    print("Nota p/ vermelho:", nota.get())
    print("Nota p/ azul:", nota2.get())
    print("Nota p/ roxo:", nota3.get())
    print("Nota p/ verde:", nota4.get())
    print("Nota p/ amarelo:", nota5.get())
    print("Nota p/ rosa:", nota6.get())
    print("Nota p/ preto:", nota7.get())

    json_dados={

          "instrumentos": {
              "box 1": instrumento1.get(), "box 2" : instrumento2.get(), "box 3": instrumento3.get(), "box 4": instrumento4.get(), "box 5": instrumento5.get(),
          },
          "cores":
          {
              "Vermelho": nota.get(), "Azul": nota2.get(), "Roxo" : nota3.get(), "Verde": nota4.get(), "Amarelo": nota5.get(), "Rosa": nota6.get(),"Preto":nota7.get()
          },
          "Velocidades":
          {
              "Velocidade": vel#.get()
          }
    }

    with open("Dadosescolhidos.json", "w") as arquivo:
        json.dump(json_dados, arquivo) 

botao_dados = tk.Button(janela, text="Salvar Dados", command=salvar_dados)
botao_dados.place(x=550, y=205)

#GLOBAIS

global cont
cont=0

global timer
timer = None

global bpm
bpm= 0.35

global envio_sons_finais
envio_sons_finais = []


#Envio JSON

def escolhas_definidas():
    global envio_sons_finais
    envio_sons_finais=[]

    for i in range(0,len(matriz)):
        cores_na_linha = matriz[i]
        lista_de_notas = []

        for cor in cores_na_linha:
            if cor != None:
                lista_de_notas.append(notas[cor].get())
            else:
                lista_de_notas.append(None)


        dicionario = {
            "instrumento": instrumentos[i].get(),
            "notas": lista_de_notas
        }

        envio_sons_finais.append(dicionario)

    print(envio_sons_finais)
    return 


#Botao Envio

botao_escolhas = tk.Button(janela, text="Enviar dados", command=escolhas_definidas)
botao_escolhas.place(x=550, y=260)

s_biblioteca={"Trompete":trompete,"Bateria":drums,"Baixo":baixo,"Viol??o":viola,"Piano":piano}


#PLAY
def play():
    global envio_sons_finais
    global cont

    if cont >= 8:
        cont=0

    for i in range(len(envio_sons_finais)):
        dicionario=envio_sons_finais[i]

        if dicionario["instrumento"] != "(selecione)":

            s_som=s_biblioteca[dicionario["instrumento"]]
            if dicionario["notas"][cont]:

                recurso_de_nota=s_som[dicionario["notas"][cont]]

                if isinstance(recurso_de_nota,pygame.mixer.Sound) == True:
                    toca_inst=s_som[dicionario["notas"][cont]]
                    toca_inst.play()
                else:
                    nota=s_som[dicionario["notas"][cont]]
                    toca_inst=pygame.mixer.Sound(buffer=nota)
                    toca_inst.play()
    cont+=1

    global timer 
    timer= Timer(vel, play)
    timer.start()



# Carolina converteu a matriz de cores para uma estrura como essa abaixo

# [
#     {'instrumento': 'Piano', 'notas': ['D??', None, 'F??', None, None, None, None, None]},
#     {'instrumento': '(selecione)', 'notas': [None, 'Si', None, None, None, None, None, None]},
#     {'instrumento': 'Baixo', 'notas': [None, None, 'R??', None, None, None, None, None]},
#     {'instrumento': '(selecione)', 'notas': [None, None, None, '(selecione)', None, None, None, None]},
#     {'instrumento': '(selecione)', 'notas': ['F??', '(selecione)', None, None, None, None, None, None]}
# ]

#Botao Play
botaoplay = tk.Button(janela, text="PLAY", command= play)
botaoplay.place(x=640, y=305)


#STOP


def stop():
    global timer
    if timer != None:
        timer.cancel()
        timer=None

# Botao Pausa
botaostop = tk.Button(janela, text="STOP", command= stop)
botaostop.place(x=560, y=305)

# #Execu????o
# cores_detectadas = [
#     ["Vermelho",None,"Azul",None,None,None,None,None],
#     [None,"Vermelho",None,None,None,None,None,None],
#     [None,None,"Vermelho",None,None,None,None,None],
#     [None,None,None,"Vermelho",None,None,None,None],
#     ["Vermelho","Vermelho",None,None,None,None,None,None],
# ]


# Canvas
grade = tk.Label(janela, text="Grade Virtual:")
grade.place(x=20, y=480)

myCanvas = tk.Canvas(janela, bg="white", height=500, width=500)

myCanvas.place(x=20, y=500)

def carol():
    print("carol")
    for i in range(len(matriz)):
        for j in range(len(matriz[0])):
            x = j * 30 + 30
            y = i * 30 +30
            if matriz[i][j] == "Vermelho":
                cor = "red"
            elif matriz[i][j] == "Verde":
                cor = "green"
            elif matriz[i][j] == "Azul":
                cor = "blue"
            elif matriz[i][j] == "Roxo":
                cor = "purple"
            elif matriz[i][j] == "Laranja":
                cor = "orange"
            elif matriz[i][j] == "Rosa":
                cor = "pink"
            elif matriz[i][j] == "Preto":
                cor = "black"
            elif matriz[i][j] == None:
                cor = "white"


            myCanvas.create_oval(x,y,x+10,y+10, fill = cor)
            
    janela.after(100, carol)

carol()

'''
myCanvas = tk.Canvas(janela, bg="white", height=100, width=100)
coord = 20, 20, 50, 50
bola = myCanvas.create_oval(coord, start=0, extent=359, fill="pink")

myCanvas.place(x=20, y=500)
janela.mainloop()
'''
