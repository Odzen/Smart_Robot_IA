"""
Class Obstacle
"""

# Recieves a Maze and an initial position of the Obstacle
class Obstacle(object):
    def __init__(self, position, maze):
        self.position = position
        self.maze = maze
        
    def __str__(self):
        return "The Obstacle is here["+str(self.position.getX())+" , " + str(self.position.getY()) +  "]"     
