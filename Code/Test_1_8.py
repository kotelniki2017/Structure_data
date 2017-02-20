def get_positive(L):
    result=[]
    for i in L:
        if i>0:
            result.append(i)
    return result

def get_negative(L):
    result=[]
    for i in L:
        if i<0:
            result.append(i)
    return result

def get_zero(L):
    result=[]
    for i in L:
        if i==0:
            result.append(i)
    return result

def main(L):
    return get_negative(L)+get_positive(L)+get_zero(L)
