def insert_sort(lst):
    compare = 0; permulation = 0
    for i in range(1,len(lst)):
        j=0
        compare += 1
        while (lst[j]<lst[i]) & (j<i):
            j  += 1
            compare += 1
        if (lst[j]>=lst[i]) & (j<i):
            lst=lst[0:j]+[lst[i]]+[lst[j]]+lst[(j+1):i]+lst[(i+1):len(lst)]
            permulation += 1
        #print(lst)
    return [compare,permulation]

def shaker_sort(lst):
    compare = 0; permulation = 0; pr = True; i = 0
    while pr & (i<(len(lst)//2)):
        pr=False
        for j in range(len(lst)-i-1):
            compare += 1
            if lst[j]>=lst[j+1]:
                lst[j],lst[j+1]=lst[j+1],lst[j]
                permulation += 1; pr = True
            #print(lst)
        for j in range(len(lst)-i-3):
            compare += 1
            if lst[len(lst)-i-2-j]<=lst[len(lst)-i-3-j]:
                lst[len(lst)-i-2-j],lst[len(lst)-i-3-j]=lst[len(lst)-i-3-j],lst[len(lst)-i-2-j]
                permulation += 1; pr = True
            #print(lst)
        i += 1
    return [compare,permulation]

def bubble_best_sort(lst):
    compare = 0; permulation = 0; pr = True; i = 0
    while pr & (i<len(lst)):
        pr=False
        for j in range(len(lst)-i-1):
            compare += 1
            if lst[j]>=lst[j+1]:
                lst[j],lst[j+1]=lst[j+1],lst[j]
                permulation += 1; pr = True
            #print(lst)
        i += 1
    return [compare,permulation]


compare = 0; permutation = 0
def quick_sort(lst):
    global compare,permutation
    if lst==[]:
        return []
    else:
        s1=[]
        s2=[]
        a=lst[0]
        for i in range(1,len(lst)):
            compare += 1	
            if lst[i]<a:
                s1=s1+[lst[i]]
            else:
                s2=s2+[lst[i]]
        permutation += 1
        #print(s1+[a]+s2)
        return quick_sort(s1)+[a]+quick_sort(s2)

def select_sort(lst):
    compare = 0; permulation = 0
    for i in range(len(lst)):
        min=lst[i]
        index=i
        for j in range(i+1,len(lst)):
            compare += 1
            if min>lst[j]:
                min=lst[j]
                index=j
        if index != i:        
            a=lst[i]
            lst[i]=lst[index]
            lst[index]=a
            permulation += 1
        #print(lst)
    return [compare,permulation]

import random
def gen(n):
    return random.sample(range(2*n ),n)

compare=0
permutation=0
def test(A,N):
    compare_insert=0;
    compare_shaker=0;
    compare_bubble=0;
    compare_select=0;
    
    permulation_insert=0;
    permulation_shaker=0;
    permulation_bubble=0;
    permulation_select=0;
    
    for i in range(A):
        print('испытание №',i)
        lst=gen(N);
        r=list(lst);
        w=insert_sort(r);
        compare_insert+=w[0]
        permulation_insert+=w[1]
        r=list(lst)
        w=shaker_sort(r);
        compare_shaker+=w[0];
        permulation_shaker+=w[1];
        r=list(lst)
        w=bubble_best_sort(r);
        compare_bubble+=w[0];
        permulation_bubble+=w[1];
        r=list(lst)
        w=select_sort(r);
        compare_select+=w[0];
        permulation_select+=w[1];
        r=list(lst)
        quick_sort(r);
        
    print('Вставка',[compare_insert/A,permulation_insert/A])
    print('Шейкер',[compare_shaker/A,permulation_shaker/A])
    print('Улучшенный пузырек',[compare_bubble/A,permulation_bubble/A])
    print('Выбор',[compare_select/A,permulation_select/A])
    print('Быстрая',[compare/A,permutation/A])













