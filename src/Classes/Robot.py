"""
Class for Smart Robot, simple agent
"""

#from .Maze import Maze
from .Position import Position 
from .Obstacle import Obstacle
from .Item import Item
from .Oil import Oil
from .Ship import Ship

# Recieves a Maze and an initial position of the Robot
class Robot1(object):
    def __init__(self, position, maze):
        self.maze = maze
        self.position = position
        self.foundItem = False
        self.collectedItems = 0
        #maze.setElement(position,2)
    
    def getRobotPosition(self):
        """
        Return the position of the robot.
        returns: a Position object giving the agent's position.
        """
        return self.position
    
    def getCollectedItems(self):
        return self.collectedItems
    
    def setCollectedItems(self, newItems):
        self.collectedItems = newItems
        
    def increaseByOneCollectedItems(self):
        self.collectedItems += 1
        
    def decreaseByOneCollectedItems(self):
        self.collectedItems -= 1
    
    def __str__(self):
        return "There is a Robot here: ["+str(self.position.getX())+" , " + str(self.position.getY()) +  "]"
    
    def hadfoundAllItems(self):
        if self.getCollectedItems() == 0:
            return True
        else:
            return False
    
    def isObstacleUp(self):
        nextPosition = Position(self.position.getX()-1, self.position.getY())
        typeNextPositionElement = type(self.maze.getElement(nextPosition))
        if(typeNextPositionElement == Obstacle or self.maze.getElement(nextPosition) == 7):
            return True
        else:
            return False
        
    def isObstacleDown(self):
        nextPosition = Position(self.position.getX()+1, self.position.getY())
        typeNextPositionElement = type(self.maze.getElement(nextPosition))
        if(typeNextPositionElement == Obstacle or self.maze.getElement(nextPosition) == 7):
            return True
        else:
            return False
        
    def isObstacleOnLeft(self):
        nextPosition = Position(self.position.getX(), self.position.getY()-1)
        typeNextPositionElement = type(self.maze.getElement(nextPosition))
        if(typeNextPositionElement == Obstacle or self.maze.getElement(nextPosition) == 7):
            return True
        else:
            return False
        
    def isObstacleOnRight(self):
        nextPosition = Position(self.position.getX(), self.position.getY()+1)
        typeNextPositionElement = type(self.maze.getElement(nextPosition))
        if(typeNextPositionElement == Obstacle or self.maze.getElement(nextPosition) == 7):
            return True
        else:
            return False
        
    def smellItem(self):
        lookUp = Position(self.position.getX()-1, self.position.getY())
        lookDown = Position(self.position.getX()+1, self.position.getY())
        lookRight = Position(self.position.getX(), self.position.getY()+1)
        lookLeft = Position(self.position.getX(), self.position.getY()-1)
        if(type(self.maze.getElement(lookRight)) == Item or type(self.maze.getElement(lookLeft)) == Item
           or type(self.maze.getElement(lookDown)) == Item or type(self.maze.getElement(lookUp)) == Item):
            return True
        else:
            return False
    
    def setAgentPosition(self, position):
        """
        Set the position of the robot to POSITION.
        position: a Position object.
        """
        #raise NotImplementedError
        self.position = position
        
    def moveLeft(self, firstShip, secondShip, items, oils):
        try:
            if(not(self.isObstacleOnLeft())):
                lookLeft = Position(self.position.getX(), self.position.getY()-1)
                elementOnLeft = self.maze.getElement(lookLeft)
                typeElement = type(elementOnLeft)
                
                # Got Item on Left
                if(typeElement == Item):
                    self.foundItem = True
                    self.increaseByOneCollectedItems()
                    
                    # If the robot grabbed the first Item
                    if items[0].getItemPosition() == lookLeft:
                        items[0].setItemState()
                    else: # If the robot grabbed the second Item
                        items[1].setItemState()
                    
                    # If the robot grabbed all the Items
                    if self.hadfoundAllItems():
                        print("Found All Items, Congrats!!")
                    else:# If the robot grabbed all the Items
                        print("Found One Item!!")

                # Passed Over Oil
                if(typeElement == Oil):
                    print(elementOnLeft)
                    elementOnLeft.setOilState()
                
                # Passed Over Ship
                if(typeElement == Ship):
                    print(elementOnLeft)
                    elementOnLeft.decreaseFuelByOne()
                    
                self.maze.setElement(self.position, 0) 
                newY = self.position.getY()-1
                newPosition = self.position.setPosition(self.position.getX() , newY)
                self.maze.setElement(newPosition, 2)
                self.setAgentPosition(newPosition)
                print("Moved Left")
                
                if(self.smellItem()):
                    print("Item close!")
            else:
                print("Cannot move, something on the left")
                
        except IndexError as error:
            print("Try again")
            raise Exception("Error: "+str(error))
    
    def moveUp(self, firstShip, secondShip, items, oils):
        try:
            if(not (self.isObstacleUp())):
                lookUp = Position(self.position.getX()-1, self.position.getY())
                elementUp = self.maze.getElement(lookUp)
                typeElement = type(elementUp)
                
                # Got Item Above
                if(typeElement == Item):
                    self.foundItem = True
                    self.increaseByOneCollectedItems()
                    
                    # If the robot grabbed the first Item
                    if items[0].getItemPosition() == lookUp:
                        items[0].setItemState()
                    else: # If the robot grabbed the second Item
                        items[1].setItemState()
                    
                    # If the robot grabbed all the Items
                    if self.hadfoundAllItems():
                        print("Found All Items, Congrats!!")
                    else:# If the robot grabbed all the Items
                        print("Found One Item!!")

                # Passed Over Oil
                if(typeElement == Oil):
                    print(elementUp)
                    elementUp.setOilState()
                
                # Passed Over Ship
                if(typeElement == Ship):
                    print(elementUp)
                    elementUp.decreaseFuelByOne()
                    
                self.maze.setElement(self.position, 0)
                newX = self.position.getX()-1
                newPosition = self.position.setPosition(newX , self.position.getY())
                self.maze.setElement(newPosition, 2)
                self.setAgentPosition(newPosition)
                print("Moved Up")
                
                if(self.smellItem()):
                    print("Item close!!")
            
            else:
                print("Cannot move, something Up")
                
        except IndexError as error:
            print("Try again")
            raise Exception("Error: "+str(error))
            
    def moveDown(self, firstShip, secondShip, items, oils):
        try:
            if(not(self.isObstacleDown())):
                lookDown = Position(self.position.getX()+1, self.position.getY())
                elementDown = self.maze.getElement(lookDown)
                typeElement = type(elementDown)
                
                # Got Item Below
                if(typeElement == Item):
                    self.foundItem = True
                    self.increaseByOneCollectedItems()
                    
                    # If the robot grabbed the first Item
                    if items[0].getItemPosition() == lookDown:
                        items[0].setItemState()
                    else: # If the robot grabbed the second Item
                        items[1].setItemState()
                    
                    # If the robot grabbed all the Items
                    if self.hadfoundAllItems():
                        print("Found All Items, Congrats!!")
                    else:# If the robot grabbed all the Items
                        print("Found One Item!!")

                # Passed Over Oil
                if(typeElement == Oil):
                    print(elementDown)
                    elementDown.setOilState()
                
                # Passed Over Ship
                if(typeElement == Ship):
                    print(elementDown)
                    elementDown.decreaseFuelByOne()
                    
                self.maze.setElement(self.position, 0)
                newX = self.position.getX()+1
                newPosition = self.position.setPosition(newX , self.position.getY())
                self.maze.setElement(newPosition, 2)
                self.setAgentPosition(newPosition)
                print("Moved Down")
                
                if(self.smellItem()):
                    print("Item close!!")
            else:
                print("Cannot move, something Down")
                
        except IndexError as error:
            print("Try again")
            raise Exception("Error: "+str(error))
            
    def moveRight(self, firstShip, secondShip, items, oils):
        try:
            if(not(self.isObstacleOnRight())):
                lookRight = Position(self.position.getX(), self.position.getY()+1)
                elementOnRight = self.maze.getElement(lookRight)
                typeElement = type(elementOnRight)
                
                # Got Item on Right
                if(typeElement == Item):
                    self.foundItem = True
                    self.increaseByOneCollectedItems()
                    
                    # If the robot grabbed the first Item
                    if items[0].getItemPosition() == lookRight:
                        items[0].setItemState()
                    else: # If the robot grabbed the second Item
                        items[1].setItemState()
                    
                    # If the robot grabbed all the Items
                    if self.hadfoundAllItems():
                        print("Found All Items, Congrats!!")
                    else:# If the robot grabbed all the Items
                        print("Found One Item!!")

                # Passed Over Oil
                if(typeElement == Oil):
                    print(elementOnRight)
                    elementOnRight.setOilState()
                
                # Passed Over Ship
                if(typeElement == Ship):
                    print(elementOnRight)
                    elementOnRight.decreaseFuelByOne()
                    
                self.maze.setElement(self.position, 0)
                newY = self.position.getY()+1
                newPosition = self.position.setPosition(self.position.getX() , newY)
                self.maze.setElement(newPosition, 2)
                self.setAgentPosition(newPosition)
                print("Moved Right")
                
                if(self.smellItem()):
                    print("Item close!!")
            else:
                print("Cannot move, something on the Right")

        except IndexError as error:
            print("Try again")
            raise Exception("Error: "+str(error))

