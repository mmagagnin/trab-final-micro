from re import X
from serial import Serial
from threading import Thread, Timer

meu_serial = Serial("/dev/serial0", baudrate=9600)

matriz=[[11,12,13,14,15,16,17,18],
        [21,22,23,24,25,26,27,28],
        [31,32,33,34,35,36,37,38],
        [41,42,43,44,45,46,47,48],
        [51,52,53,54,55,56,57,58],
        ]

matrizTeste=[["vermelho",None,None,None,None,None,None,None],
            [None,"azul",None,None,None,None,None,None],
            [None,None,"verde",None,None,None,None,None],
            [None,None,None,None,"preto",None,None,None],
            [None,None,None,None,None,None,"laranja",None],
            ]

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

mInv=matrizInv(matrizTeste)
mLuzes=matrizLuzes(mInv)
envio=criaString(mLuzes)

print(envio)
meu_serial.write(envio.encode("UTF-8"))

