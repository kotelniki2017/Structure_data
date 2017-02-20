def y(x,epsilon):
    if x>1:
        s=0
        n=0
        while (1/x**n>epsilon):
            s=s+1/x**n
            n+=1
        return s
    else:
        return "Error"


