"""
Class OpenCell
"""


# Recieves a Maze and an initial position of the Oil
class OpenCell(object):
    def __init__(self, position, maze):
        self.position = position
        self.maze = maze
        self.cost = 1
        #maze.setElement(position,6)

    def getCost(self):
        return self.cost

    def __str__(self):
        return "There is an Open Cell here [" + str(
            self.position.getX()) + " , " + str(self.position.getY()) + "]"
