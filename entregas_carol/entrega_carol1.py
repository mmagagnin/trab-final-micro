#BIBLIOTECAS
import tkinter as tk
import json
import pygame
from pygame import mixer
from threading import Timer

#Abrindo o json

with open("Dadosescolhidos.json", "r") as arquivo:
    data = json.load(arquivo)
    #print(data)
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

trompete={"Dó":tdo,"Ré":tre,"Mi":tmi,"Fa":tfa,"Sol":tsol,"La":tla,"Si":tsi}

#DRUMS

snare=pygame.mixer.Sound(file='snare.wav')
kick=pygame.mixer.Sound(file='kick.wav')
hihat=pygame.mixer.Sound(file='hi-hat.wav')
clap=pygame.mixer.Sound(file='clap.wav')
sino=pygame.mixer.Sound(file='sino.wav')
moresnare=pygame.mixer.Sound(file='moresnare.wav')
triangulo=moresnare=pygame.mixer.Sound(file='triangulo.wav')

drums={"Dó":snare,"Ré":kick,"Mi":hihat,"Fá":clap,"Sol":sino,"La":moresnare,"Si":triangulo}

#BAIXO

soundb1=pygame.mixer.Sound(file='baixo1.wav')
b1raw_array_ = soundb1.get_raw()
soundb2=pygame.mixer.Sound(file='baixo2.wav')
b2raw_array_ = soundb2.get_raw()
soundb3=pygame.mixer.Sound(file='baixo3.wav')
b3raw_array_ = soundb3.get_raw()

baixo={"Dó":b1raw_array_[6350000:6500000],"Ré":b2raw_array_[6350000:6500000],"Mi":b3raw_array_[9350000:9500000],"Fa":b1raw_array_[9600000:9750000],"Sol":b2raw_array_[9600000:9750000],"La":b2raw_array_[4350000:4500000],"Si":b3raw_array_[6350000:6500000]}



#VIOLÃO

soundv1=pygame.mixer.Sound(file='viola1.wav')
v1raw_array_ = soundv1.get_raw()
soundv2=pygame.mixer.Sound(file='viola2.wav')
v2raw_array_ = soundv2.get_raw()
soundv3=pygame.mixer.Sound(file='viola3.wav')
v3raw_array_ = soundv3.get_raw()

viola={"Dó":v1raw_array_[6420000:6570000],"Ré":v3raw_array_[6270000:6420000],"Mi":v2raw_array_[6250000:6400000],"Fa":v1raw_array_[9600000:9750000],"Sol":v3raw_array_[9400000:9550000],"La":v1raw_array_[13420000:13570000],"Si":v2raw_array_[13420000:13570000]}

# PIANO

soundp = pygame.mixer.Sound(file='escalamaior.wav')
praw_array_ = soundp.get_raw()
global piano
piano = {"Dó":praw_array_[100000:250000],"Ré":praw_array_[300000:450000],"Mi":praw_array_[450000:600000],"Fa":praw_array_[620000:770000],"Sol":praw_array_[800000:950000],"La":praw_array_[1000000:1150000],"Si":praw_array_[1150000:1300000]}



#Interface coding

#INSTRUMENTS
janela = tk.Tk()
janela.title("Projeto de Gridi")
janela.geometry("800x800")

escolha1 = tk.Label(janela, text="Escolha o instrumento:")
escolha1.place(x=20, y=5)

instrumento1 = tk.StringVar(value= data["instrumentos"]["box 1"])
campo_instrumento = tk.OptionMenu(janela, instrumento1, "(selecione)", "Violão", "Baixo", "Piano", "Bateria", "Trompete")

campo_instrumento.config(width=10)
campo_instrumento.place(x=20, y=55)

instrumento2 = tk.StringVar(value= data["instrumentos"]["box 2"])
campo_instrumento = tk.OptionMenu(janela, instrumento2, "(selecione)", "Violão", "Baixo", "Piano", "Bateria", "Trompete")

campo_instrumento.config(width=10)
campo_instrumento.place(x=20, y=105)

instrumento3 = tk.StringVar(value= data["instrumentos"]["box 3"])
campo_instrumento = tk.OptionMenu(janela, instrumento3, "(selecione)", "Violão", "Baixo", "Piano", "Bateria", "Trompete")

campo_instrumento.config(width=10)
campo_instrumento.place(x=20, y=155)

instrumento4 = tk.StringVar(value= data["instrumentos"]["box 4"])
campo_instrumento = tk.OptionMenu(janela, instrumento4, "(selecione)", "Violão", "Baixo", "Piano", "Bateria", "Trompete")

