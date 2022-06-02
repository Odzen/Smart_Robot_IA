"""
Class Maze, grid (NxM)
"""

from .Item import Item
from .Oil import Oil
from .Robot import *
from .Obstacle import Obstacle
from .OpenCell import OpenCell
from .Ship import Ship
from .Position import Position 



# Creat only the maze with  initially in each position
# 0 represents an open path
# 1 represents an obstacle
# 2 represents the initial point of the Robot
# 3 represents ship 1
# 4 represents ship 2
# 5 represents an item
# 6 represents an oil
class Maze(object):
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.maze = [ [0] * height for i in range(width)]
        self.OUT = 7
    
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
    
    # 7 is a case when is trying to access to a position outside from the maze
    def getElement(self, position):
        if(position.getX() < 0 or position.getY() < 0):
            return self.OUT
        else:
            assert(type(position.getX()) == int and type(position.getY()) == int)
            try:
                numberPosition = self.maze[position.getX()][position.getY()]
                if( numberPosition == 0):
                    return OpenCell(position, self)
                if( numberPosition == 1):
                    return Obstacle(position, self)
                if( numberPosition == 2):
                    return Robot1(position, self)
                    #return Robot2(position, self)
                if( numberPosition == 3):
                    return Ship(position, self, 10)
                if( numberPosition == 4):
                    return Ship(position, self, 20)
                if( numberPosition == 5):
                    return Item(position, self)
                if( numberPosition == 6):
                    return Oil(position, self)
                
            # If I'm looking outside of the Maze
            except IndexError as e:
                return self.OUT
    
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