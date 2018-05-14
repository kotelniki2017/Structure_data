#random.seed
import random

class Hashtable:
    __size=None
    __table=None
    __counter=0

    def __init__(self,n):
      self.__size=n
      self.__table=[]
      for i in range(n):
          self.__table.append(None)

    def hashf(self,s):
        if type(s)!=str:
            s=str(s)
        H=0
        for i in s:
            H=(H<<4)+ord(i)
        G=H&0xF0000000
        if G!= 0:
            H=(H^(G>>24))^G
        return H%self.__size
        

    def get_table(self):
        return self.__table

    def get_size(self):
        return self.__size
    
    def get_counter(self):
        return self.__counter
    
    def add(self,x):
        if self.__counter==self.__size:
            return 'Overflow'
        self.__counter+=1
        y=self.hashf(x)
        random.seed(y)
        r=random.randint(0, self.__size-1)
        if self.__table[r]==None:
            self.__table[r]=x
        else:
            r=random.randint(0, self.__size-1)
            while (self.__table[r]!=None):
                r=random.randint(0, self.__size-1)
            self.__table[r]=x
                
        
    def find(self,x):
        if self.__counter==self.__size:
            print('Overflow')
            i=0
            while (i<self.__size and  self.__table[i]!=x):
                i+=1
                
            if i==self.__size:
                return -1
            else:
                return i
        y=self.hashf(x)
        random.seed(y)
        r=random.randint(0, self.__size-1)
        if self.__table[r]==x:
            return r
        else:
            r=random.randint(0, self.__size-1)
            while not(self.__table[r]==None or self.__table[r]==x):
                r=random.randint(0, self.__size-1)
            if self.__table[r]==x:
                return r
            else:
                return -1
           
        
    def add_list(self,L):
        for i in L:
            self.add(i)
            
    def delete(self,x):
        if self.find(x)==-1:
            return -1
        else:
            a=self.find(x)
            y=self.hashf(x)
            random.seed(y)
            r=random.randint(0, self.__size-1)
            while(r!=a):
                r=random.randint(0, self.__size-1)
            r=random.randint(0, self.__size-1)
            if self.__table[r]==None:
                self.__table[a]=None
                self.__counter -= 1
                return 0
            else:
                self.__table[a]=None
                self.__counter -= 1
                b=self.__table[r]
                self.delete(b)
                self.__table[a]=b

    
                    
                
            
                
            
        

a=Hashtable(13)
a.add_list([12,34,45,67,78,26,13, 39, 89])
