#! python3

import sys
import uuid 

class GraphNode:

    def DisplayInfo(self):
        print("Id : ", self.id, "pseudo : ", self.easy_id," data : ", self.data_string, "level : ", self.level)

    def DisplayChild(self):
        for i in self.list_child:
            i.DisplayInfo()
    
    # def DisplayParent(self):
    #     for i in self.list_parent:
    #         i.DisplayInfo()

    def GetShortId(self):
        return str(self.id)[30:]

    def CreateChildFromData(self, data="no data", pseudo="no pseudo"):
        self.list_child.append(GraphNode(data, self.level+1))

    def __init__(self, data="", lvl=1, pseudo=""):
        self.id = uuid.uuid4()
        self.level = lvl
        self.easy_id=pseudo
        self.data_string = data
        self.list_child = []
        self.list_parent = []



class MaistreNode:

    def FindChildById(self):
        print("recherche d'un enfant par le uid WIP")
        #for i in 

    def GenOneMainChild(self, dataGvn="nothing", pseudoGvn="pseudoD_default"):
        self.list_root_node.append(GraphNode(data=dataGvn, pseudo=pseudoGvn))

    

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
            print("[", tst.GetShortId(), "]")
        entry = input("Que voulez-faire?\n--$>")

        if entry == 'quit':
            print("Au revoir")
            return True
        elif entry == 'add':
            entry_bis = input("Que voulez-ajouter?\n--$>")
            if tst:
                tst.CreateChildFromData(data=entry_bis)
            else : 
                masterNode.GenOneMainChild(dataGvn=entry_bis)
            #tst.addOneChild(dataStr=entry_bis, dataVal=42)
        elif entry == 'display':
            masterNode.DisplayRootNode()
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
        # elif entry == 'display_child':
        #     rtr = tst.displayMyChild()
        #     print('retour : ', rtr)
        # elif entry == 'info':
        #     rtr = tst.getInfo()
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
            tst = masterNode
        # elif entry == "goto_parent":
        #     if tst.hasParent():
        #         tst = tst.parent
        #     else : 
        #         print(" on n'a pas de parent ")
        # elif entry == "picture":
        #     global extract
        #     extract = []
        #     genDataForPicture(main_node=masterNode, and_data=True)
        #     fileName = "toto_dyn_graph"
        #     genPicture(fileName=fileName)

def main(av):
    print("run graph.py")
    mn = MaistreNode()
    mn.GenOneMainChild("bonjour", "Salutation arrivé")
    mn.GenOneMainChild("au revoir", "Salutation départ")
    mn.GenOneMainChild("ntm", "Salutation insulte")
    mn.DisplayRootNode()

    dynamicGenGraphe(mn)




if __name__ == '__main__':
    main(sys.argv)