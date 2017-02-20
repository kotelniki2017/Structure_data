def y(x):
    return x**4+10*x**3-3*x-5

L=[]
h=0.2
x=0
mmin=y(x)
print("Шаг равен ",h)
while x<1:
    L.append(y(x))
    print(L[-1])
    if mmin>L[-1]:
        mmin=L[-1]
    x=x+h
print("Минимальный элемент равен ",mmin)
A=[]
h=0.1
x=0
mmin=y(x)
print("Шаг равен ",h)
while x<1:
    A.append(y(x))
    print(A[-1])
    if mmin>A[-1]:
        mmin=A[-1]
    x=x+h
print("Минимальный элемент равен ",mmin)
