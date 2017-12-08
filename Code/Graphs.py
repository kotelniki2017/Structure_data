class node():
    __value = None
    __links = None
    lable=None
    d=None
    ways=None
    
    def __init__(self, n):
        self.__value = n
        self.__links = []
        self.lable=False
        self.d=None
        self.ways=[]
        
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
            i.lable=False
            i.d=None
        current_node.lable=True
        current_node.d=0
        pr=True
        while pr:
            pr=False
            for i in self.get_list_nodes():
                if i.lable==False:
                    pr=True
                    break
            if pr:
                for i in  current_node.get_near_links():
                    if  i.lable==False:
                        if i.d==None:
                            i.ways.append(current_node.get_value())
                            i.d=current_node.d+current_node.get_weight(i)
                        else:
                            if i.d>current_node.d+current_node.get_weight(i):
                                i.ways.append(current_node.get_value())
                                i.d=current_node.d+current_node.get_weight(i)
                mind=None;

                
                
                for i in self.get_list_nodes():
                    if (i.lable==False)&(i.d!=None):
                        if mind==None:
                            mind=i.d
                            current_node=i
                        elif (mind>i.d):
                            mind=i.d
                            current_node=i
                current_node.ways.append(current_node.get_value())
                current_node.lable=True
                            
    def print_d(self):
         for i in self.get_list_nodes():
             print("Вершина ",i.get_value()," : ",i.d)
    def prima(self, cur_node):
        V=[cur_node]
        R=[]
        R1=[]
        while (len(V)!=len(self.__list_nodes)):
            near=cur_node.get_links()
            min_w=float("inf")
            for i in near:
                if not(i[0] in V) and i[1]!=None:
                    R1.append([[cur_node.get_value(),i[0].get_value()], i[1], i[0]])
            print("Проход")
            for i in R1:
                print(i[0])
            for i in range(len(R1)):
                if min_w>R1[i][1]:
                    min_w=R1[i][1]
                    min_node=R1[i][2]
                    min_index=i
            R.append([cur_node.get_value(),min_node.get_value()])
            del R1[min_index]        
            
            V.append(min_node)
            cur_node=min_node
        print(R)    
            
                    
               
            
G = graph()
G1= graph()
G.create_from_adjacency([[None, 2, 10,None, None], [None, None, 3, 1, 7], [None, None, None, 5, None], [0, None, None, None, 1], [1, None, 12, None, None]])
G1.create_from_adjacency([[None, 2, 10, 0, 1], [2, None, 3, 1, 7], [10, 3, None, 5, 12], [0, 1, 5, None, 1], [1,7, 12, 1, None]])
G1.vizualize()
A=G.get_list_nodes()[0]
#G.round_width(A)

    
