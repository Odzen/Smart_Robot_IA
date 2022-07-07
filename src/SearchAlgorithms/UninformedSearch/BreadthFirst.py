"""
BFS - Breadth First Search
"""

#import sys
#sys.path.append("..") # Adds higher directory to python modules path.
from ..Node import Node
import Classes.Maze
import Classes.Robot
from Classes.Position import Position


class Breadth_First(object):
    def __init__(self, robot, firstShip, secondShip, items, oils, obstacles,
                 mainMaze):
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
        self.nodeRoot = Node(None, self.initialPosition, 0, 0, None)
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

    """
    Checks if there is an obstacle in any direction
    If not checks the following, using conjuntions
        1. If it is the root node -- isRootNode(self, currentNode)
        2. If the position where I want to move it's not the previous one -- isPreviousOne(self, nextPosition, currentNode)
        3. If the position is indeed the previous one, then: The move is allowed only if the robot just catched one of the items or ships in the previous move
            a. If the robot just grabbed one of the items, then it allows to turn back -- justCatchedItem(self, currentNode)
            b. If the robot just grabbed the one of the ships, then it allows to turn back -- justCatchedShip(self, currentNode)
            
    """

    def analizeMove(self, currentNode):
        if not self.robot.isObstacleUp(currentNode.getPosition()):
            positionUp = Position(currentNode.getPosition().getX() - 1,
                                  currentNode.getPosition().getY())
            # If that checks --> root or avoid turn back
            if self.isRootNode(currentNode) or self.isPreviousOne(
                    positionUp, currentNode) or self.justCatchedItem(
                        currentNode) or self.justCatchedShip(currentNode):
                currentNode.addChild(positionUp, 1, "Up")
                self.increaseByOneExpandedNodes()
                # Check and set depth
                self.setDepth(currentNode.getChildren()[0].getDepth())

        if not self.robot.isObstacleDown(currentNode.getPosition()):
            positionDown = Position(currentNode.getPosition().getX() + 1,
                                    currentNode.getPosition().getY())
            # If that checks --> root or avoid turn back
            if self.isRootNode(currentNode) or self.isPreviousOne(
                    positionDown, currentNode) or self.justCatchedItem(
                        currentNode) or self.justCatchedShip(currentNode):
                currentNode.addChild(positionDown, 1, "Down")
                self.increaseByOneExpandedNodes()
                # Check and set depth
                self.setDepth(currentNode.getChildren()[0].getDepth())

        if not self.robot.isObstacleOnLeft(currentNode.getPosition()):
            positionLeft = Position(currentNode.getPosition().getX(),
                                    currentNode.getPosition().getY() - 1)
            # If that checks --> root or avoid turn back
            if self.isRootNode(currentNode) or self.isPreviousOne(
                    positionLeft, currentNode) or self.justCatchedItem(
                        currentNode) or self.justCatchedShip(currentNode):
                currentNode.addChild(positionLeft, 1, "Left")
                self.increaseByOneExpandedNodes()
                # Check and set depth
                self.setDepth(currentNode.getChildren()[0].getDepth())

        if not self.robot.isObstacleOnRight(currentNode.getPosition()):
            positionRight = Position(currentNode.getPosition().getX(),
                                     currentNode.getPosition().getY() + 1)
            # If that checks --> root or avoid turn back
            if self.isRootNode(currentNode) or self.isPreviousOne(
                    positionRight, currentNode) or self.justCatchedItem(
                        currentNode) or self.justCatchedShip(currentNode):
                currentNode.addChild(positionRight, 1, "Right")
                self.increaseByOneExpandedNodes()
                # Check and set depth
                self.setDepth(currentNode.getChildren()[0].getDepth())

    def getItems(self, initialNode):
        stack = []
        stack.append(initialNode)
        temp_First_goal = self.first_Goal
        temp_Second_goal = self.second_Goal
        while len(stack) != 0:
            currentNode = stack.pop(0)
            currentNode.analizeGoal(temp_First_goal, temp_Second_goal)

            if self.isAllItemsRecollected():
                return self.findPath(self.getItemsRecollected()[1])

            if currentNode.getIsGoal():
                print("Found one Item", currentNode, "\n")
                #self.setDepth(currentNode.getDepth() + self.getDepth())
                print("Path: ", self.findPath(currentNode), "\n")
                self.itemsRecollected.append(currentNode)
                stack = []  # Clean stack
                stack.append(currentNode)  # Add current Node as root
                # Set the position of the found item, because the robot already grabbed the item, so this node is not longer a goal
                # I set them to (99,99), to no to interfer with the analizeGoal method
                if temp_Second_goal in self.getPositionItemsRecollected():
                    temp_Second_goal = Position(99, 99)
                elif temp_First_goal in self.getPositionItemsRecollected():
                    temp_First_goal = Position(99, 99)

            else:
                self.analizeMove(currentNode)
                stack.extend(currentNode.getChildren())

    def constructPath(self):
        path = self.getItems(self.nodeRoot)
        return path

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
