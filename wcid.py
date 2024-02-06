from math import sqrt
def Privet():
    return "What am I doing in MechMat?"
def Poka():
    return "2+2=integral"
def diffr_vector(v1,v2):
    n=len(v1)
    V=[]
    for i in range(n):
        V[i]=v1[i]-v2[i]
    return V
def norma(v):
    normalno=0
    for i in range(len(v)):
        normalno+=i**2
    normalno=sqrt(normalno)
    return normalno
def norma2(v):
    return max(v)