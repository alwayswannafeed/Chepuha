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