# -*- coding: utf-8 -*-
"""
Created on Thu Apr 28 23:48:50 2022

@author: Juan Sebastian Velasquez
"""
import inspect
from Classes import Item
from Classes import Maze
from Classes import Oil
from Classes import Robot
from Classes import Obstacle
from Classes import OpenCell
from Classes import Ship
from Classes import Position 
from SearchAlgorithms.InformedSearch import *
from SearchAlgorithms.UninformedSearch import *
from SearchAlgorithms import ia_algorithms
from ReadTest import *

#import sys
#sys.path.append(1, '/SearchAlgorithms')
#import ia_algorithms




def transformData(width, height, lines):
    
    mainMaze = Maze.Maze(width, height)
    items = []
    oils = []
    
    for x in range(len(lines)):
        for y in range(len(lines)):
            # Open Cell
            if lines[x][y] == 0:
                openCellPosition = Position.Position(x, y)
                openCell = OpenCell.OpenCell(openCellPosition, mainMaze)
            # Obstacle
            if lines[x][y] == 1:
                obstaclePosition = Position.Position(x, y)
                obstacle = Obstacle.Obstacle(obstaclePosition, mainMaze)
            # Robot
            if lines[x][y] == 2:
                robotPosition = Position.Position(x, y)
                robot = Robot.Robot1(robotPosition, mainMaze)
            # Ship 1, fuel for 10 movements
            if lines[x][y] == 3:
                firstShipPosition = Position.Position(x, y)
                firstShip = Ship.Ship(firstShipPosition, mainMaze, 10)
            # Ship 2, fuel for 20 movements
            if lines[x][y] == 4:
                secondShipPosition = Position.Position(x, y)
                secondShip = Ship.Ship(secondShipPosition, mainMaze, 20)
            # Item
            if lines[x][y] == 5:
                itemPosition = Position.Position(x, y)
                item = Item.Item(itemPosition, mainMaze)
                items.append(item)
            # Oil
            if lines[x][y] == 6:
                oilPosition = Position.Position(x, y)
                oil = Oil.Oil(oilPosition, mainMaze)
                oils.append(oil)
            mainMaze.setElement(Position.Position(x,y), lines[x][y])
    
    return robot, firstShip, secondShip, items, oils, mainMaze 

def main():
    
    Test = 1
    MaxSteps = 15
    t = 2 # 2 seconds
    
    readWrite = ReadAndWrite(Test)
    width, height, lines = readWrite.input()
    robot, firstShip, secondShip, items, oils, mainMaze = transformData(width, height, lines)
    numberItems = len(items)
    numberOils = len(oils)
    
# =============================================================================
#     # Testing checks
#     print(robot.isObstacleUp())
#     print(robot.isObstacleOnLeft())
#     print(robot.isObstacleOnRight())
#     print(robot.isObstacleDown())
# =============================================================================

    # Testing Movements
    # IA Agent 1, Simple algorithm to check movements
    ia_algorithms.runIAAgent1(robot, mainMaze, items, MaxSteps, t)
    
    
    if(robot.getCollectedItems() == numberItems):
        print("Collected All Items")

main()

