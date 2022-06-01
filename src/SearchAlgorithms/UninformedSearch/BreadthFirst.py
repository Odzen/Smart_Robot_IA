"""
BFS - Breadth First Search
"""

import sys
sys.path.append("..") # Adds higher directory to python modules path.
from ..Node import Node
import Maze
import Robot
import Position


class Breadth_First (object):
    
    def __init__(self, robot, firstShip, secondShip, items, oils, obstacles, mainMaze):
        self.robot = robot
        self.first_Goal = items[0].getItemPosition()
        self.second_Goal = items[1].getItemPosition()
        self.initialPosition = self.robot.getRobotPosition()
        self.nodeRoot = Node(None,self.initialPosition, 0, 0, None)
        self.path = []
        self.itemsRecollected = []
    
    def first_Goal(self):
        return self.goal
    
    def second_Goal(self):
        return self.goal
    
    def getNodeRoot(self):
        return self.nodeRoot
    
    def getMaze(self):
        return self.maze
    
    def getInitialPosition(self):
        return self.initialPosition
    
    def getPath(self):
        return self.path

    def getItemsRecollected(self):
        if len (self.itemsRecollected) == 2:
            print("All Items Recollected!!")
        return self.itemsRecollected
    
    def addOperation(self, operation):
        self.path.append(operation)
    
    def analizeMove(self, currentNode):
        if not self.robot.isObstacleUp(currentNode.getPosition()):
            positionUp = Position.Position(currentNode.getPosition().getX() - 1, currentNode.getPosition().getY())
            if currentNode.getFather() == None :  #root
                currentNode.addChild(positionUp, 1, "Up")
            elif positionUp != currentNode.getFather().getPosition(): #avoid turn back
                currentNode.addChild(positionUp, 1, "Up")
                 
        if not self.robot.isObstacleDown(currentNode.getPosition()):
            positionDown = Position.Position(currentNode.getPosition().getX() + 1, currentNode.getPosition().getY())
            if currentNode.getFather() == None: #root
                currentNode.addChild(positionDown, 1, "Down")
            elif positionDown != currentNode.getFather().getPosition(): #avoid turn back
                currentNode.addChild(positionDown, 1, "Down")
            
        if not self.robot.isObstacleOnLeft(currentNode.getPosition()):
            positionLeft = Position.Position(currentNode.getPosition().getX() , currentNode.getPosition().getY() - 1)
            if currentNode.getFather() == None : #root
                 currentNode.addChild(positionLeft, 1, "Left")
            elif positionLeft != currentNode.getFather().getPosition(): #avoid turn back
                currentNode.addChild(positionLeft, 1, "Left")
            
        if not self.robot.isObstacleOnRight(currentNode.getPosition()):
            positionRight = Position.Position(currentNode.getPosition().getX() , currentNode.getPosition().getY() +1 )
            if currentNode.getFather() == None : #root   
                currentNode.addChild(positionRight, 1, "Right")
            elif positionRight != currentNode.getFather().getPosition(): #avoid turn back
                 currentNode.addChild(positionRight, 1, "Right")
                 
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
                #stackItems.append(currentNode)
                print("Tree: \n", initialNode.subTree(), "\n")
                currentNode.setIsGoal()
                return currentNode
            
            
            else:
                self.analizeMove(currentNode)
                stack.extend(currentNode.getChildren())
                
        print("The stack is = 0")

    
    def constructTree(self):
        
        initialNode = self.nodeRoot
        first_node_goal = self.getOneItem(initialNode)
        self.itemsRecollected.append(first_node_goal.getPosition())
        newRoot = Node(None, first_node_goal.getPosition(), 0, 0, first_node_goal.getOperator())
        

        second_node_goal = self.getOneItem(newRoot)
        self.itemsRecollected.append(second_node_goal.getPosition())
        
        self.getItemsRecollected()
        
        

        
        
    

        
