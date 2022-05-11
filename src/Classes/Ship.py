"""
Class Ship
"""

# Recieves a Maze and an initial position of the Ship
class Ship(object):
    def __init__(self, position, maze):
        self.position = position
        self.maze = maze
        maze.setElement(position,2)
        
    def __str__(self):
        return "The Ship is here["+str(self.position.getX())+" , " + str(self.position.getY()) +  "]"     