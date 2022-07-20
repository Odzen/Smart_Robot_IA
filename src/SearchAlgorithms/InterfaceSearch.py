"""
Interface Search, here are methods that will be used for all the search algorithms
"""

#import sys
#sys.path.append("..") # Adds higher directory to python modules path.
from SearchAlgorithms.Node import Node


class InterfaceSearch(object):
    def __init__(self, robot, firstShip, secondShip, items, oils, obstacles, mainMaze):
        self.firstShip = firstShip
        self.secondShip = secondShip
        self.firstShipPosition = self.firstShip.getShipPosition();
        self.secondShipPosition = self.secondShip.getShipPosition();
        self.oils = oils
        self.obstacles = obstacles
        self.mainMaze = mainMaze
        self.robot = robot
        self.items = items
        self.first_Goal = self.items[0].getItemPosition()
        self.second_Goal = self.items[1].getItemPosition()
        self.initialPosition = self.robot.getRobotPosition()
        self.nodeRoot = Node(None, self.initialPosition, 0, 0, None, 0, firstShip, secondShip)
        self.path = []
        self.itemsRecollected = []
        self.expanded_nodes = 0
        self.depth = 0
        self.time = 0

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

    def getTime(self):
        return self.time

    def setTime(self, new_time):
        self.time = new_time

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
        if currentNode.getPosition() == self.first_Goal or currentNode.getPosition() == self.second_Goal:
            return True
        else:
            return False

    # Aux function for method analizeMove()
    # If the position is indeed the previous one, then: The move is allowed only if the robot just catched one of the ships
    def justCatchedShip(self, currentNode):
        
        if currentNode.getPosition() == self.firstShipPosition or currentNode.getPosition() == self.secondShipPosition:
            #print("JUST CACTHED SHIP")
            return True
        else:
            return False
    
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
        # UNNCOMENT THIS LINE IF YOU WANT TO SEE THE TREE IN THE REPORT
        print("Tree: \n", self.nodeRoot.subTreeCost(), "\n")
        print("Final Path: ", path)
        print("Tree Depth: ", self.getDepth())
        print("Nodes expanded: ", self.getExpandedNodes(), "\n")
        print("Computation time : ", self.getTime(), "\n")
        return path, self.getDepth(), self.getExpandedNodes(), self.getTime()