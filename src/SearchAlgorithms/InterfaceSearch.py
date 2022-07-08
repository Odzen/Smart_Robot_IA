"""
Interface Search, here are methods that will be used for all the search algorithms
"""

#import sys
#sys.path.append("..") # Adds higher directory to python modules path.
from SearchAlgorithms.Node import Node
from Classes.Item import Item
from Classes.Ship import Ship
from Classes.Oil import Oil


class InterfaceSearch(object):
    def __init__(self, robot, firstShip, secondShip, items, oils, obstacles, mainMaze):
        self.firstShip = firstShip
        self.secondShip = secondShip
        self.oils = oils
        self.obstacles = obstacles
        self.mainMaze = mainMaze
        self.robot = robot
        self.items = items
        self.first_Goal = self.items[0].getItemPosition()
        self.second_Goal = self.items[1].getItemPosition()
        self.initialPosition = self.robot.getRobotPosition()
        self.nodeRoot = Node(None, self.initialPosition, 0, 0, None, robot)
        self.path = []
        self.itemsRecollected = []
        self.expanded_nodes = 0
        self.depth = 0

    def getFirst_Goal(self):
        return self.first_Goal

    def getSecond_Goal(self):
        return self.second_Goal

    def getDepth(self):
        return self.depth

    def setDepth(self, qty):
        self.depth = qty

    def getNodeRoot(self):
        return self.nodeRoot

    def getMaze(self):
        return self.maze

    def getExpandedNodes(self):
        return self.expanded_nodes

    def increaseByOneExpandedNodes(self):
        self.expanded_nodes += 1

    def getInitialPosition(self):
        return self.initialPosition

    def getPath(self):
        return self.path[::-1]

    def getItemsRecollected(self):
        if len(self.itemsRecollected) == 2:
            print("All Items Recollected!! \n")
        return self.itemsRecollected
    
    def getNumberItemsRecollected(self):
        return len(self.itemsRecollected)

    def getPositionItemsRecollected(self):
        positions = []
        for item in self.getItemsRecollected():
            position = item.getPosition()
            positions.append(position)
        return positions

    def isAllItemsRecollected(self):
        if len(self.itemsRecollected) == 2:
            return True
        else:
            return False

    def addPath(self, path):
        self.path.append(path)

    def findPath(self, node):
        currentNode = node
        tempPath = []
        while currentNode.getFather() != None:
            tempPath.append(currentNode.getOperator())
            currentNode = currentNode.getFather()
        return tempPath[::-1]

    # Aux function for method analizeMove()
    # If the current node is the root node
    def isRootNode(self, currentNode):
        if currentNode.getFather() == None:
            return True
        else:
            return False

    # Aux function for method analizeMove()
    # If the position where I want to move it's not the previous one
    def isPreviousOne(self, nextPosition, currentNode):
        if nextPosition != currentNode.getFather().getPosition():
            return True
        else:
            return False

    # Aux function for method analizeMove()
    # If the position is indeed the previous one, then: The move is allowed only if the robot just catched one of the items
    def justCatchedItem(self, currentNode):
        if currentNode.getPosition(
        ) == self.first_Goal or currentNode.getPosition() == self.second_Goal:
            return True
        else:
            return False

    # Aux function for method analizeMove()
    # If the position is indeed the previous one, then: The move is allowed only if the robot just catched one of the ships
    def justCatchedShip(self, currentNode):
        if currentNode.getPosition() == self.firstShip.getShipPosition(
        ) or currentNode.getPosition() == self.secondShip.getShipPosition():
            return True
        else:
            return False
    
    # Aux function that I use in other algorithms, since this class is inherited. I use this aux function in this class too, but at the end, it doesn't matter
    # because in the main algorithm 'getItems' I don't compare the costs
    def costNextMovement(self, nextPosition):
        cost = 1
        elementOnNextPosition = self.mainMaze.getElement(nextPosition)
        typeElement = type(elementOnNextPosition)

        # Item
        if (typeElement == Item):
            cost = 1

        # Oil
        if (typeElement == Oil):
            if self.firstShip.isRobotDriving(
            ) or self.secondShip.isRobotDriving():
                cost = 1
            else:
                cost = 4

        # Ship
        if (typeElement == Ship):
            cost = 1

        return cost

    def giveDirectionsRobot(self, path, anim):
        for operation in path:
            if operation == "Left":
                self.robot.moveLeft(self.firstShip, self.secondShip,
                                    self.items, self.oils)
                anim.update()
            elif operation == "Right":
                self.robot.moveRight(self.firstShip, self.secondShip,
                                     self.items, self.oils)
                anim.update()
            elif operation == "Down":
                self.robot.moveDown(self.firstShip, self.secondShip,
                                    self.items, self.oils)
                anim.update()
            elif operation == "Up":
                self.robot.moveUp(self.firstShip, self.secondShip, self.items,
                                  self.oils)
                anim.update()
        anim.done()

    def report(self, path):
        print("REPORT: ", "\n")
        print("Tree: \n", self.nodeRoot.subTreeCost(), "\n")
        print("Final Path: ", path)
        print("Tree Depth: ", self.getDepth())
        print("Nodes expanded: ", self.getExpandedNodes(), "\n")
