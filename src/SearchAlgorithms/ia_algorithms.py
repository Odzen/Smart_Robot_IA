# -*- coding: utf-8 -*-
"""
Created on Fri Apr 29 00:15:50 2022

@author: Juan Sebastian Velasquez Acevedo
"""
import time
from RobotVisualization import *

def runIAAgent1(robot, firstShip, secondShip, items, numberItems, oils, obstacles, mainMaze, maxSteps):
    """

    Parameters
    ----------
    Parameters
    ----------
    robot : RobotAgent1
        Agent.
    mainMaze : Maze
        Grid.
    item : item
        item, goal.
    maxSteps : int
        maximun steps that the robot is allowed to find the item.
    t : int
        time to sleep after each step.

    Returns
    -------
    None.

    """
    
    anim = RobotVisualization(robot, firstShip, secondShip, items, oils, obstacles, mainMaze)
    
    
    print("Initial Maze:")
    print(mainMaze)
    steps = 1
    while(robot.getCollectedItems() != numberItems and steps <= maxSteps):
        print("Step: ", steps)
        if((not (robot.isObstacleOnLeft())) and (not (robot.isObstacleUp())) and (not (robot.isObstacleOnRight())) and (not(robot.isObstacleDown()))):
            print("Caso - 1")
            robot.moveUp()
            steps+=1
            
        elif((not (robot.isObstacleOnLeft())) and (not (robot.isObstacleUp())) and (not (robot.isObstacleOnRight())) and robot.isObstacleDown()):
            print("Caso - 2")
            robot.moveUp()
            steps+=1
            
        elif((not (robot.isObstacleOnLeft())) and (not (robot.isObstacleUp())) and robot.isObstacleOnRight() and (not(robot.isObstacleDown()))):
            print("Caso - 3")
            robot.moveUp()
            steps+=1
            
        elif((not (robot.isObstacleOnLeft())) and (not (robot.isObstacleUp())) and robot.isObstacleOnRight() and robot.isObstacleDown()):
            print("Caso - 4")
            robot.moveUp()
            steps+=1
            
        elif((not (robot.isObstacleOnLeft())) and robot.isObstacleUp() and (not(robot.isObstacleOnRight())) and (not(robot.isObstacleDown()))):
            print("Caso - 5")
            robot.moveLeft()
            steps+=1
            
        elif((not (robot.isObstacleOnLeft())) and robot.isObstacleUp() and (not(robot.isObstacleOnRight()))and robot.isObstacleDown()):
            print("Caso - 6")
            robot.moveRight()
            steps+=1
            
        elif((not (robot.isObstacleOnLeft())) and robot.isObstacleUp() and robot.isObstacleOnRight() and (not(robot.isObstacleDown()))):
            print("Caso - 7")
            robot.moveLeft()
            steps+=1
            
        elif((not (robot.isObstacleOnLeft())) and robot.isObstacleUp() and robot.isObstacleOnRight() and robot.isObstacleDown()):
            print("Caso - 8")
            robot.moveLeft()
            steps+=1
            
        elif(robot.isObstacleOnLeft() and (not (robot.isObstacleUp())) and (not(robot.isObstacleOnRight())) and (not(robot.isObstacleDown()))):
            print("Caso - 9")
            robot.moveUp()
            steps+=1
            
        elif(robot.isObstacleOnLeft() and (not (robot.isObstacleUp())) and (not(robot.isObstacleOnRight())) and robot.isObstacleDown()):
            print("Caso - 10")
            robot.moveRight()
            steps+=1
            
        elif(robot.isObstacleOnLeft() and (not (robot.isObstacleUp())) and robot.isObstacleOnRight() and (not(robot.isObstacleDown()))):
            print("Caso - 11")
            robot.moveDown()
            steps+=1
            
        elif(robot.isObstacleOnLeft() and (not (robot.isObstacleUp())) and robot.isObstacleOnRight() and robot.isObstacleDown()):
            print("Caso - 12")
            robot.moveUp()
            steps+=1
            
        elif(robot.isObstacleOnLeft() and robot.isObstacleUp() and (not(robot.isObstacleOnRight())) and (not(robot.isObstacleDown()))):
            print("Caso - 13")
            robot.moveRight()
            steps+=1
            
        elif(robot.isObstacleOnLeft() and robot.isObstacleUp() and (not(robot.isObstacleOnRight())) and robot.isObstacleDown()):
            print("Caso - 14")
            robot.moveRight()
            steps+=1
            
        else:
            print("Caso - 15")
            robot.moveDown()
            steps+=1
        
        if steps > maxSteps:
            print("Your robot took too long!! Maybe there is no way he can find the items :(")
            anim.done()
        
        anim.update()
        #print(mainMaze)
        #time.sleep(t)