campo_instrumento.config(width=10)
campo_instrumento.place(x=20, y=205)

instrumento5 = tk.StringVar(value= data["instrumentos"]["box 5"])
campo_instrumento = tk.OptionMenu(janela, instrumento5, "(selecione)", "Violão", "Baixo", "Piano", "Bateria", "Trompete")

campo_instrumento.config(width=10)
campo_instrumento.place(x=20, y=255)

escolha2 = tk.Label(janela, text="Associe uma nota a cada cor!")
escolha2.place(x=300, y=5)


#COLORS AND TONES

#Vermelho

vermelho = tk.Label(janela, bg = "red", text="   ",)
vermelho.place(x=300, y=55)

nota = tk.StringVar(value= data["cores"]["Vermelho"])  
campo_nota = tk.OptionMenu(janela, nota, "(selecione)", "Dó", "Ré", "Mi", "Fa", "Sol", "La", "Si")
campo_nota.config(width=10)
campo_nota.place(x=350, y=55)

#Azul

azul = tk.Label(janela, bg = "blue", text="   ",)
azul.place(x=300, y=105)

nota2 = tk.StringVar(value= data["cores"]["Azul"])  
campo_nota2 = tk.OptionMenu(janela, nota2, "(selecione)", "Dó", "Ré", "Mi", "Fa", "Sol", "La", "Si")
campo_nota2.config(width=10)
campo_nota2.place(x=350, y=105)

#Roxo

roxo = tk.Label(janela, bg = "purple", text="   ",)
roxo.place(x=300, y=155)

nota3 = tk.StringVar(value= data["cores"]["Roxo"])  
campo_nota3 = tk.OptionMenu(janela, nota3, "(selecione)", "Dó", "Ré", "Mi", "Fa", "Sol", "La", "Si")
campo_nota3.config(width=10)
campo_nota3.place(x=350, y=155)

#Verde

verde = tk.Label(janela, bg = "green", text="   ",)
verde.place(x=300, y=205)

nota4 = tk.StringVar(value= data["cores"]["Verde"])  
campo_nota4 = tk.OptionMenu(janela, nota4, "(selecione)", "Dó", "Ré", "Mi", "Fa", "Sol", "La", "Si")
campo_nota4.config(width=10)
campo_nota4.place(x=350, y=205)

#Amarelo

amarelo = tk.Label(janela, bg = "yellow", text="   ",)
amarelo.place(x=300, y=255)

nota5 = tk.StringVar(value= data["cores"]["Amarelo"])  
campo_nota5 = tk.OptionMenu(janela, nota5, "(selecione)", "Dó", "Ré", "Mi", "Fa", "Sol", "La", "Si")
campo_nota5.config(width=10)
campo_nota5.place(x=350, y=255)

#Rosa

rosa = tk.Label(janela, bg = "pink", text="   ")
rosa.place(x=300, y= 305)

nota6 = tk.StringVar(value= data["cores"]["Rosa"])  
campo_nota6 = tk.OptionMenu(janela, nota6, "(selecione)", "Dó", "Ré", "Mi", "Fa", "Sol", "La", "Si")
campo_nota6.config(width=10)
campo_nota6.place(x=350, y=305)

#Laranja

# laranja = tk.Label(janela, bg = "orange", text="   ")
# laranja.place(x= 300, y= 355)
# 
# nota7 = tk.StringVar(value= data["cores"]["Laranja"])  
# campo_nota7 = tk.OptionMenu(janela, nota7, "(selecione)", "Dó", "Ré", "Mi", "Fa", "Sol", "La", "Si")
# campo_nota7.config(width=10)
# campo_nota7.place(x=350, y=355)

#LISTAS
instrumentos = [instrumento1, instrumento2, instrumento3, instrumento4, instrumento5]
#notas = {"Vermelho": nota, "Azul": nota2, "Roxo": nota3, "Verde": nota4, "Preto": nota5, "Rosa": nota6, "Laranja": nota7}
notas = data[cores]

#Botoes Velocidade

velocidade_maxima = tk.Label(janela, text="Velocidade Máxima")
velocidade_maxima.place(x=547, y=60)

vemax = tk.IntVar() 
campovmax = tk.Spinbox(janela, width=6, textvariable=vemax, from_= data["Velocidades"]["Velocidade maxima"], to=10)
campovmax.place(x=550, y=80)

velocidade_minima = tk.Label(janela, text="Velocidade Mínima")
velocidade_minima.place(x=547, y=110)

