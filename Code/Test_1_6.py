def mmin(L):
    result=L[0]
    for i in L:
        if result > i:
           result=i
    return result

def mmax(L):
    result=L[0]
    for i in L:
        if result < i:
           result=i
    return result

def mean(L):
    s=0
    for i in L:
        s+=i
    if len(L)!=0:
        return s/len(L)
    else:
        return 0

def iter(L):
    amin=mmin(L)
    amax=mmax(L)
    amean=mean(L)

    for i in range(len(L)):
        L[i]=(L[i]-amin)*(amax-amean)
    return L    

def main(L,n):
    for i in range(n):
        iter(L)
    return L


