"""
BFS - Breadth First Search
"""

import sys
sys.path.append("..") # Adds higher directory to python modules path.
from Node import Node
import Maze
import Robot
import Position


class Breadth_First (object):
    
    def __init__(self, robot, firstShip, secondShip, items, oils, obstacles, mainMaze):
        self.robot = robot
        self.first_Goal = items[0].getItemPosition()
        self.initialPosition = self.robot.getRobotPosition()
        self.nodeRoot = Node(None,self.initialPosition, 0, 0, None)
        self.path = []
    
    def first_Goal(self):
        return self.goal
    
    def getNodeRoot(self):
        return self.nodeRoot
    
    def getMaze(self):
        return self.maze
    
    def getInitialPosition(self):
        return self.initialPosition
    
    def getPath(self):
        return self.path
    
    def addOperation(self, operation):
        self.path.append(operation)
    
    def analizeMove(self, currentNode):
        if not self.robot.isObstacleUp(currentNode.getPosition()):
            positionUp = Position.Position(currentNode.getPosition().getX() - 1, currentNode.getPosition().getY())
            if currentNode.getFather() == None :  #root
                currentNode.addChild(positionUp, 1, "Up")
            elif positionUp != currentNode.getFather().getPosition(): #avoid turn back
                currentNode.addChild(positionUp, 1, "Up")
                currentNode.analizeGoal(self.first_Goal)
                 
        if not self.robot.isObstacleDown(currentNode.getPosition()):
            positionDown = Position.Position(currentNode.getPosition().getX() + 1, currentNode.getPosition().getY())
            if currentNode.getFather() == None: #root
                currentNode.addChild(positionDown, 1, "Down")
            elif positionDown != currentNode.getFather().getPosition(): #avoid turn back
                currentNode.addChild(positionDown, 1, "Down")
                currentNode.analizeGoal(self.first_Goal)
            
        if not self.robot.isObstacleOnLeft(currentNode.getPosition()):
            positionLeft = Position.Position(currentNode.getPosition().getX() , currentNode.getPosition().getY() - 1)
            if currentNode.getFather() == None : #root
                 currentNode.addChild(positionLeft, 1, "Left")
            elif positionLeft != currentNode.getFather().getPosition(): #avoid turn back
                 currentNode.addChild(positionLeft, 1, "Left")
                 currentNode.analizeGoal(self.first_Goal)
            
        if not self.robot.isObstacleOnRight(currentNode.getPosition()):
            positionRight = Position.Position(currentNode.getPosition().getX() , currentNode.getPosition().getY() +1 )
            if currentNode.getFather() == None : #root   
                currentNode.addChild(positionRight, 1, "Right")
            elif positionRight != currentNode.getFather().getPosition(): #avoid turn back
                 currentNode.addChild(positionRight, 1, "Right")
                 currentNode.analizeGoal(self.first_Goal)

    
    def constructTree(self):
        
        stack = []
        stack.append(self.nodeRoot)
        
        
        while len(stack) != 0:
            currentNode = stack.pop(0)
            #print("Current Node: ", currentNode)
            currentNode.analizeGoal(self.first_Goal)
            
            if currentNode.getIsGoal():
                print("Found Item", currentNode, "\n")
                print("Tree: \n", self.nodeRoot.subTree())
                return currentNode
            
            else:
                self.analizeMove(currentNode)
                stack.extend(currentNode.getChildren())
        
        

        

        
        
        

        
        
    

        