vemin = tk.IntVar() 
campovmin= tk.Spinbox(janela, width=6, textvariable=vemin, from_= data["Velocidades"]["Velocidade minima"], to=10)
campovmin.place(x=550, y=130)

#SAVING CHOSEN DATA

def salvar_dados():
  print("\n*** Escolhas selecionadas pelo usuário.***")
  print("Nota p/ vermelho:", nota.get())
  print("Nota p/ azul:", nota2.get())
  print("Nota p/ roxo:", nota3.get())
  print("Nota p/ verde:", nota4.get())
  print("Nota p/ preto:", nota5.get())
  print("Nota p/ rosa:", nota6.get())
  print("Nota p/ laranja:", nota7.get())
  
  json_dados={
      
          "instrumentos": {
              "box 1": instrumento1.get(), "box 2" : instrumento2.get(), "box 3": instrumento3.get(), "box 4": instrumento4.get(), "box 5": instrumento5.get(),
          },
          "cores":
          {
              "Vermelho": nota.get(), "Azul": nota2.get(), "Roxo" : nota3.get(), "Verde": nota4.get(), "Preto": nota5.get(), "Rosa": nota6.get(),"Laranja":nota7.get()
          },
          "Velocidades":
          {
              "Velocidade maxima": vemax.get(), "Velocidade minima": vemin.get()
          }
    }
  
  with open("Dadosescolhidos.json", "w") as arquivo:
     json.dump(json_dados, arquivo)
  

botao_dados = tk.Button(janela, text="Salvar Dados", command=salvar_dados)
botao_dados.place(x=550, y=205)


cores_detectadas = [
    ["vermelho",None,"azul",None,None,None,None,None],
    [None,"vermelho",None,None,None,None,None,None],
    [None,None,"vermelho",None,None,None,None,None],
    [None,None,None,"vermelho",None,None,None,None],
    ["vermelho","vermelho",None,None,None,None,None,None],
]

#Envio JSON

def escolhas_definidas():
    lista = []
    for i in range(0,len(cores_detectadas)):
        cores_na_linha = cores_detectadas[i]
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
        
        lista.append(dicionario)
    
    print(lista)
    return escolhas_definidas


#Botao Envio

botao_escolhas = tk.Button(janela, text="Botão 1", command=escolhas_definidas)
botao_escolhas.place(x=550, y=260)

s_biblioteca={"Trompete":trompete,"Bateria":drums,"Baixo":baixo,"Viol\u00e3o":viola,"Piano":piano}
#PLAY
def play():
    
    global cont
    
    for i in range(len(lista)-1):
        dicionario=lista[i]
        s_som=s_biblioteca[lista[instrumento]]
        if isinstance(s_som[dicionario[notas]],pygame.mixer.Sound) == True:
            toca_inst=s_som[dicionario[notas]]
            toca_inst.play()
        else:
            nota=s_som[dicionario[notas]]
            
    cont+=1
    
    global timer
    global bpm
    timer= Timer(bpm, play)
    timer.start()
    
    #if cont >= 8:
        #parar_timer()
        #cont=0

# Carolina converteu a matriz de cores para uma estrura como essa abaixo

# [
#     {'instrumento': 'Piano', 'notas': ['Dó', None, 'Fá', None, None, None, None, None]},
#     {'instrumento': '(selecione)', 'notas': [None, 'Si', None, None, None, None, None, None]},
#     {'instrumento': 'Baixo', 'notas': [None, None, 'Ré', None, None, None, None, None]},
#     {'instrumento': '(selecione)', 'notas': [None, None, None, '(selecione)', None, None, None, None]},
#     {'instrumento': '(selecione)', 'notas': ['Fá', '(selecione)', None, None, None, None, None, None]}
# ]

#Botao Play
botaoplay = tk.Button(janela, text="PLAY", command= play)
botaoplay.place(x=200, y=500)

# coord=[
#     ["vermelho",None,None,None],
#     [None,"vermelho",None,None],
#     [None,None,"vermelho",None],
#     [None,None,None,"vermelho"],
#     ["vermelho","vermelho",None,None],
#     [None,None,None,"vermelho"],
#     [None,None,None,None],
#     ["vermelho","vermelho","vermelho","vermelho"]
# ]

#STOP
global timer
timer = None

global bpm
bpm= 0.35

global cont
cont=0

def stop():
    global timer
    if timer != None:
        timer.cancel()
        timer=None

# Botao Pausa
botaostop = tk.Button(janela, text="STOP", command= stop)
botaostop.place(x=500, y=500)
