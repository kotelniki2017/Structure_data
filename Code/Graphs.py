class node():
    __value = None
    __links = None
    __lable=None
    __d=None
    
    def __init__(self, n):
        self.__value = n
        self.__links = []
        self.__lable=False
        self.__d=None
        
    def set_value(self, n):
        self.__value = n

    def get_value(self):
        return self.__value

    def add_link(self, curNode, n):
        self.__links.append([curNode, n])

    def get_links(self):
        return self.__links

    def get_near_links(self):
        result = []
        for i in self.__links:
            if (i[1]!=None):
                result.append(i[0])
        return result

    def get_weight(self,node2):
        for i in self.get_links():
            if  i[0]==node2:
                return i[1]
        return None
    
    def print_weight_links(self):
        a = []
        for i in self.get_links():
            a.append(i[1])
        print(a)

class graph():
    __list_nodes = None

    def __init__(self):
        self.__list_nodes = []

    def create_from_adjacency(self, L):
        for x in range(len(L)):
            newNode = node(x)
            self.__list_nodes.append(newNode)
        for i in range(len(L)):
            for j in range(len(L)):
                self.__list_nodes[i].add_link(self.__list_nodes[j], L[i][j])


                
    def round_width(self, curNode):
        close_nodes = []
        open_nodes = [curNode]
        while (open_nodes!=[]):
            a = open_nodes[0].get_near_links()
            for i in a:
                if ((not (i in  open_nodes)) and (not(i in close_nodes))):
                    open_nodes.append(i)
                print(open_nodes[0].get_value(), "-", i.get_value())
            close_nodes.append(open_nodes[0])
            open_nodes = open_nodes[1:]
        return close_nodes

    def round_deep(self, curNode):
        close_nodes = []
        open_nodes = [curNode]
        while (open_nodes!=[]):
            a = open_nodes[-1].get_near_links()
            b=open_nodes[-1]
            for i in a:
                print(b.get_value(), "-", i.get_value())
            close_nodes.append(open_nodes.pop())
            for i in a:
                if ((not (i in  open_nodes)) and (not(i in close_nodes))):
                    open_nodes.append(i)

        
        return close_nodes
        
            
    
                
    def vizualize(self):
        for i in self.__list_nodes:
            i.print_weight_links()

    def get_list_nodes(self):
        return self.__list_nodes

   
            


def deykstra(self,current_node):
        for i in self.get_list_nodes():
            i.__lable=False
            i.__d=None
        current_node.__lable=True
        current_node.__d=0
        pr=True
        while pr:
            pr=False
            for i in self.get_list_nodes():
                if i.__ lable==False:
                    pr=True
                    break
            if pr:
                for i in  current_node.get_near_links():
                    if  i.__lable==False:
                        if i.__d==None:
                            i.__d=current_node.__d+current_node.get_weight(i)
                        else:
                            if i.__d>current_node.__d+current_node.get_weight(i):
                                 i.__d=current_node.__d+current_node.get_weight(i)
                for i in
            
                
            
G = graph()
G.create_from_adjacency([[None, 2, 10,None, None], [None, None, 3, -1, 7], [None, None, None, 5, None], [0, None, None, None, 1], [1, None, 12, None, None]])
#G.vizualize()
A=G.get_list_nodes()[0]
#G.round_width(A)

    
