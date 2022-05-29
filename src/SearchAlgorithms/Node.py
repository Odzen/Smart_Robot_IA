"""
Class Node
"""

class Node(object):
    def __init__(self, value):
        self.value = value
        self.children = []

    def getValue(self):
        return self.value

    def getChildren(self):
        return self.children

    def addChild(self, childValue):
        newChildren = Node(childValue)
        self.children.append(newChildren)
        #return newChildren


    def getDepth(self):
        if not self.children:
            return 1
        else:
            return 1 + max(x.getDepth() for x in self.children)

    def __str__(self, level=0):
        ret = "\t"*level+repr(self.value)+"\n"
        for child in self.children:
            ret += child.__str__(level+1)
        return ret



mytree = Node(1)
mytree.addChild(2)
mytree.addChild(3)
mytree.addChild(4)
mytree.getChildren()[0].addChild(5)
mytree.getChildren()[1].addChild(6)
mytree.getChildren()[1].addChild(7)
mytree.getChildren()[1].addChild(8)
mytree.getChildren()[2].addChild(7)
mytree.getChildren()[0].getChildren()[0].addChild(10)
print(mytree)
print("Depth:",  mytree.getDepth())