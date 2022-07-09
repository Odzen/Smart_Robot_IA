"""
Uniform Cost
"""
from SearchAlgorithms.UninformedSearch.BreadthFirst import Breadth_First
from Classes.Position import Position
from Classes.Ship import Ship


class UniformCost(Breadth_First):
    
    def __init__(self, robot, firstShip, secondShip, items, oils, obstacles, mainMaze):
        super().__init__(robot, firstShip, secondShip, items, oils, obstacles, mainMaze)
    
    
    def analizeMove(self, currentNode):
        
        if self.firstShip.isRobotDriving():
            self.firstShip.decreaseFuelByOne()
        elif self.secondShip.isRobotDriving():
            self.secondShip.decreaseFuelByOne()
        
        
        if currentNode.getPosition() == self.firstShip.getShipPosition() and not  self.secondShip.isRobotDriving() and not  self.firstShip.isRobotDriving():
            self.firstShip.setShipRobotDriving(True)
        if currentNode.getPosition() == self.secondShip.getShipPosition()  and not  self.firstShip.isRobotDriving() and not  self.secondShip.isRobotDriving():
            self.secondShip.setShipRobotDriving(True)
        
        if not self.robot.isObstacleUp(currentNode.getPosition()):
            positionUp = Position(currentNode.getPosition().getX() - 1, currentNode.getPosition().getY())
            # If that checks --> root or avoid turn back
            if self.isRootNode(currentNode) or self.isPreviousOne(positionUp, currentNode) or self.justCatchedItem(currentNode) or self.justCatchedShip(currentNode):
                # I give the cost to the next movement to the child              
                currentNode.addChild(positionUp, self.costNextMovement(positionUp) , "Up", self.getNumberItemsRecollected(), self.firstShip , self.secondShip)
                self.increaseByOneExpandedNodes()
                # Check and set depth
                self.setDepth(currentNode.getChildren()[0].getDepth())

        if not self.robot.isObstacleDown(currentNode.getPosition()):
            positionDown = Position(currentNode.getPosition().getX() + 1, currentNode.getPosition().getY())
            # If that checks --> root or avoid turn back
            if self.isRootNode(currentNode) or self.isPreviousOne(positionDown, currentNode) or self.justCatchedItem(currentNode) or self.justCatchedShip(currentNode):
                # I give the cost to the next movement to the child
                currentNode.addChild(positionDown, self.costNextMovement(positionDown) , "Down", self.getNumberItemsRecollected(), self.firstShip, self.secondShip)
                # Check and set depth
                self.setDepth(currentNode.getChildren()[0].getDepth())

        if not self.robot.isObstacleOnLeft(currentNode.getPosition()):
            positionLeft = Position(currentNode.getPosition().getX(),currentNode.getPosition().getY() - 1)
            # If that checks --> root or avoid turn back
            if self.isRootNode(currentNode) or self.isPreviousOne(positionLeft, currentNode) or self.justCatchedItem(currentNode) or self.justCatchedShip(currentNode):
                # I give the cost to the next movement to the child
                currentNode.addChild(positionLeft, self.costNextMovement(positionLeft) , "Left", self.getNumberItemsRecollected(), self.firstShip, self.secondShip)
                self.increaseByOneExpandedNodes()
                # Check and set depth
                self.setDepth(currentNode.getChildren()[0].getDepth())

        if not self.robot.isObstacleOnRight(currentNode.getPosition()):
            positionRight = Position(currentNode.getPosition().getX(), currentNode.getPosition().getY() + 1)
            # If that checks --> root or avoid turn back
            if self.isRootNode(currentNode) or self.isPreviousOne(positionRight, currentNode) or self.justCatchedItem(currentNode) or self.justCatchedShip(currentNode):
                # I give the cost to the next movement to the child
                currentNode.addChild(positionRight, self.costNextMovement(positionRight) , "Right", self.getNumberItemsRecollected(), self.firstShip, self.secondShip)
                self.increaseByOneExpandedNodes()
                # Check and set depth
                self.setDepth(currentNode.getChildren()[0].getDepth())

    #Override, main algorithm
    # The only line that I change here is the sorting of the slack before getting the current node with pop. Here I use the cost for sorting
    def getItems(self, initialNode):
        stack = []
        stack.append(initialNode)
        temp_First_goal = self.first_Goal
        temp_Second_goal = self.second_Goal
        while len(stack) != 0:
            stack.sort(key=lambda node: node.cost) # CHANGE HERE COMPARED TO SUPER -> I sort by cost, to get always the one with minor cost
            #stack.sort() # I can do it just like this as well, because of the __eq__ method on the Node class
            currentNode = stack.pop(0)
            currentNode.analizeGoal(temp_First_goal, temp_Second_goal)
            
            
            print("Fuel 1:", self.firstShip.getFuel())
            print("Fuel 2:", self.secondShip.getFuel())
            
            
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
