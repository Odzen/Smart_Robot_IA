"""
Class Item
"""

# Recieves a Maze and an initial position of the Item
class Item(object):
    def __init__(self, position, maze):
        self.position = position
        self.maze = maze
        self.state = True #True if the Item is still on the Maze, False if the Item was grabbed by the robot
    
    
    def getItemState(self):
        return self.state
    
    def setItemState(self):
        if self.state:
            self.state = False
    
    def getItemPosition(self):
        return self.position
        
    def __str__(self):
        return "There is an Item here ["+str(self.position.getX())+" , " + str(self.position.getY()) +  "]"     