import sys

sys.path.append("..")  # Adds higher directory to python modules path.

import Classes.Position
"""
Class Node


Valid Operators
 - right
 - left
 - up
 - down

Position in Maze (x,y)
"""


class Node(object):
    def __init__(self, father, position, depth, cost, operator):
        self.father = father
        self.position = position
        self.children = []
        self.depth = depth
        self.cost = cost
        self.operator = operator
        self.isGoal = False

    def getChildren(self):
        return self.children

    def getFather(self):
        return self.father

    def getPosition(self):
        return self.position

    def setPosition(self, position):
        self.position = position

    def getCost(self):
        return self.cost

    def getOperator(self):
        return self.operator

    def getDepth(self):
        return self.depth

    def getHeight(self):
        if not self.children:
            return 0
        else:
            return 1 + max(x.getDepth() for x in self.children)

    def analizeGoal(self, positionFirstItem, positionSecondItem):
        if positionFirstItem == self.position or positionSecondItem == self.position:
            self.isGoal = True
        else:
            self.isGoal = False

    def getIsGoal(self):
        return self.isGoal

    def setIsGoal(self):
        if self.isGoal:
            self.isGoal = False
        else:
            self.isGoal = True

    def addChild(self, position, costChild, operator):
        newChildren = Node(self, position, self.depth + 1,
                           self.cost + costChild, operator)
        self.children.append(newChildren)
        return newChildren

    def __str__(self):
        return "Node at the position: " + str(self.position)

    def subTreePositions(self, level=0):
        """
        Prints the subTree formed below the node
        """
        if self.isGoal:
            ret = "\t" * level + repr(str(self.position)) + "* " + (str(
                self.operator)) + "\n"
        else:
            ret = "\t" * level + repr(str(self.position)) + " " + (str(
                self.operator)) + "\n"
        for child in self.children:
            ret += child.subTreePositions(level + 1)
        return ret

    def subTreeCost(self, level=0):
        """
        Prints the subTree formed below the node
        """
        if self.isGoal:
            ret = "\t" * level + repr(str(self.position)) + "* " + (str(
                self.operator)) + "-- Cost:" + str(self.cost) + "\n"
        else:
            ret = "\t" * level + repr(str(self.position)) + " " + (str(
                self.operator)) + "-- Cost:" + str(self.cost) + "\n"
        for child in self.children:
            ret += child.subTreeCost(level + 1)
        return ret

    def printDepth(self):
        print("Node Depth: ", self.depth)

    def printOperator(self):
        print("The operator to get to this node was: ", self.operator)

    def __gt__(self, other):
        if isinstance(other, Node):
            if self.cost > other.cost:
                return True
            if self.cost < other.cost:
                return False


"""

# TESTS ---

# ROOT
rootNode = Node(None,Position.Position(1, 1), 0, 0, None)
#GOAL
goalPosition = Position.Position(6, 6)
rootNode.analizeGoal(goalPosition)

#CHILDREN
# The childs only need a position, value, cost and operator
child1 = rootNode.addChild(Position.Position(2, 2), 1, "left")
child2 = rootNode.addChild(Position.Position(3, 3), 1, "left")
child3 = rootNode.addChild(Position.Position(4, 4), 1, "left")

#GRANDCHILDREN
grand1 = child1.addChild(Position.Position(5, 5), 1, "left")
grand2 = child1.addChild(Position.Position(6, 6), 1, "left")
grand2.analizeGoal(goalPosition)
grand3 = child1.addChild(Position.Position(7, 7), 1, "left")


grand4 = child2.addChild(Position.Position(8, 8), 1, "left")
grand5 = child2.addChild(Position.Position(9, 9), 1, "left")
grand6 = child2.addChild(Position.Position(10, 10), 1, "left")


grand7 = child3.addChild(Position.Position(11, 11), 1, "left")
grand8 = child3.addChild(Position.Position(12, 12), 1, "left")

# Checking Positions and Familia
print(rootNode) # Should be (1,1)
print(rootNode.getFather()) # Should be None
print(child3.getFather()) # Should be (1,1)
print(grand5.getFather()) # Should be (3,3)
print(grand8.getFather()) # Should be (4,4)

# Checking Depths
rootNode.printDepth() # 0

child1.printDepth() # 1
child2.printDepth() # 1
child3.printDepth() # 1

grand4.printDepth() # 2
grand5.printDepth() # 2
grand6.printDepth() # 2
grand7.printDepth() # 2
grand8.printDepth() # 2

# Checking Costs, taking into account that every move costs 1
print(rootNode.getCost())
print(child1.getCost())
print(grand7.getCost())

# Family Tree
print(rootNode.subTree())

"""
