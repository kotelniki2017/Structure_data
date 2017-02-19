import random

#Функция генерирует случайный список
def genlist(n):
    L=[]
    for i in range(n):
        L.append(random.randint(-10,10))
    return L

#Функция считает количество отрицательных элементов
def count_minus(A):
    result=0
    for i in A:
        if i<0:
            result+=1
    return result

def revlist(A):
    for i in range(len(A)//2):
        A[i],A[len(A)-i-1]=A[len(A)-i-1],A[i]

n=int(input("Введите длину списка:"))
L=genlist(n)
print(L)
print(count_m(L))






