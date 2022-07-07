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

    def isRobotDriving(self):
        return self.robotDriving

    def setShipRobotDriving(self):
        if not self.robotDriving:
            self.robotDriving = True
        else:
            self.robotDriving = False

    def getShipState(self):
        return self.state

    def setShipState(self):
        if self.state:
            self.state = False
        else:
            self.state = True

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
            self.setShipState()
            self.setShipRobotDriving()

    def __str__(self):
        return "There is a Ship here[" + str(
            self.position.getX()) + " , " + str(
                self.position.getY()) + "]" + " with " + str(
                    self.getFuel()) + " of fuel"
