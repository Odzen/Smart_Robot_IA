"""
Class Item
"""

# Recieves a Maze and an initial position of the Item
class Item(object):
    def __init__(self, position, maze):
        self.position = position
        self.maze = maze
        #maze.setElement(position,5)
    
    def getItemPosition(self):
        return self.position
        
    def __str__(self):
        return "There is an Item here ["+str(self.position.getX())+" , " + str(self.position.getY()) +  "]"     