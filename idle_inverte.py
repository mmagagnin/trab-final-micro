matriz=[[11,12,13,14,15,16,17,18],
        [21,22,23,24,25,26,27,28],
        [31,32,33,34,35,36,37,38],
        [41,42,43,44,45,46,47,48],
        [51,52,53,54,55,56,57,58],
        ]

def matrizInv(m):
    mInv=[]
    i=0
    j=0
    while j<8:
        mInv.append([])
        while i<5:
            mInv[j].append(i)
            i+=1
        i=0
        j+=1
    return mInv

print(matrizInv(matriz))
