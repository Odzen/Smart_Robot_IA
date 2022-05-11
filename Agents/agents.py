# -*- coding: utf-8 -*-
"""
Created on Sat Apr 23 23:13:36 2022

@author: Juan Sebastian Velasquez Acevedo
"""
class Position(object):
    """
    A Position represents a location in a two-dimensional room.
    """
    def __init__(self, x, y):
        """
        Initializes a position with coordinates (x, y).
        """
        self.x = x
        self.y = y
        
    def getX(self):
        return self.x
    
    def getY(self):
        return self.y
    
    def setPosition(self, x, y):
        """
        Computes and returns the new Position after a single clock-tick has
        passed, with this object as the current position, and with the
        specified angle and speed.

        Does NOT test whether the returned position fits inside the room.
        Returns: a Position object representing the new position.
        """
        old_x, old_y = self.getX(), self.getY()
        new_x = x
        new_y = y
        return Position(new_x, new_y)

    def __str__(self):  
        return  "(" + str(self.x) + "," +  str(self.y)  + ")"

# Creat only the maze with  initially in each position
# 0 represents an open path
# 1 represents an obstacle
# 2 represents an object Cheese
# 3 represents an object Mouse
class Maze(object):
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.maze = [ [0] * height for i in range(width)]
        self.OUT = 5
    
    def getWidth(self):
        return self.width
    
    def getHeight(self):
        return self.height
    
    def getNumCells(self):
        """
        Return the total number of cells in the maze.

        returns: an integer
        """
        return self.width * self.height
    
    def setElement(self, position, new_element):
        assert(type(position.getX()) == int and type(position.getY()) == int and type(new_element) == int)
        try:
            self.maze[position.getX()][position.getY()] = new_element
        except IndexError as error:
            print("Try again")
            raise Exception("Error: "+str(error))
    
    # 5 is a case when is trying to access to a position outside from the maze
    def getElement(self, position):
        if(position.getX() < 0 or position.getY() < 0):
            result = self.OUT
        else:
            assert(type(position.getX()) == int and type(position.getY()) == int)
            result = 1
            try:
                result = self.maze[position.getX()][position.getY()]
            except IndexError as e:
                result = self.OUT
        return result
    
    def isPositionInMaze(self, pos):
        """
        Return True if pos is inside the maze.
        pos: a Position object.
        returns: True if pos is in the maze, False otherwise.
        """
        #raise NotImplementedError
        if pos.x >= 0 and pos.x < self.width and pos.y >= 0 and pos.y < self.height:
            return True
        else:
            return False
            
    
    def __str__(self):
        string = ""
        for x in range(self.width):
            for y in range(self.height):
                string+= str(self.maze[x][y]) + "| "
            string+="\n"
        return string
            

