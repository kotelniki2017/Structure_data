

class Node :
    __value = None
    __next = None
    __prev = None
    __number = None

    def __init__(self,x):
      self.__value=x
    def set_number (self, x ) :
        self.__number = x
    def get_number ( self ) :
        return self.__number
    def set_value (self, x ) :
        self.__value = x
    def set_next ( self , y ) :
        self.__next = y
    def set_prev ( self , y ) :
        self.__prev = y
    def get_value ( self ) :
        return self.__value
    def get_next ( self ) :
        return self.__next
    def get_prev ( self ) :
        return self.__prev
        
class mylist:
    __first = None
    __last = None

    def __init__(self, x):
        a=Node(x)
        self.__first = a
        self.__last = a

    def add_first(self, x):
        if self.__first.get_next==None:
            self.__last = self.__first
        a=Node(x)
        a.set_next(self.__first)
        self.__first.set_prev(a)
        self.__first = a
        

    def print_list(self):
        x = self.__first
        while x.get_next() != None:
            print(x.get_value())
            x = x.get_next()
        print(x.get_value())

    def get_first(self):
        return self.__first
    

    def find(self, x):
        y = self.__first
        while y.get_next() != None and y.get_value()!=x:
            y = y.get_next()
        
        
   
class Hashtable:
    __size=None
    __table=None
    

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
    

    
    def add(self,x):
        y=self.hashf(x)
        if self.__table[y]==None:
            a=mylist(x)
            self.__table[y]=a
        else:
            self.__table[y].add_first(x)
            
            
            
        
        
    def find(self,x):
        y=self.hashf(x)
        if (self.__table[y]==None):
            return -1
        else:
            
       
           
        
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
