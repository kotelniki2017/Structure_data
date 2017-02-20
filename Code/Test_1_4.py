from random import randint as rand

N=1000000
m=0
for i in range(N):
    a=rand(1,6)
    b=rand(1,6)
    if (a+b)>7:
        m+=1
print("Искомая вероятность равна ",m/N)


