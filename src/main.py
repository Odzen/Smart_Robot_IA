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
from ReadTest import *
from RobotVisualization import *
from SearchAlgorithms.UninformedSearch import BreadthFirst
from SearchAlgorithms.UninformedSearch import UniformCost
from SearchAlgorithms.UninformedSearch import DepthFirst
from SearchAlgorithms.InformedSearch import Avara
from SearchAlgorithms.InformedSearch import AStar
import tkinter as tk
from tkinter import ttk
from Dashboard import Dashboard


#import sys
#sys.path.append(1, '/SearchAlgorithms')
#import ia_algorithms



def transformData(width, height, lines):

    mainMaze = Maze.Maze(width, height)
    items = []
    oils = []
    obstacles = []

    for x in range(width):
        for y in range(height):
            # Open Cell
            if lines[x][y] == 0:
                openCellPosition = Position.Position(x, y)
                openCell = OpenCell.OpenCell(openCellPosition, mainMaze)
            # Obstacle
            if lines[x][y] == 1:
                obstaclePosition = Position.Position(x, y)
                obstacle = Obstacle.Obstacle(obstaclePosition, mainMaze)
                obstacles.append(obstacle)
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
            mainMaze.setElement(Position.Position(x, y), lines[x][y])

    return robot, firstShip, secondShip, items, oils, obstacles, mainMaze


def main():

    Test = 2 # The number of text that I want to try, the tests are in the folder MazeTests/in
    # 2 seconds, the delay that I want to give to each frame of movement of my robot, if I not pass this to RobotVisualization, the robot will do 1 movement per second by default
    # Basically, if you want the robot move faster, decrease this value and pass this as an argument of RobotVisualization class
    # THE LESS DELAY, THE FASTER THE ROBOT WILL MOVE
    delay = 0.3   

    readWrite = ReadAndWrite(Test)
    width, height, lines = readWrite.input()
    robot, firstShip, secondShip, items, oils, obstacles, mainMaze = transformData(width, height, lines)
    
    root=tk.Tk()
    root.geometry("1000x600")
    root.title("Smart Robot")
    dashboard = Dashboard(root, robot, firstShip, secondShip, items, oils,obstacles, mainMaze, delay, Test)
    root.mainloop()
    # RobotVisualization(robot, firstShip, secondShip, items, oils,obstacles, mainMaze, optional : delay)
    #anim = RobotVisualization(robot, firstShip, secondShip, items, oils,obstacles, mainMaze, root, delay)
    
    


main()
