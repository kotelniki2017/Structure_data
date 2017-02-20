def fact(m):
    r=1
    for i in range(m):
        r=r*(i+1)
    return r

def C(k,n):
    if isinstance(k,int)&isinstance(n,int):
        return int(fact(n)/(fact(k)*fact(n-k)))
    else:
        return "Error"


