class Hashtable:
    __size=None
    __table=None

    def __init__(self,n):
      self.__size=n
      self.__table=[]
      for i in range(n):
          self.__table.append(None)

    def hashf(self,s):
        if type(s)==str:
            H=0
            for i in s:
                H=(H<<4)+ord(i)
                G=H&0xF0000000
                if G!= 0:
                    H=(H^(G>>24))^G
            return H%self.__size
        else:
            H=0
            H=(H<<4)+s
            G=H&0xF0000000
            if G!= 0:
                H=(H^(G>>24))^G
            return H%self.__size

    def get_table(self):
        return self.__table

    def get_size(self):
        return self.__size

    def add(self,x):
        if self.__table[self.hashf(x)]==None:
            self.__table[self.hashf(x)]=x
        else:
            k=self.hashf(x)
            L=k+1
            if L > self.__size-1:
                L=0
            print(L)
            while ((self.__table[L]!=None) & (L!=k)):
                if L == self.__size-1:
                    L=0 
                else:
                    L+=1
            if L==k:
                print('Error!')
                return 1
            self.__table[L]=x
            return 0
        
    def find(self,x):
        if self.__table[self.hashf(x)]==x:
            return self.hashf(x)
        else:
            k=self.hashf(x)
            L=k+1
            if L > self.__size-1:
                L=0
            while ((self.__table[L]!=x) & (L!=k)):
                if L == self.__size-1:
                    L=0 
                else:
                    L+=1
            if L==k:
                return -1
            return L
        
    def add_list(self,L):
        for i in L:
            self.add(i)
            
    def delete(self,element):
        if self.find(element)==-1:
            return -1
        else:
            a=self.find(element)
            if self.__table[(a+1)%self.__size]==None:
                self.__table[a]=None
                return 0
            else:
                self.__table[a]=None
                b=self.__table[(a+1)%self.__size]
                self.delete(b)
                self.add(b)

    
                    
                
            
                
            
        

a=Hashtable(13)
a.add_list([12,34,45,67,78,26,13, 39, 89])
