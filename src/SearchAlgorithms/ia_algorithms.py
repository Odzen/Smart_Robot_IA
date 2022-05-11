# -*- coding: utf-8 -*-
"""
Created on Fri Apr 29 00:15:50 2022

@author: Juan Sebastian Velasquez Acevedo
"""
import time

def runIAAgent1(mouse, mainMaze, cheese, maxSteps, t):
    """

    Parameters
    ----------
    Parameters
    ----------
    mouse : MouseAgent1
        Agent.
    mainMaze : Maze
        Grid.
    cheese : Cheese
        Cheese, goal.
    maxSteps : int
        maximun steps that the mouse is allowed to find the cheese.
    t : int
        time to sleep after each step.

    Returns
    -------
    None.

    """
    print("Initial Maze:")
    print(mainMaze)
    steps = 1
    while(not(mouse.hadfoundCheese()) and steps <= maxSteps):
        print("Step: ", steps)
        if((not (mouse.isSomethingOnLeft())) and (not (mouse.isSomethingUp())) and (not (mouse.isSomethingOnRight())) and (not(mouse.isSomethingDown()))):
            print("Caso - 1")
            mouse.moveUp()
            steps+=1
            
        elif((not (mouse.isSomethingOnLeft())) and (not (mouse.isSomethingUp())) and (not (mouse.isSomethingOnRight())) and mouse.isSomethingDown()):
            print("Caso - 2")
            mouse.moveUp()
            steps+=1
            
        elif((not (mouse.isSomethingOnLeft())) and (not (mouse.isSomethingUp())) and mouse.isSomethingOnRight() and (not(mouse.isSomethingDown()))):
            print("Caso - 3")
            mouse.moveUp()
            steps+=1
            
        elif((not (mouse.isSomethingOnLeft())) and (not (mouse.isSomethingUp())) and mouse.isSomethingOnRight() and mouse.isSomethingDown()):
            print("Caso - 4")
            mouse.moveUp()
            steps+=1
            
        elif((not (mouse.isSomethingOnLeft())) and mouse.isSomethingUp() and (not(mouse.isSomethingOnRight())) and (not(mouse.isSomethingDown()))):
            print("Caso - 5")
            mouse.moveLeft()
            steps+=1
            
        elif((not (mouse.isSomethingOnLeft())) and mouse.isSomethingUp() and (not(mouse.isSomethingOnRight()))and mouse.isSomethingDown()):
            print("Caso - 6")
            mouse.moveRight()
            steps+=1
            
        elif((not (mouse.isSomethingOnLeft())) and mouse.isSomethingUp() and mouse.isSomethingOnRight() and (not(mouse.isSomethingDown()))):
            print("Caso - 7")
            mouse.moveLeft()
            steps+=1
            
        elif((not (mouse.isSomethingOnLeft())) and mouse.isSomethingUp() and mouse.isSomethingOnRight() and mouse.isSomethingDown()):
            print("Caso - 8")
            mouse.moveLeft()
            steps+=1
            
        elif(mouse.isSomethingOnLeft() and (not (mouse.isSomethingUp())) and (not(mouse.isSomethingOnRight())) and (not(mouse.isSomethingDown()))):
            print("Caso - 9")
            mouse.moveUp()
            steps+=1
            
        elif(mouse.isSomethingOnLeft() and (not (mouse.isSomethingUp())) and (not(mouse.isSomethingOnRight())) and mouse.isSomethingDown()):
            print("Caso - 10")
            mouse.moveRight()
            steps+=1
            
        elif(mouse.isSomethingOnLeft() and (not (mouse.isSomethingUp())) and mouse.isSomethingOnRight() and (not(mouse.isSomethingDown()))):
            print("Caso - 11")
            mouse.moveDown()
            steps+=1
            
        elif(mouse.isSomethingOnLeft() and (not (mouse.isSomethingUp())) and mouse.isSomethingOnRight() and mouse.isSomethingDown()):
            print("Caso - 12")
            mouse.moveUp()
            steps+=1
            
        elif(mouse.isSomethingOnLeft() and mouse.isSomethingUp() and (not(mouse.isSomethingOnRight())) and (not(mouse.isSomethingDown()))):
            print("Caso - 13")
            mouse.moveRight()
            steps+=1
            
        elif(mouse.isSomethingOnLeft() and mouse.isSomethingUp() and (not(mouse.isSomethingOnRight())) and mouse.isSomethingDown()):
            print("Caso - 14")
            mouse.moveRight()
            steps+=1
            
        else:
        #(mouse.isSomethingOnLeft() and mouse.isSomethingUp() and mouse.isSomethingOnRight() and (not(mouse.isSomethingDown()))):
            print("Caso - 15")
            mouse.moveDown()
            steps+=1
        
        if steps > maxSteps:
            print("Your Mouse took too long!! Maybe there is no way he can find the cheese :(")
        
        print(mainMaze)
        time.sleep(t)