# Recieves a Maze and an initial position of the Mouse
class MouseAgent1(object):
    def __init__(self, position, maze):
        self.maze = maze
        self.position = position
        maze.setElement(position,3)
        self.foundCheese = False
    
    def getRobotPosition(self):
        """
        Return the position of the agent.
        returns: a Position object giving the agent's position.
        """
        #raise NotImplementedError
        return self.position
    
    def __str__(self):
        return "The Mouse is here: ["+str(self.position.getX())+" , " + str(self.position.getY()) +  "]"
    
    def hadfoundCheese(self):
        return self.foundCheese
    
    def isSomethingUp(self):
        nextPosition = Position(self.position.getX()-1, self.position.getY())
        if(self.maze.getElement(nextPosition) == 1 or self.maze.getElement(nextPosition) == 5):
            return True
        else:
            return False
    def isSomethingDown(self):
        nextPosition = Position(self.position.getX()+1, self.position.getY())
        if(self.maze.getElement(nextPosition) ==1 or self.maze.getElement(nextPosition) == 5):
            return True
        else:
            return False
    def isSomethingOnLeft(self):
        nextPosition = Position(self.position.getX(), self.position.getY()-1)
        if(self.maze.getElement(nextPosition) == 1 or self.maze.getElement(nextPosition) == 5):
            #print("If:",self.maze.getElement(self.position.getX(), self.position.getY()-1))
            return True
        else:
            #print("Else:",self.maze.getElement(self.position.getX(), self.position.getY()-1))
            return False
    def isSomethingOnRight(self):
        nextPosition = Position(self.position.getX(), self.position.getY()+1)
        if(self.maze.getElement(nextPosition) == 1 or self.maze.getElement(nextPosition) == 5):
            return True
        else:
            return False
        
    def smellCheese(self):
        lookUp = Position(self.position.getX()-1, self.position.getY())
        lookDown = Position(self.position.getX()+1, self.position.getY())
        lookRight = Position(self.position.getX(), self.position.getY()+1)
        lookLeft = Position(self.position.getX(), self.position.getY()-1)
        if(self.maze.getElement(lookRight) == 2 or self.maze.getElement(lookLeft) == 2
           or self.maze.getElement(lookDown) == 2 or self.maze.getElement(lookUp) == 2):
            return True
        else:
            return False
    
    def setAgentPosition(self, position):
        """
        Set the position of the mouse to POSITION.
        position: a Position object.
        """
        #raise NotImplementedError
        self.position = position
        
    def moveLeft(self):
        try:
            if(not(self.isSomethingOnLeft())):
                lookLeft = Position(self.position.getX(), self.position.getY()-1)
                if(self.maze.getElement(lookLeft) == 2):
                    self.foundCheese = True
                    print("Found Cheese, Congrats!!")
                self.maze.setElement(self.position, 0) 
                newY = self.position.getY()-1
                newPosition = self.position.setPosition(self.position.getX() , newY)
                self.maze.setElement(newPosition, 3)
                self.setAgentPosition(newPosition)
                print("Moved Left")
                if(self.smellCheese()):
                    print("Cheese close!")
            else:
                print("Cannot move, something on the left")
        except IndexError as error:
            print("Try again")
            raise Exception("Error: "+str(error))
    
    def moveUp(self):
        try:
            if(not (self.isSomethingUp())):
                lookUp = Position(self.position.getX()-1, self.position.getY())
                if(self.maze.getElement(lookUp) == 2):
                    self.foundCheese = True
                    print("Found Cheese, Congrats!!")
                self.maze.setElement(self.position, 0)
                newX = self.position.getX()-1
                newPosition = self.position.setPosition(newX , self.position.getY())
                self.maze.setElement(newPosition, 3)
                self.setAgentPosition(newPosition)
                print("Moved Up")
                if(self.smellCheese()):
                    print("Cheese close!!")
            
            else:
                print("Cannot move, something Up")
                
        except IndexError as error:
            print("Try again")
            raise Exception("Error: "+str(error))
            
    def moveDown(self):
        try:
            if(not(self.isSomethingDown())):
                lookDown = Position(self.position.getX()+1, self.position.getY())
                if(self.maze.getElement(lookDown) == 2):
                    self.foundCheese = True
                    print("Found Cheese, Congrats!!")
                self.maze.setElement(self.position, 0)
                newX = self.position.getX()+1
                newPosition = self.position.setPosition(newX , self.position.getY())
                self.maze.setElement(newPosition, 3)
                self.setAgentPosition(newPosition)
                print("Moved Down")
                if(self.smellCheese()):
                    print("Cheese close!!")
            else:
                print("Cannot move, something Down")
                
        except IndexError as error:
            print("Try again")
            raise Exception("Error: "+str(error))
            
    def moveRight(self):
        try:
            if(not(self.isSomethingOnRight())):
                lookRight = Position(self.position.getX(), self.position.getY()+1)
                if(self.maze.getElement(lookRight) == 2):
                    self.foundCheese = True
                    print("Found Cheese, Congrats!!")
                self.maze.setElement(self.position, 0)
                newY = self.position.getY()+1
                newPosition = self.position.setPosition(self.position.getX() , newY)
                self.maze.setElement(newPosition, 3)
                self.setAgentPosition(newPosition)
                print("Moved Right")
                if(self.smellCheese()):
                    print("Cheese close!!")
            else:
                print("Cannot move, something on the Right")

        except IndexError as error:
            print("Try again")
            raise Exception("Error: "+str(error))
        

        
# Agent 1
class MouseAgent2(MouseAgent1):
    def __init__(self, position, maze):
        super().__init__(position, maze)
        self.previousX = position.getX()
        self.previousY = position.getY()
        self.previuosPositions = []
        self.mazePreviuousPositions = Maze(self.maze.getWidth(), self.maze.getHeight())
    
    def previousPosition(self):
        return "The Mouse was here: ["+str(self.previousX)+" , " + str(self.previousY) +  "]"
    
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
    


# Recieves a Maze and an initial position of the Cheese
class Cheese(object):
    def __init__(self, position, maze):
        self.position = position
        self.maze = maze
        maze.setElement(position,2)
        
    def __str__(self):
        return "The Cheese is here["+str(self.position.getX())+" , " + str(self.position.getY()) +  "]"             
               

        
    