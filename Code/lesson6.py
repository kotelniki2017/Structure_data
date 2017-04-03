import random
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
        

    def add_last(self, x):
        a=Node(x)
        self.__last.set_next(a)
        a.set_prev(self.__last)
        self.__last = a


    def add_fix(self, x, y):
        count=0
        a=Node(x)
        b=self.__first
        while b.get_next()!=None:
            if count==y:
                a.set_next(b.get_next())
                b.get_next().set_prev(a)
                b.set_next(a)
                a.set_prev(b)
                break
            else:
                b=b.get_next()
                count+=1
        
    def print_list(self):
        x = self.__first
        while x.get_next() != None:
            print(x.get_value())
            x = x.get_next()
        print(x.get_value())

    def get_first(self):
        return self.__first
    
    def get_last(self):
        return self.__last

    def bubble_sort(self):
        y = self.__last
        x = self.__first
        p = True
        while (p & (x != y)):
            p = False
            while (x != y)&(x != self.__last):
                if x.get_value() > x.get_next().get_value():
                    a = x
                    b = x.get_next()
                    if a == self.__first:
                        self.__first = b
                    if b == self.__last:
                        self.__last = a
                        y = self.__last
                    if a.get_prev() != None:
                        b.set_prev(a.get_prev())
                    else:
                        b.set_prev(None)
                    if b.get_next() != None:
                        a.set_next(b.get_next())
                    else:
                        a.set_next(None)
                    b.set_next(a)
                    a.set_prev(b)
                    if b.get_prev() != None:
                        b.get_prev().set_next(b)
                    if a.get_next() != None:
                        a.get_next().set_prev(a)
                    p = True
                    x = b  
                x = x.get_next()
            y = y.get_prev()
            x = self.__first

    def random_list(self,n,m):
        for i in range(n):
            a=random.randint(1,m)
            self.add_last(a)

    def selection_sort(self):
        y = self.__last
        a=self.__first
        while (a != y):
            x=a
            min_element=a
            
            while (x!=y):
                if (min_element.get_value()>x.get_value()):
                    min_element=x
                x=x.get_next()
            if (min_element!=a):
                w=min_element
                v=a
                
                if(min_element!=self.__last):
                    v.get_next().set_prev(w)
                    w.get_next().set_prev(v)
                else:
                   v.get_next().set_prev(w)
                   self.__last=v
                   
 
                if(v!=self.__first):
                    v.get_prev().set_next(w)
                    w.get_prev().set_next(v)
                else:
                    w.get_prev().set_next(v)
                    self.__first=w
                    v.set_prev(w.get_prev())
                    w.set_prev(None)
                    
                z=v.get_prev()
                v.set_prev(w.get_prev())
                w.set_prev(z)

                z=v.get_next()
                v.set_next(w.get_next())
                w.set_next(z)

                

                

            a=a.get_next()


            

        

            
                    
                
        
            



L = mylist(2)
L.add_last(1)
L.add_last(5)
L.add_last(0)
L.add_last(4)
L.add_last(3)
L.print_list()







    

