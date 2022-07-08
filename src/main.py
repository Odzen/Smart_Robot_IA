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

    Test = 1
    MaxSteps = 15
    t = 2  # 2 seconds

    readWrite = ReadAndWrite(Test)
    width, height, lines = readWrite.input()
    robot, firstShip, secondShip, items, oils, obstacles, mainMaze = transformData(
        width, height, lines)
    numberItems = len(items)
    numberOils = len(oils)

    anim = RobotVisualization(robot, firstShip, secondShip, items, oils,
                              obstacles, mainMaze)
    """
    # BREADTH FIRST
    
    breadth_First = BreadthFirst.Breadth_First(robot, firstShip, secondShip, items, oils, obstacles, mainMaze)
    path_breadth = breadth_First.constructPath()
    breadth_First.giveDirectionsRobot(path_breadth, anim)
    breadth_First.report(path_breadth)
    
    """
    """
    #UNIFORM COST

    uniform_cost = UniformCost.UniformCost(robot, firstShip, secondShip, items,
                                           oils, obstacles, mainMaze)
    path_cost = uniform_cost.constructPath()
    uniform_cost.giveDirectionsRobot(path_cost, anim)
    uniform_cost.report(path_cost)

    """
    """
    # DEPTH FIRST
    depth_First = DepthFirst.DepthFirst(robot, firstShip, secondShip, items, oils, obstacles, mainMaze)
    path_depth = depth_First.constructPath()
    print(path_depth)
    depth_First.giveDirectionsRobot(path_depth, anim)
    depth_First.report(path_depth)
    """
    
    
    # AVARA
    avara = Avara.Avara(robot, firstShip, secondShip, items, oils, obstacles, mainMaze)
    avara_path = avara.constructPath()
    print(avara_path)
    avara.giveDirectionsRobot(avara_path, anim)
    avara.report(avara_path)
    
    
    """
    #A_STAR
    a_star = AStar.AStar(robot, firstShip, secondShip, items, oils, obstacles, mainMaze)
    a_star_path = a_star.constructPath()
    print(a_star_path)
    a_star.giveDirectionsRobot(a_star_path, anim)
    a_star.report(a_star_path)
    """

main()
