"""
Class Maze, grid (NxM)
"""

# Creat only the maze with  initially in each position
# 0 represents an open path
# 1 represents an obstacle
# 2 represents the initial point of the Robot
# 3 represents ship 1
# 4 represents ship 2
# 5 represents an item
# 5 represents an oil
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