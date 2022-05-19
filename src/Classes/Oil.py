"""
Class Oil
"""

# Recieves a Maze and an initial position of the Oil
class Oil(object):
    def __init__(self, position, maze):
        self.position = position
        self.maze = maze
        self.cost = 4
    
    def getCost(self):
        return self.cost
    
    def getOilPosition(self):
        return self.position
    
    # Call this function to set the cost, for example when the player
    # is driving a one of the ships, the cost is not 4, is just 1
    def setCost(self, newCost):
        self.cost = newCost
        
    def __str__(self):
        return "There is an Oil here["+str(self.position.getX())+" , " + str(self.position.getY()) +  "]"     