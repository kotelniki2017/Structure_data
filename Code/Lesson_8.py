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
        self.__parent = m_node

    def set_left(self,m_node):
        self.__left = m_node

    def set_right(self,m_node):
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

    def add_list(self, lst):
        for i in lst:
            self.add_node(i, self.get_top())

    def visualize(self, current_node):
        if (current_node.get_left()==None) and (current_node.get_right()==None):
            return [current_node.get_info(), [], []]
        elif current_node.get_left()==None:
            return [current_node.get_info(), [], self.visualize(current_node.get_right())]
        elif current_node.get_right()==None:
            return [current_node.get_info(), self.visualize(current_node.get_left()), []]
        else:
            return [current_node.get_info(), \
                    self.visualize(current_node.get_left()), \
                    self.visualize(current_node.get_right())]


    def find_el(self,value,current_node):
        if current_node.get_info()==value:
            return True
        elif (current_node.get_right()== None)&(current_node.get_left()==None): 
            return False
        elif current_node.get_info()>value:
            return self.find_el(value,current_node.get_left())
        else:
            return self.find_el(value,current_node.get_right())

    def count_vertex(self, current_node):
        if (current_node.get_left() == None) and (current_node.get_right() == None):
            return 1
        elif (current_node.get_left() == None) and (current_node.get_right() != None):
            return self.count_vertex(current_node.get_right()) + 1
        elif (current_node.get_left() != None) and (current_node.get_right() == None):
            return self.count_vertex(current_node.get_left()) + 1
        else:
            return self.count_vertex(current_node.get_left()) + self.count_vertex(current_node.get_right()) + 1

    def count_leaves(self, current_node):
        if (current_node.get_left() == None) and (current_node.get_right() == None):
            return 1
        elif (current_node.get_left() == None) and (current_node.get_right() != None):
            return self.count_leaves(current_node.get_right()) 
        elif (current_node.get_left() != None) and (current_node.get_right() == None):
            return self.count_leaves(current_node.get_left())
        else:
            return self.count_leaves(current_node.get_left()) + self.count_leaves(current_node.get_right())

    def depth_tree(self,current_node):
        if current_node == None:
            return 0
        if (current_node.get_left() == None) and (current_node.get_right() == None):
            return 0
        elif (current_node.get_left() == None) and (current_node.get_right() != None):
            return 1+self.depth_tree(current_node.get_right())
        elif (current_node.get_left() != None) and (current_node.get_right() == None):
            return 1+self.depth_tree(current_node.get_left())
        elif self.depth_tree(current_node.get_left())>=self.depth_tree(current_node.get_right()):
            return 1+self.depth_tree(current_node.get_left())
        else:
            return 1+self.depth_tree(current_node.get_right())

    def step_up(self, current_node):
        if current_node.get_parent() != None:
            print(current_node.get_parent().get_info())
        return current_node.get_parent()
    
    def step_left(self, current_node):
        if current_node.get_left() != None:
            print(current_node.get_left().get_info())
        return current_node.get_left()

    def step_right(self, current_node):
        if current_node.get_right() != None:
            print(current_node.get_right().get_info())
        return current_node.get_right()

    def turn_left(self, current_node):
        if current_node.get_right() != None:
            a = current_node
            a_par = current_node.get_parent()
            b = current_node.get_right()
            c = b.get_left()
            a.set_parent(b)
            b.set_left(a)
            a.set_right(c)
            b.set_parent(a_par)
            if a_par != None:
                if a_par.get_right() == a:
                    a_par.set_right(b)
                else:
                    a_par.set_left(b)
            else:
                self.__top = b
        else:
            print("ERROR")


    def infix_traverse(self,  current_node):
        if current_node == None:
            return []
        elif (current_node.get_left()==[]) & \
             (current_node.get_right()==[]):
            return [current_node.get_info()]
        elif (current_node.get_left()!=[]) & \
             (current_node.get_right()==[]):
            return \
                self.infix_traverse(current_node.get_left())+ \
                [current_node.get_info()]
        elif (current_node.get_left()==[]) & \
             (current_node.get_right()!=[]):
            return  [current_node.get_info()]+\
                self.infix_traverse(current_node.get_right())
        else:
            return  \
                self.infix_traverse(current_node.get_left())+\
                [current_node.get_info()]+\
                self.infix_traverse(current_node.get_right())

    def postfix_traverse(self,  current_node):
        if current_node == None:
            return []
        elif (current_node.get_left()==[]) & \
             (current_node.get_right()==[]):
            return [current_node.get_info()]
        elif (current_node.get_left()!=[]) & \
             (current_node.get_right()==[]):
            return \
                [current_node.get_info()] + \
                self.postfix_traverse(current_node.get_left())
        elif (current_node.get_left()==[]) & \
             (current_node.get_right()!=[]):
            return  \
                self.postfix_traverse(current_node.get_right())+\
                [current_node.get_info()]
        else:
            return  \
                self.postfix_traverse(current_node.get_right())+\
                [current_node.get_info()]+\
                self.postfix_traverse(current_node.get_left())


    def prefix_traverse(self,  current_node):
        if current_node == None:
            return []
        elif (current_node.get_left()==[]) & \
             (current_node.get_right()==[]):
            return [current_node.get_info()]
        elif (current_node.get_left()!=[]) & \
             (current_node.get_right()==[]):
            return \
                [current_node.get_info()] + \
                self.prefix_traverse(current_node.get_left())
        elif (current_node.get_left()==[]) & \
             (current_node.get_right()!=[]):
            return [current_node.get_info()]+\
                self.prefix_traverse(current_node.get_right())\
                
        else:
            return  [current_node.get_info()]+\
                self.prefix_traverse(current_node.get_left())+\
                self.prefix_traverse(current_node.get_right())

    
    def find_min(self,  current_node):
        if (current_node.get_left()==None):
            return current_node.get_info()
        else:
            return self.find_min(current_node.get_left())
    def find_max(self,  current_node):
        if (current_node.get_right()==None):
            return current_node.get_info()
        else:
            return self.find_max(current_node.get_right())
        

    def delete_node(self,current_node):
        if (current_node.get_left()==None)&(current_node.get_right()==None):
            if current_node.get_parent().get_left()==current_node:
                current_node.get_parent().set_left(None)
                current_node.set_parent(None)
                return
            else:
                current_node.get_parent().set_right(None)
                current_node.set_parent(None)
                return
        if (current_node.get_left()!=None)&(current_node.get_right()==None):
            if (current_node.get_left().get_left()==None)&(current_node.get_left().get_right()==None):
                current_node.set_value(current_node.get_left().get_info())
                current_node.get_left().set_parent(None)
                current_node.set_left(None)
                return
        if (current_node.get_left()==None)&(current_node.get_right()!=None):
            if (current_node.get_right().get_left()==None)&(current_node.get_right().get_right()==None):
                current_node.set_value(current_node.get_right().get_info())
                current_node.get_right().set_parent(None)
                current_node.set_right(None)
                return
        if self.depth_tree(current_node.get_left())>=self.depth_tree(current_node.get_right()):
            current_node.set_value(current_node.get_left().get_info())
            current_node=current_node.get_left()
            return self.delete_node(current_node)
        else:
            current_node.set_value(current_node.get_right().get_info())
            current_node=current_node.get_right()
            return self.delete_node(current_node)


           
    def get_node(self,value,current_node):
        if current_node.get_info()==value:
            return current_node
        #elif (current_node.get_right()== None)&(current_node.get_left()==None): 
        #    return 'Not found'
        elif current_node.get_info()>value:
            return self.get_node(value,current_node.get_left())
        else:
            return self.get_node(value,current_node.get_right())



#r=tree(5)
#r.add_list([6,47,8,3,2,9,10])
r=tree(6)
r.add_list([1,8,6,5,9,4,0,7,10,-4,9.5,11])













