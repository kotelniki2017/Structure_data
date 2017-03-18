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


    def search(self,x):
        current = self.__first
        found = False
        while (current != None) and (not found):
            if current.get_value() == x:
                found = True
            else:
                current = current.get_next()
        return found

    def count(self):
        a = self.__first
        count = 1
        while a.get_next() != None:
            a = a.get_next()
            count += 1
        return count

    def buble(self):
        for i in range(L.count()):
            a = self.__first
            b = self.__first.get_next()
            while b != None:
                if a.get_value() > b.get_value():
                    i = a.get_value()
                    j = b.get_value()
                    a.set_value(j)
                    b.set_value(i)
                else:
                    a = a.get_next()
                    b = b.get_next()

L=mylist()
L.add(1)
L.add(9)
L.add(3)
L.add(45)
L.add(13)
L.add(27)
L.print_list()
 
