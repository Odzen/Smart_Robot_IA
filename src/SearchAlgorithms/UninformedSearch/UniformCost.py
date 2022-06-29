"""
Uniform Cost
"""
from .BreadthFirst import Breadth_First
from ..Node import Node
import Classes.Maze
import Classes.Robot
from Classes.Position import Position
from Classes.Item import Item
from Classes.Ship import Ship
from Classes.Oil import Oil

class UniformCost (Breadth_First):

    def __init__(self, robot, firstShip, secondShip, items, oils, obstacles, mainMaze):
        super().__init__(robot, firstShip, secondShip, items, oils, obstacles, mainMaze)
        
    
    def costNextMovement(self, nextPosition):
        cost = 1
        elementOnNextPosition = self.mainMaze.getElement(nextPosition)
        typeElement = type(elementOnNextPosition)
        
        # Item
        if(typeElement == Item):
            cost = 1

        # Oil
        if(typeElement == Oil):
            if self.firstShip.isRobotDriving() or self.secondShip.isRobotDriving():
                cost = 1
            else:
                cost = 4
        
        # Ship
        if(typeElement == Ship):
            cost = 1
            
        return cost
    
    #Override
    def analizeMove(self, currentNode):
        if not self.robot.isObstacleUp(currentNode.getPosition()):
            positionUp = Position(currentNode.getPosition().getX() - 1, currentNode.getPosition().getY())
            
            if self.isRootNode(currentNode) or self.isPreviousOne(positionUp, currentNode)  or self.justCatchedItem(currentNode) or self.justCatchedShip(currentNode) :
                currentNode.addChild(positionUp, self.costNextMovement(positionUp), "Up")
                self.increaseByOneExpandedNodes()
                # Check and set depth
                self.setDepth(currentNode.getChildren()[0].getDepth())
                 
        if not self.robot.isObstacleDown(currentNode.getPosition()):
            positionDown = Position(currentNode.getPosition().getX() + 1, currentNode.getPosition().getY())
            
            if self.isRootNode(currentNode) or self.isPreviousOne(positionDown, currentNode)  or self.justCatchedItem(currentNode) or self.justCatchedShip(currentNode):
                currentNode.addChild(positionDown, self.costNextMovement(positionDown), "Down")
                self.increaseByOneExpandedNodes()
                # Check and set depth
                self.setDepth(currentNode.getChildren()[0].getDepth())
            
        if not self.robot.isObstacleOnLeft(currentNode.getPosition()):
            positionLeft = Position(currentNode.getPosition().getX() , currentNode.getPosition().getY() - 1)
            
            if self.isRootNode(currentNode) or self.isPreviousOne(positionLeft, currentNode)  or self.justCatchedItem(currentNode) or self.justCatchedShip(currentNode):
                 currentNode.addChild(positionLeft, self.costNextMovement(positionLeft), "Left")
                 self.increaseByOneExpandedNodes()
                 # Check and set depth
                 self.setDepth(currentNode.getChildren()[0].getDepth())
            
        if not self.robot.isObstacleOnRight(currentNode.getPosition()):
            positionRight = Position(currentNode.getPosition().getX() , currentNode.getPosition().getY() +1 )
            
            if self.isRootNode(currentNode) or self.isPreviousOne(positionRight, currentNode)  or self.justCatchedItem(currentNode) or self.justCatchedShip(currentNode):   
                currentNode.addChild(positionRight, self.costNextMovement(positionRight), "Right")
                self.increaseByOneExpandedNodes()
                # Check and set depth
                self.setDepth(currentNode.getChildren()[0].getDepth())
    
    #Override
    def getItems(self, initialNode):
        stack = []
        stack.append(initialNode)
        temp_First_goal = self.first_Goal
        temp_Second_goal = self.second_Goal
        while len(stack) != 0:
            stack.sort()
            currentNode = stack.pop(0)
            currentNode.analizeGoal(temp_First_goal, temp_Second_goal)
            
            if self.isAllItemsRecollected():
                return self.findPath(self.getItemsRecollected()[1])
            
            if currentNode.getIsGoal():
                print("Found one Item", currentNode, "\n")
                #self.setDepth(currentNode.getDepth() + self.getDepth())
                print("Path: ", self.findPath(currentNode), "\n")
                self.itemsRecollected.append(currentNode)
                stack = [] # Clean stack
                stack.append(currentNode) # Add current Node as root
                # Set the position of the found item, because the robot already grabbed the item, so this node is not longer a goal
                # I set them to (99,99), to no to interfer with the analizeGoal method 
                if temp_Second_goal in self.getPositionItemsRecollected():
                    temp_Second_goal = Position(99,99)
                elif temp_First_goal in self.getPositionItemsRecollected():
                    temp_First_goal = Position(99,99)
            
            else:
                self.analizeMove(currentNode)
                stack.extend(currentNode.getChildren())
    """
    #Override
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
                print("Tree: \n", initialNode.subTreeCost(), "\n")
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
    
    
    #Override
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

    """