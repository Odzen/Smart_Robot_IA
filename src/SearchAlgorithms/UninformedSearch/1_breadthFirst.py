"""
BFS - Breadth First Search
"""
from Node import Node
import sys
sys.path.append("../Classes") # Adds higher directory to python modules path.
import Maze
import Robot 


class Breadth_First(self, goal, nodeRoot, maze):
    
    self.goal = goal
    self.nodeRoot = nodeRoot
    self.path = []
    
    def getGoal(self):
        return self.goal
    
    def getNodeRoot(self):
        return self.nodeRoot
    
    def getMaze(self):
        return self.maze
    
    def getPath(self):
        return self.path
    
    def addOperation(self, operation):
        self.path.append(operation)
    
    def constructTree(self):

        
def executeSearch(robot, firstShip, secondShip, items, oils, obstacles, mainMaze):
    
    initialPosition = robot.getRobotPosition
    nodeRoot = Node(None,initialPosition, 1, 0, 0, None)