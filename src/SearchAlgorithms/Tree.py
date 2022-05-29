"""
Class Tree
"""

from ast import For
from socket import SO_SNDBUF


class Tree(object):
    def __init__(self, value):
        self.value = value
        self.sons = []
        self.depth = 0

    def getValue(self):
        return self.value

    def getSons(self):
        return self.sons

    def addSon(self, sonValue):
        newSon = Tree(sonValue)
        self.sons.append(newSon)
        return newSon

    #To implement
    def getDepth(self):
        return self.depth


    """ def getNodeString(self):
        string = ""
        string = str(self.getValue())
        string = string + " ("
        for node in self.getSons():
            string = string + str(node.getValue()) + " "
        string = string + ")"
        return string """

    #To implement
    def __str__(self):
        return self.getNodeString()



mytree = Tree(1)
mytree.addSon(2)
mytree.addSon(3)
mytree.addSon(4)
mytree.getSons()[0].addSon(5)
mytree.getSons()[1].addSon(6)
mytree.getSons()[1].addSon(7)