class Hashtable:
    __size=None
    __table=None
    def __init__(self,n):
      self.__size=n
      self.__table=[]
      for i in range(n):
          self.__table.append(None)
    def hashf(self,x):
        return x%self.__size
    def get_table(self):
        return self.__table
    def get_size(self):
        return self.__size
    def add(self,x):
        self.__table[self.hashf(x)]=x
