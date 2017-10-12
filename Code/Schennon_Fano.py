def del_rep(L):
    if L==[]:
        return L
    elif (L[0] in L[1:]):
        return del_rep(L[1:])
    else:
        return [L[0]]+del_rep(L[1:])


def score_count(L):
    S = del_rep(list(L))
    a = 0
    H = []
    for i in range(len(S)):
        for j in range(len(L)):
            if L[j] == S[i]:
                a+=1
        H.append([a,S[i]])         
        a=0
    return H

def summ_elem(L):
    s=0
    for i in L:
        s+=i[0]
    return s


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

    def build_tree(self,L,current_node):
        if len(L)==1:
            current_node.set_value(L[0][1])
            return 0
        elif L==[]:
            return 0
        else:
            d=summ_elem(L)//2
            print(L)
            summ=L[0][0]
            index=1
            while (summ+L[index][0])<=d:
                summ+=L[index][0]
                index+=1
            current_node.set_value(summ)
            left_child=node(0)
            right_child=node(0)
            current_node.set_left(left_child)
            current_node.set_right(right_child)
            left_child.set_parent(current_node)
            right_child.set_parent(current_node)
            s1=L[0:index]
            s2=L[index:]
            self.build_tree(s1,left_child)
            self.build_tree(s2,right_child)



    def decoding(self, L,current_node):
        if L=="":
            if (current_node.get_left()==None) & (current_node.get_right()==None):
                return str(current_node.get_info())
            else:
                return "Error"
        elif  (current_node.get_left()==None) & (current_node.get_right()==None):
            return str(current_node.get_info())+self.decoding(L,self.get_top())
        elif L[0]=="0":
            return self.decoding(L[1:],current_node.get_left())
        elif L[0]=="1":
            return self.decoding(L[1:],current_node.get_right())
        else:
            return print("error!")

    def coding(self, L):
        s=''
        for i in L:
            current_node=self.find_el(i,self.get_top())
            if current_node==None:
                    print('Error')
                    return None
            s1=''
            while current_node!=self.get_top():
                if current_node.get_parent().get_left()==current_node:
                    s1='0'+s1
                else:
                    s1='1'+s1
                current_node=current_node.get_parent()
            s=s+s1
        return s
            

    def find_el(self,value,current_node):
        if current_node==None:
            return None
        elif current_node.get_info()==value:
            return current_node
        elif (self.find_el(value,current_node.get_left())==None):
            return self.find_el(value,current_node.get_right())
        else:
            return self.find_el(value,current_node.get_left())
                


    def visualize(self, current_node):
        if (current_node.get_left()==None) and (current_node.get_right()==None):
            return [current_node.get_info(), [], []]
        elif current_node.get_left()==None:
            return [current_node.get_info(), [], self.visualize(current_node.get_right())]
        elif current_node.get_right()==None:
            return [current_node.get_info(), self.visualize(current_node.get_left()), []]
        else:
            return [current_node.get_info(), self.visualize(current_node.get_left()), self.visualize(current_node.get_right())]
                
                
            
Tr = tree(0)
L = score_count("sadasgwefghdfgsdfgsafffgssgdgfsa")
L.sort()
L.reverse()
Tr.build_tree(L,Tr.get_top())
