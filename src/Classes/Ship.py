"""
Class Ship
"""

#from itertools import count # Tool for Ids


# Recieves a Maze and an initial position of the Ship
# Each ship has a counter, because we need to know 
class Ship(object):
    def __init__(self, position, maze, fuel):
        self.position = position
        self.maze = maze
        self.cost = 1
        self.fuel = fuel
        #maze.setElement(position,6)
    
    def getCost(self):
        return self.cost
    
    def getFuel(self):
        return self.fuel
    
    def setFuel(self, newFuel):
        self.fuel = newFuel
    
    def getShipPosition(self):
        return self.position
    
    def decreaseFuelByOne(self):
        self.fuel -= 1
    
    def __str__(self):
        return "There is a Ship here["+str(self.position.getX())+" , " + str(self.position.getY()) +  "]" + " with " + str(self.getFuel()) + " of fuel"   