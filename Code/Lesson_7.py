#Задание структуры бинарного дерева поиска

class node():
    __parent = None
    __left = None
    __right = None
    __info = None

    def __init__(self, value):
        self.__info = value
        self.__parent = None
        self.__left = None
        self.__right = None

    def get_parent(self):
        return self.__parent

    def get_left(self):
        return self.__left

    def get_right(self):
        return self.__right

    def get_info(self):
        return self.__info

    def set_value(self,a):
        self.__info = a

    def set_parent(self,m_node):
        if isinstance(m_node,node):
            self.__parent = m_node

    def set_left(self,m_node):
        if isinstance(m_node,node):
            self.__left = m_node

    def set_right(self,m_node):
        if isinstance(m_node,node):
            self.__right = m_node


class tree():

    __top = None

    def __init__(self,value):
        self.__top = node(value)
        #return 'ok'

    def get_top(self):
        return self.__top

    def add_node(self, value,current_node):
        if current_node.get_info()>value:
            if current_node.get_left() == None:
                a = node(value)
                current_node.set_left(a)
                a.set_parent(current_node)
            else:
                current_node = current_node.get_left()
                self.add_node(value,current_node)
        else:
            if current_node.get_right() == None:
                a = node(value)
                current_node.set_right(a)
                a.set_parent(current_node)
            else:
                current_node = current_node.get_right()
                self.add_node(value,current_node)

    def visualize(self, current_node):
        if (current_node.get_left()==None) and (current_node.get_right()==None):
            return [current_node.get_info(), [], []]
        elif current_node.get_left()==None:
            return [current_node.get_info(), [], self.visualize(current_node.get_right())]
        elif current_node.get_right()==None:
            return [current_node.get_info(), self.visualize(current_node.get_left()), []]
        else:
            return [current_node.get_info(), self.visualize(current_node.get_left()), self.visualize(current_node.get_right())]
        
