
def vInicialDic(matriz):
    lDic=[]
    i=0
    for linha in matriz:
        lDic.append([])
        for posicao in linha:
            lDic[i].append({"corAntiga":None,"corAtual":None,"contagem":1})
        i+=1
    return lDic

def atualizaContagemDic(d):
    if d["corAntiga"]==d["corAtual"]:
        d["contagem"]+=1
        if d["contagem"]==5:
            return True
    else:
        d["corAntiga"]=d["corAtual"]
        d["contagem"]=1

def atualizaLdeDic(matrizNova,lD):
    linha=0
    for row in matrizNova:
        coluna=0
        for bolinha in row:
            lD[linha][coluna]["corAtual"]=matrizNova[linha][coluna]
            if atualizaContagemDic(lD[linha][coluna]):
                #determinadas outras operacoes
            coluna+=1
        linha+=1

matriz=[[None,None,None,None,None,None,None,None],
            [None,None,None,None,None,None,None,None],
            [None,None,None,None,None,None,None,None],
            [None,None,None,None,None,None,None,None],
            [None,None,None,None,None,None,None,None],
            ]

dicInicial=vInicialDic(matriz)
print(dicInicial)

matrizNova=[['vermelho',None,None,None,None,None,None,None],
            [None,None,None,None,None,None,None,None],
            [None,None,None,None,None,None,None,None],
            [None,None,None,None,None,None,None,None],
            [None,None,None,None,None,None,None,None],
            ]

atualizaLdeDic(matrizNova,dicInicial)

print(dicInicial)









            
