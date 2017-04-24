class heap():
    __body = []

    def __init__(self):
        self.__body = []

    def get_left_child(self,n):
        try:
            return self.__body[2*n + 1]
        except:
            return None

    def get_right_child(self,n):
        try:
            return self.__body[2*n + 2]
        except:
            return None

    def get_parent(self,n):
        try:
            if (n-1)//2<0:
                return None
            else:
                return self.__body[(n-1)//2]
        except:
            return None

    def bubble_up(self,n):
        if n==0:
            return True
        if self.get_parent(n)>=self.__body[n]:
            return True
        else:
            temp=self.__body[n]
            self.__body[n]=self.get_parent(n)
            self.__body[(n-1)//2] = temp
            return self.bubble_up((n-1)//2)

    def add(self, n):
        self.__body.append(n)
        self.bubble_up(len(self.__body)-1)

    def add_list(self,L):
        for i in L:
            self.add(i)

    def get_body(self):
        return self.__body

             
                                                    
                 


    
        
