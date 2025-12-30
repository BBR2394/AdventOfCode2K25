#! python3

import sys
import uuid 

class GraphNode:

    def DisplayInfo(self):
        print("Lvl:", self.level, ",Id : ", self.id, "pseudo : ", self.easy_id," data : ", self.data_string)

    def DisplayPseudo(self):
        print(self.easy_id)
        return True

    def DisplayChild(self, recurent=False):
        for i in self.list_child:
            if recurent:
                 for j in range(0, self.level):
                    print("-", end="")
            i.DisplayInfo()
            if recurent:
                i.DisplayChild(recurent)

    
    def DisplayParents(self):
        if self.level == 1:
            print("le parent est le noeud maitre")
        for i in self.list_parent:
            i.DisplayInfo()

    def GetShortId(self):
        return str(self.id)[30:]

    def CreateChildFromData(self, data="no data", pseudoGiven="no pseudo", childSParent=None): #childSParent == chil's parent
        self.list_child.append(GraphNode(data, lvl=self.level+1, pseudo=pseudoGiven ,parent=childSParent))

    def AddParent(self, parent):
        if self.level > parent.level:
            self.list_parent.append(parent)
        else:
            print("cannot add parent because it is not in the right level : it must be in lower level")

    def hasParent(self):
        if len(self.list_parent) > 0:
            return True
        else:
            return False

    def __init__(self, data="", lvl=1, pseudo="", parent=None, uuid_arg=""):
        if uuid_arg:
            self.id = uuid.UUID(uuid_arg)
        else:
            self.id = uuid.uuid4()
        self.level = lvl
        self.easy_id=pseudo
        self.data_string = data
        self.list_child = []
        self.list_parent = []

        if parent:
            self.list_parent.append(parent)


class MaistreNode:

    def FindChildById(self):
        print("recherche d'un enfant par le uid WIP")
        #for i in 

    def GenOneMainChild(self, dataGvn="nothing", pseudoGvn="pseudoD_default"):
        self.list_root_node.append(GraphNode(data=dataGvn, pseudo=pseudoGvn))

    def CreateMainChild(self, uuid, dataGvn, pseudoGvn):
        self.list_root_node.append(GraphNode(data=dataGvn, pseudo=pseudoGvn, uuid_arg=uuid))

    def DisplayRootNode(self):
        for i in self.list_root_node:
            i.DisplayInfo()

    def __init__(self, name_given="Maistre"):
        print("Creation of one Maistre Node")
        self.name = name_given
        self.list_root_node = []

def dynamicGenGraphe(masterNode=None):
    tst=None #the cursor
    
    while True:
        if tst != None:
            print("[", tst.GetShortId(), "] - ", end="")
            print(tst.DisplayPseudo())
            print("$--$")

        entry = input("Que voulez-faire?\n--$>")

        if entry == 'quit':
            print("Au revoir")
            return True
        elif entry == 'add':
            entry_bis = input("Que voulez-ajouter?\n--$>")
            if tst:
                tst.CreateChildFromData(data=entry_bis, childSParent=tst)
            else : 
                masterNode.GenOneMainChild(dataGvn=entry_bis)
            #tst.addOneChild(dataStr=entry_bis, dataVal=42)
        elif entry == 'display':
            masterNode.DisplayRootNode()
        elif entry == "display_all":
            if tst:
                tst.DisplayChild(True)
            else:
                for i in masterNode.list_root_node:
                    i.DisplayInfo()
                    i.DisplayChild(True)
        elif entry == 'display_child':
            if tst:
                rtr = tst.DisplayChild()
                print('retour : ', rtr)
            else :
                print("affichage des noeud principaux")
                masterNode.DisplayRootNode()
        elif entry == 'select_child':
            if tst == None:
                print("premiere initialisation")
                masterNode.DisplayRootNode()
            else :
                tst.DisplayChild()
                
        elif entry == 'display_current':
            if tst != None:
                tst.DisplayInfo()
            else :
                print("cursor Not Init")
        # elif entry == 'info':
        #     rtr = tst.getInfo()
        elif entry == 'p_moovein':
            if tst == None:
                print("le seul parent est le neud maitre")
            else :
                tst.DisplayParents()
                #entry_bis = input("choississez\n--$>")

        elif entry == 'moovein':
            print("dans quel enfant se deplacer ? ")
            if tst == None:
                print("premiere initialisation")
                masterNode.DisplayRootNode()
            else :
                tst.DisplayChild()

            entry_bis = input("choississez\n--$>")
            try:
                entry_int = int(entry_bis)
                if entry_int < 0:
                    print("le nœud choisit ne peut etre negatif")
                else:
                    print("selection du noeud : ", entry_int)
                    if tst == None:
                        tst = masterNode.list_root_node[entry_int]
                    else :
                        if entry_int > len(tst.list_child):
                            print("le nœud choisit ne peut dépasser le tableau")
                        else:
                            tst = tst.list_child[entry_int]
            except:
                print(" une erreur est survenu : avez vous choisit une bonne valeur ?")
        elif entry == 'reset_cursor':
            print("retour au nœud maitre")
            tst = None
        elif entry == 'display_parents':
            if tst == None:
                print("No parents : main node")
            else :
                tst.DisplayParents()
        elif entry == "goto_parent":
            if tst.hasParent():
                print("on affiche les parents")
                tst.DisplayParents()
            else : 
                print(" on n'a pas de parent (ou pas de parent lié")

        # elif entry == "picture":
        #     global extract
        #     extract = []
        #     genDataForPicture(main_node=masterNode, and_data=True)
        #     fileName = "toto_dyn_graph"
        #     genPicture(fileName=fileName)

def defaultCreation(mainNode):
    print("default creation")
    mainNode.GenOneMainChild("bonjour", "Salutation arrivé")
    mainNode.GenOneMainChild("au revoir", "Salutation départ")
    mainNode.GenOneMainChild("ntm", "Salutation insulte")
    mainNode.GenOneMainChild("une donnée")
    mainNode.DisplayRootNode()
    dynamicGenGraphe(mainNode)


def readAndStoreFromFile(nodeMaster, filename):
    fd = open("data.csv", 'r')
    input = fd.read()
    lst = input.split('\n')
    idx = 1
    while idx < len(lst):
        print(lst[idx])
        
        line = lst[idx].split(';')
        print(line)
        if int(line[3]) == 1:
            nodeMaster.CreateMainChild(line[0], line[2], line[1])
        else:
            print("->pour le moment on ne fait que le niveau 1")
        idx+=1

def main(av):
    print("run graph.py")
    mn = MaistreNode()

    if len(av) >= 2:
        if av[1] == "--dyn" or av[1] == "-d":
            dynamicGenGraphe(mn)
            return 0
        elif av[1] == "--dyn-auto" :
            defaultCreation(mn)
        elif av[1] == "-r" :
            print("readfile")
            readAndStoreFromFile(mn, "")
            mn.DisplayRootNode()
            dynamicGenGraphe(mn)
        
            #if 
            #readFile(av[2])
            #defaultCreation(mn)
    else :
        defaultCreation(mn)




if __name__ == '__main__':
    main(sys.argv)