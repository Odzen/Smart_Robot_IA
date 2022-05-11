"""
Class Oil
"""

# Recieves a Maze and an initial position of the Oil
class Oil(object):
    def __init__(self, position, maze):
        self.position = position
        self.maze = maze
        maze.setElement(position,2)
        
    def __str__(self):
        return "The Oil is here["+str(self.position.getX())+" , " + str(self.position.getY()) +  "]"     