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
            elif positionUp != currentNode.getFather().getPosition(): #avoid turn back
                currentNode.addChild(positionUp, 1, "Up")
                self.increaseByOneExpandedNodes()
                 
        if not self.robot.isObstacleDown(currentNode.getPosition()):
            positionDown = Position(currentNode.getPosition().getX() + 1, currentNode.getPosition().getY())
            if currentNode.getFather() == None: #root
                currentNode.addChild(positionDown, 1, "Down")
                self.increaseByOneExpandedNodes()
            elif positionDown != currentNode.getFather().getPosition(): #avoid turn back
                currentNode.addChild(positionDown, 1, "Down")
                self.increaseByOneExpandedNodes()
            
        if not self.robot.isObstacleOnLeft(currentNode.getPosition()):
            positionLeft = Position(currentNode.getPosition().getX() , currentNode.getPosition().getY() - 1)
            if currentNode.getFather() == None : #root
                 currentNode.addChild(positionLeft, 1, "Left")
                 self.increaseByOneExpandedNodes()
            elif positionLeft != currentNode.getFather().getPosition(): #avoid turn back
                currentNode.addChild(positionLeft, 1, "Left")
                self.increaseByOneExpandedNodes()
            
        if not self.robot.isObstacleOnRight(currentNode.getPosition()):
            positionRight = Position(currentNode.getPosition().getX() , currentNode.getPosition().getY() +1 )
            if currentNode.getFather() == None : #root   
                currentNode.addChild(positionRight, 1, "Right")
                self.increaseByOneExpandedNodes()
            elif positionRight != currentNode.getFather().getPosition(): #avoid turn back
                 currentNode.addChild(positionRight, 1, "Right")
                 self.increaseByOneExpandedNodes()
                 
    def getOneItem(self, initialNode):
        stack = []
        stack.append(initialNode)
        while len(stack) != 0:
            currentNode = stack.pop(0)
            
            if self.second_Goal in self.itemsRecollected:
                currentNode.analizeGoal(self.first_Goal)
            elif self.first_Goal in self.itemsRecollected:
                currentNode.analizeGoal(self.second_Goal)
            else:
                currentNode.analizeGoal(self.first_Goal)
                currentNode.analizeGoal(self.second_Goal)
                
            if currentNode.getIsGoal():
                print("Found one Item", currentNode, "\n")
                print("Tree: \n", initialNode.subTree(), "\n")
                currentNode.setIsGoal()
                print("Nodes expanded: ", self.getExpandedNodes(), "\n") # Mistake, it is counting all the nodes except for the goal!!
                self.setDepth(currentNode.getDepth() + self.getDepth())
                print("Tree Depth: ", self.getDepth()) # Mistake, it is coundting all the nodes until the goal, but not the deeper ones!!
                print("Path: ", self.findPath(currentNode), "\n")
                return currentNode, self.findPath(currentNode)
            
            
            else:
                self.analizeMove(currentNode)
                stack.extend(currentNode.getChildren())
                
        print("The stack is = 0")

    
    def constructTree(self):
        
        initialNode = self.nodeRoot
        first_node_goal, path1 = self.getOneItem(initialNode)
        self.itemsRecollected.append(first_node_goal.getPosition())
        newRoot = Node(None, first_node_goal.getPosition(), 0, 0, first_node_goal.getOperator()) # newRoot because if it keeps the father, there is not any possible move
        

        second_node_goal, path2 = self.getOneItem(newRoot)
        self.itemsRecollected.append(second_node_goal.getPosition())
        
        self.getItemsRecollected()
        self.addPath(path2)
        self.addPath(path1)
        print("Final Path: ", self.getPath())
        
        return self.getPath()
    
    def giveDirectionsRobot(self, paths, anim):
        for path in paths:
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
                    
   
        

        
        
    

        
