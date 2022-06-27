"""
BFS - Breadth First Search
"""

#import sys
#sys.path.append("..") # Adds higher directory to python modules path.
from ..Node import Node
import Classes.Maze
import Classes.Robot
from Classes.Position import Position


class Breadth_First (object):
    
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
        self.nodeRoot = Node(None,self.initialPosition, 0, 0, None)
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
        if len (self.itemsRecollected) == 2:
            print("All Items Recollected!! \n")
        return self.itemsRecollected
    
    def getPositionItemsRecollected(self):
        positions = []
        for item in self.getItemsRecollected():
            position = item.getPosition()
            positions.append(position)
        return positions
            
    
    def isAllItemsRecollected(self):
        if len (self.itemsRecollected) == 2:
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
        
    
    def analizeMove(self, currentNode):
        if not self.robot.isObstacleUp(currentNode.getPosition()):
            positionUp = Position(currentNode.getPosition().getX() - 1, currentNode.getPosition().getY())
            if currentNode.getFather() == None :  #root
                currentNode.addChild(positionUp, 1, "Up")
                self.increaseByOneExpandedNodes()
            elif positionUp != currentNode.getFather().getPosition()  or (currentNode.getPosition() == self.first_Goal or  currentNode.getPosition() == self.second_Goal): #avoid turn back
                currentNode.addChild(positionUp, 1, "Up")
                self.increaseByOneExpandedNodes()
                 
        if not self.robot.isObstacleDown(currentNode.getPosition()):
            positionDown = Position(currentNode.getPosition().getX() + 1, currentNode.getPosition().getY())
            if currentNode.getFather() == None: #root
                currentNode.addChild(positionDown, 1, "Down")
                self.increaseByOneExpandedNodes()
            elif positionDown != currentNode.getFather().getPosition() or (currentNode.getPosition()== self.first_Goal or  currentNode.getPosition() == self.second_Goal): #avoid turn back
                currentNode.addChild(positionDown, 1, "Down")
                self.increaseByOneExpandedNodes()
            
        if not self.robot.isObstacleOnLeft(currentNode.getPosition()):
            positionLeft = Position(currentNode.getPosition().getX() , currentNode.getPosition().getY() - 1)
            if currentNode.getFather() == None : #root
                 currentNode.addChild(positionLeft, 1, "Left")
                 self.increaseByOneExpandedNodes()
            elif positionLeft != currentNode.getFather().getPosition() or (currentNode.getPosition() == self.first_Goal or  currentNode.getPosition() == self.second_Goal): #avoid turn back
                currentNode.addChild(positionLeft, 1, "Left")
                self.increaseByOneExpandedNodes()
            
        if not self.robot.isObstacleOnRight(currentNode.getPosition()):
            positionRight = Position(currentNode.getPosition().getX() , currentNode.getPosition().getY() +1 )
            if currentNode.getFather() == None : #root   
                currentNode.addChild(positionRight, 1, "Right")
                self.increaseByOneExpandedNodes()
            elif positionRight != currentNode.getFather().getPosition() or (currentNode.getPosition() == self.first_Goal or  currentNode.getPosition() == self.second_Goal): #avoid turn back
                 currentNode.addChild(positionRight, 1, "Right")
                 self.increaseByOneExpandedNodes()
                 
    def getItems(self, initialNode):
        stack = []
        stack.append(initialNode)
        while len(stack) != 0:
            currentNode = stack.pop(0)
            print(currentNode)
            currentNode.analizeGoal(self.first_Goal, self.second_Goal)
            
            if self.isAllItemsRecollected():
                print("Tree Depth: ", self.getDepth()) # Mistake, it is coundting all the nodes until the goal, but not the deeper ones!!
                print("Nodes expanded: ", self.getExpandedNodes(), "\n") # Mistake, it is counting all the nodes except for the goal!!
                print("Tree: \n", initialNode.subTreePositions(), "\n")
                print(self.getItemsRecollected())
            
                return self.findPath(self.getItemsRecollected()[1])
            
                
            if currentNode.getIsGoal():
                print("Found one Item", currentNode, "\n")
                self.setDepth(currentNode.getDepth() + self.getDepth())
                print("Path: ", self.findPath(currentNode), "\n")
                self.itemsRecollected.append(currentNode)
                stack = []
                stack.append(currentNode)
                # Set the position of the found item, because the robot already grabbed the item, so this node is not longer a goal
                if self.second_Goal in self.getPositionItemsRecollected():
                    self.second_Goal = Position(99,99)
                elif self.first_Goal in self.getPositionItemsRecollected():
                    self.first_Goal = Position(99,99)
            
            else:
                self.analizeMove(currentNode)
                stack.extend(currentNode.getChildren())
            
                
        print("The stack is = 0")

    
    # TODO -- Fix this, and construct just one tree    
    def constructTree(self):
        initialNode = self.nodeRoot
        path = self.getItems(initialNode)
        print("Final Path: ", path)
        
        return path
    
    def giveDirectionsRobot(self, path, anim):
        for operation in path:
            if operation == "Left":
                self.robot.moveLeft(self.firstShip, self.secondShip, self.items, self.oils)
                anim.update()
            elif operation == "Right":
                self.robot.moveRight(self.firstShip, self.secondShip, self.items, self.oils)
                anim.update()
            elif operation == "Down":
                self.robot.moveDown(self.firstShip, self.secondShip, self.items, self.oils)
                anim.update()
            elif operation == "Up":
                self.robot.moveUp(self.firstShip, self.secondShip, self.items, self.oils)
                anim.update()
        anim.done()
                    
   
        

        
        
    

        
