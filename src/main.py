# -*- coding: utf-8 -*-
"""
Created on Thu Apr 28 23:48:50 2022

@author: Juan Sebastian Velasquez
"""

from Classes import Item
from Classes import Maze
from Classes import Oil
from Classes import *
from Classes import Robot
from Classes import Ship
from Classes import Position 
from SearchAlgorithms.InformedSearch import *
from SearchAlgorithms.UninformedSearch import *
from SearchAlgorithms import ia_algorithms
from ReadTest import *

#import sys
#sys.path.append(1, '/SearchAlgorithms')
#import ia_algorithms

Test = 1
MaxSteps = 15
t = 2 # 2 second



def transformData(width, height, lines):
    
    mainMaze = Maze.Maze(width, height)
    items = []
    oils = []
    
    for x in range(len(lines)):
        for y in range(len(lines)):
            if lines[x][y] == 2:
                robotPosition = Position.Position(x, y)
                robot = Robot.Robot2(robotPosition, mainMaze)
            if lines[x][y] == 3:
                firstShipPosition = Position.Position(x, y)
                firstShip = Ship.Ship(firstShipPosition, mainMaze)
            if lines[x][y] == 4:
                secondShipPosition = Position.Position(x, y)
                secondShip = Ship.Ship(secondShipPosition, mainMaze)
            if lines[x][y] == 5:
                itemPosition = Position.Position(x, y)
                item = Item.Item(itemPosition, mainMaze)
                items.append(item)
            if lines[x][y] == 6:
                oilPosition = Position.Position(x, y)
                oil = Oil.Oil(oilPosition, mainMaze)
                oils.append(oil)
            mainMaze.setElement(Position.Position(x,y), lines[x][y])
    
    return robot, firstShip, secondShip, items, oils, mainMaze 

def main():
    
    readWrite = ReadAndWrite(Test)
    width, height, lines = readWrite.input()
    robot, firstShip, secondShip, items, oils, mainMaze = transformData(width, height, lines)
    
    ## TEST set up Maze
    print(robot) # Should be in [2,2] according to the test
    print(firstShip) # Should be in [5,9]
    print(secondShip) # Should be in [0,8]
    for item in items: # Should be in [0,5] and [9,9]
        print(item) 
    for oil in oils: # Should be in [2,3],[2,4], [3,1],[3,9],[4,1], [4,9], [5,1], [6,1], [9,4],[9,5],[9,6]
        print(oil) 
    
    
    ## DONT USE, THEY'RE NOT WORKING PROPERLY YET
    # IA Agent 1
    #ia_algorithms.runIAAgent1()
    
    # IA Agent 2
    #ia_algorithms.runIAAgent2()

main()

