import pygame
from pygame import mixer
import tkinter as tk
from threading import Timer

#MIXER

pygame.mixer.init(44100,-16,3,10)
pygame.mixer.set_num_channels(32)

#TROMPETE

tdo=pygame.mixer.Sound(file='trom_Do.wav')
tre=pygame.mixer.Sound(file='trom_Re.wav')
tmi=pygame.mixer.Sound(file='trom_Mi.wav')
tfa=pygame.mixer.Sound(file='trom_Fa.wav')
tsol=pygame.mixer.Sound(file='trom_Sol.wav')
tla=pygame.mixer.Sound(file='trom_La.wav')
tsi=pygame.mixer.Sound(file='trom_Si.wav')

trompete={"do":tdo,"re":tre,"mi":tmi,"fa":tfa,"sol":tsol,"la":tla,"si":tsi}
#DRUMS

snare=pygame.mixer.Sound(file='snare.wav')
kick=pygame.mixer.Sound(file='kick.wav')
hihat=pygame.mixer.Sound(file='hi-hat.wav')
clap=pygame.mixer.Sound(file='clap.wav')
sino=pygame.mixer.Sound(file='sino.wav')
moresnare=pygame.mixer.Sound(file='moresnare.wav')
triangulo=moresnare=pygame.mixer.Sound(file='triangulo.wav')

drums={"do":snare,"re":kick,"mi":hihat,"fa":clap,"sol":sino,"la":moresnare,"si":triangulo}

#BAIXO

soundb1=pygame.mixer.Sound(file='baixo1.wav')
b1raw_array_ = soundb1.get_raw()
soundb2=pygame.mixer.Sound(file='baixo2.wav')
b2raw_array_ = soundb2.get_raw()
soundb3=pygame.mixer.Sound(file='baixo3.wav')
b3raw_array_ = soundb3.get_raw()

baixo={"do":b1raw_array_[6350000:6500000],"re":b2raw_array_[6350000:6500000],"mi":b3raw_array_[9350000:9500000],"fa":b1raw_array_[9600000:9750000],"sol":b2raw_array_[9600000:9750000],"la":b2raw_array_[4350000:4500000],"si":b3raw_array_[6350000:6500000]}



#VIOLÃO

soundv1=pygame.mixer.Sound(file='viola1.wav')
v1raw_array_ = soundv1.get_raw()
soundv2=pygame.mixer.Sound(file='viola2.wav')
v2raw_array_ = soundv2.get_raw()
soundv3=pygame.mixer.Sound(file='viola3.wav')
v3raw_array_ = soundv3.get_raw()

viola={"do":v1raw_array_[6420000:6570000],"re":v3raw_array_[6270000:6420000],"mi":v2raw_array_[6250000:6400000],"fa":v1raw_array_[9600000:9750000],"sol":v3raw_array_[9400000:9550000],"la":v1raw_array_[13420000:13570000],"si":v2raw_array_[13420000:13570000]}

# PIANO

soundp = pygame.mixer.Sound(file='escalamaior.wav')
praw_array_ = soundp.get_raw()
global piano
piano = {"do":praw_array_[100000:250000],"re":praw_array_[300000:450000],"mi":praw_array_[450000:600000],"fa":praw_array_[620000:770000],"sol":praw_array_[800000:950000],"la":praw_array_[1000000:1150000],"si":praw_array_[1150000:1300000]}

#funções
def ptoca_nota_do():
    global piano
    nota= piano["do"]
    cut_sound_ = pygame.mixer.Sound(buffer=nota)
    cut_sound_.play()
    
def ptoca_nota_re():
    global piano
    nota= piano["re"]
    cut_sound_ = pygame.mixer.Sound(buffer=nota)
    cut_sound_.play()

def ptoca_nota_mi():
    global piano
    nota= piano["mi"]
    cut_sound_ = pygame.mixer.Sound(buffer=nota)
    cut_sound_.play()
    
def ptoca_nota_fa():
    global piano
    nota= piano["fa"]
    cut_sound_ = pygame.mixer.Sound(buffer=nota)
    cut_sound_.play()
    
def ptoca_nota_sol():
    global piano
    nota= piano["sol"]
    cut_sound_ = pygame.mixer.Sound(buffer=nota)
    cut_sound_.play()
    
def ptoca_nota_la():
    global piano
    nota= piano["la"]
    cut_sound_ = pygame.mixer.Sound(buffer=nota)
    cut_sound_.play()
    
def ptoca_nota_si():
    global piano
    nota= piano["si"]
    cut_sound_ = pygame.mixer.Sound(buffer=nota)
    cut_sound_.play()
    
#BOTÕES
janela = tk.Tk()
janela.geometry("850x1050")

tecla_do = tk.Button(janela, text="Do",width=5,height=5,command=ptoca_nota_do)
tecla_do.place(x=30, y=10)

tecla_do = tk.Button(janela, text="Re",width=5,height=5,command=ptoca_nota_re)
tecla_do.place(x=80, y=10)

tecla_do = tk.Button(janela, text="Mi",width=5,height=5,command=ptoca_nota_mi)
tecla_do.place(x=130, y=10)

tecla_do = tk.Button(janela, text="Fa",width=5,height=5,command=ptoca_nota_fa)
tecla_do.place(x=180, y=10)

tecla_do = tk.Button(janela, text="Sol",width=5,height=5,command=ptoca_nota_sol)
tecla_do.place(x=230, y=10)

tecla_do = tk.Button(janela, text="La",width=5,height=5,command=ptoca_nota_la)
tecla_do.place(x=280, y=10)

tecla_do = tk.Button(janela, text="Si",width=5,height=5,command=ptoca_nota_si)
tecla_do.place(x=330, y=10)

# DICIONÁRIOS

coord=[["vermelho",None,None,None],[None,"vermelho",None,None],[None,None,"vermelho",None],[None,None,None,"vermelho"],["vermelho","vermelho",None,None],[None,None,None,"vermelho"],[None,None,None,None],["vermelho","vermelho","vermelho","vermelho"]]
cores={"vermelho":"do","laranja":"re","amarelo":"mi","verde":"fa","azul":"sol","roxo":"la","rosa":"si"}
instrumento=[drums,baixo,viola,piano]


#TIMER

global timer
timer = None

global bpm
bpm= 0.35

global cont
cont=0

def ler_coords():
    
    global cont

    lista=coord[cont]
    
    for i in range(len(coord[cont])):
        lista=coord[cont]
        if lista[i-1] != None:
            if lista[i-1] == "vermelho":
                if i != 1:
                    toca_instrumento=instrumento[i-1]
                    nota=toca_instrumento["do"]
                    cut_sound_ = pygame.mixer.Sound(buffer=nota)
                    cut_sound_.play()
                else:
                    drums["do"].play()
    cont+=1
    
    global timer
    global bpm
    timer= Timer(bpm, ler_coords)
    timer.start()
    
    if cont >= 8:
        parar_timer()
        cont=0

    
def parar_timer():
    global timer
    if timer != None:
        timer.cancel()
        timer=None
#TESTE

'''nota1= viola["do"]
cut_sound_1 = pygame.mixer.Sound(buffer=nota1)
cut_sound_1.play()   
nota2= viola["mi"]
cut_sound_2 = pygame.mixer.Sound(buffer=nota2)
cut_sound_2.play()  
nota3= piano["si"]
cut_sound_3 = pygame.mixer.Sound(buffer=nota3)
cut_sound_3.play()'''


    
        
        

    