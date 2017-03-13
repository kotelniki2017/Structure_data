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

    def delete_head(self):
        self.__first=self.__first.get_next()

    def delete_last(self):
        x=self.__first
        y=None
        while x.get_next() != None:
            y=x
            x=x.get_next()
        y.set_next(None)

    def put_into(self,n,x):
        a=self.__first
        for i in range(n-1):
            a = a.get_next()
        b = Node()
        b.set_value(x)
        b.set_next(a.get_next())
        a.set_next(b)
        
 L=mylist(); L.add(1);  L.add(2);L.add(3);
 L.print_list();L.put_into(2,6);
 
