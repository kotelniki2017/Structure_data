import math
print("Решение квадратного уравнения ax^2+bx+c=0")
a=int(input("a="))
b=int(input("b="))
c=int(input("c="))
D=b**2-4*a*c
if D>0:
    x1=(-b+math.sqrt(b**2-4*a*c))/(2*a)
    x2=(-b-math.sqrt(b**2-4*a*c))/(2*a)
    print("x1=",x1,"x2=",x2)
elif D==0:
    x1=-b/(2*a)
    print("x1=x2=",x1)
else:
    x1=(-b+(b**2-4*a*c)**0.5)/(2*a)
    x2=(-b-(b**2-4*a*c)**0.5)/(2*a)
    print("Получены комплексные корни")
    print("x1=",x1,"x2=",x2)






