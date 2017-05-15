class Node :
    __value = None
    __next = None
    def set_value (self, x ) :
        self.__value = x
    def set_next ( self , y ) :
        self.__next = y
    def get_value ( self ) :
        return self.__value
    def get_next ( self ) :
        return self.__next
        
class mylist:
    __first = None
    __last=None

    def __init__(self,x):
        current=Node()
        current.set_value(x)
        self.__first=current
        self.__last=current
        

    def add(self,x):
        a = Node()
        a.set_value(x)
        self.__last.set_next(a)
        self.__last = a
        
    def print_list(self):
        x= self.__first
        while x.get_next() != None:
            print(x.get_value())
            x = x.get_next()
        print(x.get_value())

    def delete(self):
        self.__first=self.__first.get_next()

    def delete_two(self):
        L=self.length()
        for i in (range(L)):
            if( (i+1)%2==0):
                self.delete()
            else:
                a=self.__first.get_value()
                self.delete()
                self.add(a)


    def length(self):
        result=0
        current =self.__first
        while(current!=None):
            result+=1
            current=current.get_next()
        return result


L=mylist(6)
L.add(1)
L.add(9)
L.add(3)
L.add(45)
L.add(13)
L.add(27)
L.print_list()













