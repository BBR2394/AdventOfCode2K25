#! python3

import sys
import uuid 

nb_node=0

class MyNode:
    def hasParent(self):
        if self.parent:
            return True
        else:
            return False

    def getName(self):
        return self.name
    
    def getInfo(self):
        print("ce node aura : ", self.maxChild, "efnants")
    
    def createAllChild(self, lvl=0):
        # print("creation lvl : ", lvl)
        # for i in range(lvl+1):
        #     print("***", end="")
        for i in range(self.maxChild):
            self.list_child.append(MyNode(max_child=self.maxChild, hello='enfant niveau :'+str(lvl), parent=self))
            if lvl > 0:
                self.list_child[len(self.list_child)-1].createAllChild(lvl=lvl-1)
            #print("======")
        self.has_created_child = True

    def displayAllChild(self, lvl=0):
        if self.has_created_child == False:
            return False
        print("->", self.id)
        for i in self.list_child:
            if lvl > 0:
                i.displayAllChild(lvl=lvl+1)
            print("|", end='')
            for j in range(lvl):
                print(" ", end='')
            print('>', i.id) 
            global nb_node
            nb_node = nb_node + 1

        

    def displayMyChild(self):
        if self.has_created_child == False:
            return False
        for i in self.list_child:
            print(i.id)


    def __init__(self, max_child=3, val=42, hello="le noeud", parent=None):
        self.id = uuid.uuid4()
        self.data = []
        self.maxChild = max_child
        self.val = val
        self.name = 'le nom du node'
        self.parent=parent
        self.has_created_child=False
        self.list_child = []
        parent=None
        # if parent != None:
        #     print("mon parent est : ", parent.id)
        # print("bonjour : ", hello, "mon id : ", self.id)

def readFile(nameFile):
    fd = open(av[1], 'r')
    # else:
    #    fd = open ("./data.txt", 'r')
    input = fd.read()

    for i in input:
        print(i)


def main(av):
    print("Bonjour - nothing special here ^^")
    if len(av) >= 2:
        readFile(av)
    else:
        print("on ne fait rien")

    tst = MyNode(hello='debut')
    #print(tst)

    level_child=8

    print(tst.getName())
    print("ID node principal = ", tst.id)
    print(tst.has_created_child)
    print("has Parettn : ", tst.hasParent())
    tst.createAllChild(lvl=level_child)
    print(tst.has_created_child)

    print('------')
    tst.displayMyChild()
    print('----')
    tst.displayAllChild(lvl=level_child)
    print("totla node = ", nb_node)
    #print(tst.getInfo())


if __name__ == '__main__':
    main(sys.argv)