"""        
# Agent saving the previous positions
class Robot2(Robot1):
    def __init__(self, position, maze):
        super().__init__(position, maze)
        self.previousX = position.getX()
        self.previousY = position.getY()
        self.previuosPositions = []
        self.mazePreviuousPositions = Maze(self.maze.getWidth(), self.maze.getHeight())
    
    def previousPosition(self):
        return "The Robot was here: ["+str(self.previousX)+" , " + str(self.previousY) +  "]"
    
    def getPreviousPositions(self):
        return self.previuosPositions
    
    def getMazePreviousPositions(self):
        return self.mazePreviuousPositions
    
    def addVisitedPosition(self, position):  
        point = (int(self.position.getX()), int(self.position.getY()))
        if point not in self.previuosPositions and self.mazePreviuousPositions.getElement(position) != 1:
            self.previuosPositions.append(point)
            self.mazePreviuousPositions.setElement(position, 1)

    
    def hadVisitedPosition(self,position):
        if self.mazePreviuousPositions.getElement(position) != 1 :
            return False
        else:
            return True
    
    def isUpperExplored(self):
        lookUp = Position(self.position.getX()-1, self.position.getY())
        if(self.hadVisitedPosition(lookUp)):
            return True
        else:
            return False
    
    def isLeftExplored(self):
        lookLeft = Position(self.position.getX(), self.position.getY()-1)
        if(self.hadVisitedPosition(lookLeft)):
            return True
        else:
            return False
    
    def isRightExplored(self):
        lookRight = Position(self.position.getX(), self.position.getY()+1)
        print(self.hadVisitedPosition(lookRight))
        if(self.hadVisitedPosition(lookRight)):
            return True
        else:
            return False
        
    def isDownExplored(self):
        lookDown = Position(self.position.getX()+1, self.position.getY())
        if(self.hadVisitedPosition(lookDown)):
            return True
        else:
            return False
    
    def moveLeft(self):
        if(not(self.isLeftExplored())):
            self.addVisitedPosition(self.position)
            super().moveLeft()
        else:
            print("Left position visited before")
            
    def moveUp(self):
        if(not(self.isUpperExplored())):
            self.addVisitedPosition(self.position)
            super().moveUp()
        else:
            print("Upper position visited before")

    def moveDown(self):
        if(not(self.isDownExplored())):
            self.addVisitedPosition(self.position)
            super().moveDown()
        else:
            print("Down position visited before")

    def moveRight(self):
        if(not(self.isRightExplored())):
            self.addVisitedPosition(self.position)
            super().moveRight()
        else:
            print("Right position visited before")
    
"""