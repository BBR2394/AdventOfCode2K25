#! python3

import sys
import uuid 

class GraphNode:

    def DisplayInfo(self):
        print("Id : ", self.id, "pseudo : ", self.easy_id," data : ", self.data_string)

    def __init__(self, data="", lvl=1, pseudo=""):
        self.id = uuid.uuid4()
        self.easy_id=pseudo
        self.data_string = data
        self.list_child = []
        self.list_parent = []
        self.level = lvl


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

def main(av):
    print("run graph.py")
    mn = MaistreNode()
    mn.GenOneMainChild("bonjour", "Salutation arrivé")
    mn.GenOneMainChild("au revoir", "Salutation départ")
    mn.GenOneMainChild("ntm", "Salutation insulte")
    mn.DisplayRootNode()


if __name__ == '__main__':
    main(sys.argv)