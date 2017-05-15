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
        current_last=self.get_last()
        while (current_last!=self.get_first()):
            current=self.get_first()
            while (current!=current_last):
                if(current.get_value()>current.get_next().get_value()):
                    a=current.get_value()
                    current.set_value(current.get_next().get_value())
                    current.get_next().set_value(a)
                current=current.get_next()
            current_last=current_last.get_prev()
            
        
                
                
L=mylist(5)
L.add_last(3)
L.add_last(4)
L.add_last(1)
L.print_list()
