"""
Uniform Cost
"""
from SearchAlgorithms.UninformedSearch.BreadthFirst import Breadth_First
from Classes.Position import Position
from Classes.Ship import Ship
from Classes.Item import Item
from Classes.Ship import Ship
from Classes.Oil import Oil


class UniformCost(Breadth_First):
    
    def __init__(self, robot, firstShip, secondShip, items, oils, obstacles, mainMaze):
        super().__init__(robot, firstShip, secondShip, items, oils, obstacles, mainMaze)
    
    # Aux function that I use in other algorithms, since this class is inherited. I use this aux function in this class too, but at the end, it doesn't matter
    # because in the main algorithm 'getItems' I don't compare the costs
    def costNextMovement(self, nextPosition, currentNode):
            
        cost = 1
        elementOnNextPosition = self.mainMaze.getElement(nextPosition)
        typeElement = type(elementOnNextPosition)

        # Item
        if (typeElement == Item):
            cost = 1

        # Oil
        if (typeElement == Oil):
            #print("Robot driving 1 shipt", self.firstShip.isRobotDriving())
            #print("Robot driving 2 ship", self.secondShip.isRobotDriving())
            if self.firstShip.isRobotDriving() or self.secondShip.isRobotDriving():
                cost = 1
            else:
                cost = 4
                
        # Ship
        if (typeElement == Ship):
            cost = 1
            
            if currentNode.analizeFirstShip() or currentNode.analizeSecondShip():
                if currentNode.analizeFirstShip():
                    currentNode.get_first_ship().setShipRobotDriving(True)
                if currentNode.analizeSecondShip():
                    currentNode.get_first_ship().setShipRobotDriving(True)
            

        return cost
    def analizeMove(self, currentNode):
        
        
        if not self.robot.isObstacleUp(currentNode.getPosition()):
            positionUp = Position(currentNode.getPosition().getX() - 1, currentNode.getPosition().getY())
            # If that checks --> root or avoid turn back
            if self.isRootNode(currentNode) or self.isPreviousOne(positionUp, currentNode) or self.justCatchedItem(currentNode) or self.justCatchedShip(currentNode):
                # I give the cost to the next movement to the child              
                currentNode.addChild(positionUp, self.costNextMovement(positionUp, currentNode) , "Up", self.getNumberItemsRecollected(),  currentNode.get_first_ship() , currentNode.get_second_ship())
                self.increaseByOneExpandedNodes()
                # Check and set depth
                self.setDepth(currentNode.getChildren()[0].getDepth())

        if not self.robot.isObstacleDown(currentNode.getPosition()):
            positionDown = Position(currentNode.getPosition().getX() + 1, currentNode.getPosition().getY())
            # If that checks --> root or avoid turn back
            if self.isRootNode(currentNode) or self.isPreviousOne(positionDown, currentNode) or self.justCatchedItem(currentNode) or self.justCatchedShip(currentNode):
                # I give the cost to the next movement to the child
                currentNode.addChild(positionDown, self.costNextMovement(positionDown, currentNode) , "Down", self.getNumberItemsRecollected(),  currentNode.get_first_ship(),currentNode.get_second_ship())
                # Check and set depth
                self.setDepth(currentNode.getChildren()[0].getDepth())

        if not self.robot.isObstacleOnLeft(currentNode.getPosition()):
            positionLeft = Position(currentNode.getPosition().getX(),currentNode.getPosition().getY() - 1)
            # If that checks --> root or avoid turn back
            if self.isRootNode(currentNode) or self.isPreviousOne(positionLeft, currentNode) or self.justCatchedItem(currentNode) or self.justCatchedShip(currentNode):
                # I give the cost to the next movement to the child
                currentNode.addChild(positionLeft, self.costNextMovement(positionLeft, currentNode) , "Left", self.getNumberItemsRecollected(),  currentNode.get_first_ship(),currentNode.get_second_ship())
                self.increaseByOneExpandedNodes()
                # Check and set depth
                self.setDepth(currentNode.getChildren()[0].getDepth())

        if not self.robot.isObstacleOnRight(currentNode.getPosition()):
            positionRight = Position(currentNode.getPosition().getX(), currentNode.getPosition().getY() + 1)
            # If that checks --> root or avoid turn back
            if self.isRootNode(currentNode) or self.isPreviousOne(positionRight, currentNode) or self.justCatchedItem(currentNode) or self.justCatchedShip(currentNode):
                # I give the cost to the next movement to the child
                currentNode.addChild(positionRight, self.costNextMovement(positionRight, currentNode) , "Right", self.getNumberItemsRecollected(),  currentNode.get_first_ship(), currentNode.get_second_ship())
                self.increaseByOneExpandedNodes()
                # Check and set depth
                self.setDepth(currentNode.getChildren()[0].getDepth())

    #Override, main algorithm
    # The only line that I change here is the sorting of the slack before getting the current node with pop. Here I use the cost for sorting
    def getItems(self):
        stack = []
        stack.append(self.nodeRoot)
        temp_First_goal = self.first_Goal
        temp_Second_goal = self.second_Goal
        while len(stack) != 0:
            stack.sort(key=lambda node: node.cost) # CHANGE HERE COMPARED TO SUPER -> I sort by cost, to get always the one with minor cost
            #stack.sort() # I can do it just like this as well, because of the __eq__ method on the Node class
            currentNode = stack.pop(0)
            currentNode.analizeGoal(temp_First_goal, temp_Second_goal)
            
            
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
        

"""

    if currentNode.getPosition() == self.firstShip.getShipPosition():
        self.firstShip.setShipRobotDriving(True)
    if currentNode.getPosition() == self.secondShip.getShipPosition():
        self.secondShip.setShipRobotDriving(True)
            
    if self.firstShip.isRobotDriving():
        self.firstShip.decreaseFuelByOne()
    elif self.secondShip.isRobotDriving():
        self.secondShip.decreaseFuelByOne()
                
                
"""

