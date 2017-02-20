def digit(a,n):
    return int(a/(10**(n-1)))%10

def list_digit(a):
    L=[]
    for i in range(len(str(a))):
        L.append(digit(a,(i+1)))
    return L

def sum_list(L):
    result=0
    for i in L:
        result+=i
    return result

def sum_digit(a):
    r=a
    while (len(str(r))!=1):
        r=sum_list(list_digit(r))
    return r
def analog(a):
    if a%9!=0:
        return a%9
    else:
        return 9
