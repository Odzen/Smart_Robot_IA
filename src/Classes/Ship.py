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
        self.state = True  #True if the Ship is still on the Maze, False if the Ship is out of fuel
        self.robotDriving = False
        self.active = False

    def isRobotDriving(self):
        return self.robotDriving

    def setShipRobotDriving(self, active):
        self.robotDriving = active
    
    def getMaze(self):
        return self.maze

    def getShipState(self):
        return self.state

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
        if self.fuel == 0:
            self.setShipState = False
            self.setShipRobotDriving(False)

    def __str__(self):
        return "[" + str(
            self.position.getX()) + "," + str(
                self.position.getY()) + "]" + "-Fuel: " + str(
                    self.getFuel()) + "-driving: " + str(self.isRobotDriving())
