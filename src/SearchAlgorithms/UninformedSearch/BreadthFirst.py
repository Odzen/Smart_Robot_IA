"""
BFS - Breadth First Search
"""

#import sys
#sys.path.append("..") # Adds higher directory to python modules path.
from typing import List
from Classes.Position import Position
from SearchAlgorithms.InterfaceSearch import InterfaceSearch 


class Breadth_First(InterfaceSearch):
    def __init__(self, robot, firstShip, secondShip, items, oils, obstacles, mainMaze):
        super().__init__(robot, firstShip, secondShip, items, oils, obstacles, mainMaze)
        
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
    
        if not self.robot.isObstacleOnLeft(currentNode.getPosition()):
            positionLeft = Position(currentNode.getPosition().getX(),currentNode.getPosition().getY() - 1)
            # If that checks --> root or avoid turn back
            print("ship: ", self.justCatchedShip(currentNode))
            print("item: ", self.justCatchedItem(currentNode))
            if self.isRootNode(currentNode) or self.isPreviousOne(positionLeft, currentNode) or self.justCatchedItem(currentNode) or self.justCatchedShip(currentNode):
                # I give the cost to the next movement to the child
                currentNode.addChild(positionLeft, 1, "Left", self.getNumberItemsRecollected(), self.firstShip , self.secondShip)
                self.increaseByOneExpandedNodes()
                # Check and set depth
                self.setDepth(currentNode.getChildren()[0].getDepth())

        if not self.robot.isObstacleOnRight(currentNode.getPosition()):
            positionRight = Position(currentNode.getPosition().getX(), currentNode.getPosition().getY() + 1)
            # If that checks --> root or avoid turn back
            print("ship: ", self.justCatchedShip(currentNode))
            print("item: ", self.justCatchedItem(currentNode))
            if self.isRootNode(currentNode) or self.isPreviousOne(positionRight, currentNode) or self.justCatchedItem(currentNode) or self.justCatchedShip(currentNode):
                # I give the cost to the next movement to the child
                currentNode.addChild(positionRight, 1 , "Right", self.getNumberItemsRecollected(), self.firstShip , self.secondShip)
                self.increaseByOneExpandedNodes()
                # Check and set depth
                self.setDepth(currentNode.getChildren()[0].getDepth())
                
        if not self.robot.isObstacleUp(currentNode.getPosition()):
            positionUp = Position(currentNode.getPosition().getX() - 1, currentNode.getPosition().getY())
            # If that checks --> root or avoid turn back
            print("ship: ", self.justCatchedShip(currentNode))
            print("item: ", self.justCatchedItem(currentNode))
            if self.isRootNode(currentNode) or self.isPreviousOne(positionUp, currentNode) or self.justCatchedItem(currentNode) or self.justCatchedShip(currentNode):
                # I give the cost to the next movement to the child
                currentNode.addChild(positionUp, 1 , "Up", self.getNumberItemsRecollected(), self.firstShip , self.secondShip)
                self.increaseByOneExpandedNodes()
                # Check and set depth
                self.setDepth(currentNode.getChildren()[0].getDepth())

        if not self.robot.isObstacleDown(currentNode.getPosition()):
            positionDown = Position(currentNode.getPosition().getX() + 1,currentNode.getPosition().getY())
            # If that checks --> root or avoid turn back
            print("ship: ", self.justCatchedShip(currentNode))
            print("item: ", self.justCatchedItem(currentNode))
            if self.isRootNode(currentNode) or self.isPreviousOne(positionDown, currentNode) or self.justCatchedItem(currentNode) or self.justCatchedShip(currentNode):
                # I give the cost to the next movement to the child
                currentNode.addChild(positionDown, 1 , "Down", self.getNumberItemsRecollected(), self.firstShip , self.secondShip)
                # Check and set depth
                self.setDepth(currentNode.getChildren()[0].getDepth())

    # MAIN algorithm
    def getItems(self):
        stack = []
        stack.append(self.nodeRoot)
        temp_First_goal = self.first_Goal
        temp_Second_goal = self.second_Goal
        while len(stack) != 0:
            currentNode = stack.pop(0)
            currentNode.analizeGoal(temp_First_goal, temp_Second_goal)
            
            # Check if the currentNode is a ship, so I set the ship to active
            # self.analizeShip(currentNode)
            
            # Check if the robot collected all the items
            if self.isAllItemsRecollected():
                return self.findPath(self.getItemsRecollected()[1]) # Gets the second element, because this is the final one. The first one [0] is the path to the first item founded

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
        path = self.getItems()
        return path
    

