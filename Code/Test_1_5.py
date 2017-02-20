from math import pi

def S(n):
    sum=0
    for i in range(n):
        k=i+1
        sum=sum+(-1)**k/(k*k*(k+2)**2)
    return sum

print(5/16-pi**2/24)



