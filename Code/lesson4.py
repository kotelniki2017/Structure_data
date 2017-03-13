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
    __count = 0

    def add(self,x):
        a = Node()
        a.set_value(x)
        a.set_next(self.__first)
        self.__first = a
        self.__count += 1
        del a

    def get_count(self):
        return self.__count
    def get_first(self):
        return self.__first
    
    def print_list(self):
        x= self.__first
        while x.get_next() != None:
            print(x.get_value())
            x = x.get_next()
        print(x.get_value())
    
