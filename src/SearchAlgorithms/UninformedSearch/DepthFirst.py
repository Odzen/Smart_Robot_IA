"""
Depth First algorithm
"""
from SearchAlgorithms.InterfaceSearch import InterfaceSearch 
from Classes.Position import Position


class DepthFirst(InterfaceSearch):
    def __init__(self, robot, firstShip, secondShip, items, oils, obstacles,
                 mainMaze):
        super().__init__(robot, firstShip, secondShip, items, oils, obstacles,
                         mainMaze)

    #Override
    def analizeMove(self, currentNode):
        
        if not self.robot.isObstacleUp(currentNode.getPosition()):
            positionUp = Position(currentNode.getPosition().getX() - 1,currentNode.getPosition().getY())
            # If that checks --> root or avoid turn back
            if self.isRootNode(currentNode) or self.isPreviousOne(positionUp, currentNode) or self.justCatchedItem(currentNode) or self.justCatchedShip(currentNode):
                # CHANGE HERE COMPARED TO SUPER -> Extra condition that checks if the node was visited, this helps to avoid infinite loops
                if not self.wasVisited(currentNode):
                    # I give the cost to the next movement to the child
                    currentNode.addChild(positionUp, 1, "Up", self.getNumberItemsRecollected(), self.firstShip , self.secondShip)
                    self.increaseByOneExpandedNodes()
                    # Check and set depth
                    self.setDepth(currentNode.getChildren()[0].getDepth())

        if not self.robot.isObstacleDown(currentNode.getPosition()):
            positionDown = Position(currentNode.getPosition().getX() + 1,currentNode.getPosition().getY())
            # If that checks --> root or avoid turn back
            if self.isRootNode(currentNode) or self.isPreviousOne(positionDown, currentNode) or self.justCatchedItem(currentNode) or self.justCatchedShip(currentNode):
                # CHANGE HERE COMPARED TO SUPER -> Extra condition that checks if the node was visited, this helps to avoid infinite loops
                if not self.wasVisited(currentNode):
                    # I give the cost to the next movement to the child
                    currentNode.addChild(positionDown,  1, "Down", self.getNumberItemsRecollected(), self.firstShip , self.secondShip)
                    self.increaseByOneExpandedNodes()
                    # Check and set depth
                    self.setDepth(currentNode.getChildren()[0].getDepth())
        
        
        if not self.robot.isObstacleOnLeft(currentNode.getPosition()):
            positionLeft = Position(currentNode.getPosition().getX(),currentNode.getPosition().getY() - 1)
            # If that checks --> root or avoid turn back
            if self.isRootNode(currentNode) or self.isPreviousOne(positionLeft, currentNode) or self.justCatchedItem(currentNode) or self.justCatchedShip(currentNode):
                # CHANGE HERE COMPARED TO SUPER -> Extra condition that checks if the node was visited, this helps to avoid infinite loops
                if not self.wasVisited(currentNode):
                    # I give the cost to the next movement to the child
                    currentNode.addChild(positionLeft, 1 , "Left", self.getNumberItemsRecollected(), self.firstShip , self.secondShip)
                    self.increaseByOneExpandedNodes()
                    # Check and set depth
                    self.setDepth(currentNode.getChildren()[0].getDepth())
                    
        if not self.robot.isObstacleOnRight(currentNode.getPosition()):
            positionRight = Position(currentNode.getPosition().getX(), currentNode.getPosition().getY() + 1)
            # If that checks --> root or avoid turn back
            if self.isRootNode(currentNode) or self.isPreviousOne(positionRight, currentNode) or self.justCatchedItem(currentNode) or self.justCatchedShip(currentNode):
                # CHANGE HERE COMPARED TO SUPER -> Extra condition that checks if the node was visited, this helps to avoid infinite loops
                if not self.wasVisited(currentNode):
                    # I give the cost to the next movement to the child
                    currentNode.addChild(positionRight, 1 , "Right", self.getNumberItemsRecollected(), self.firstShip , self.secondShip)
                    self.increaseByOneExpandedNodes()
                    # Check and set depth
                    self.setDepth(currentNode.getChildren()[0].getDepth())

    def wasVisited(self, currentNode):
        father_node = currentNode.getFather()
        while father_node != None:
            #print("Items in this node,", str(currentNode), "are: ", currentNode.getStateItems())
            #print("Items in its father node,", str(father_node), "are: ", father_node.getStateItems())
            if (currentNode.position == father_node.position) and (currentNode.getStateItems() == father_node.getStateItems()):
                print("Was visited")
                return True
            father_node = father_node.getFather()
        print("Was NOT visited")
        return False
    
    
    #Override, main algorithm
    def getItems(self):
        stack = []
        stack.append(self.nodeRoot)
        temp_First_goal = self.first_Goal
        temp_Second_goal = self.second_Goal
        while len(stack) != 0:
            currentNode = stack.pop(0)
            currentNode.analizeGoal(temp_First_goal, temp_Second_goal)
            
            if self.isAllItemsRecollected():
                print(self.getItemsRecollected())
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
                stack = currentNode.getChildren() + stack # CHANGE HERE COMPARED TO SUPER -> Insert children on front to follow the Depth First dynamic
                
    def constructPath(self):
        path = self.getItems()
        return path