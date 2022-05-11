# -*- coding: utf-8 -*-
"""
Created on Thu Apr 28 23:48:50 2022

@author: Juan Sebastian Velasquez
"""

import readFile
import agents
import ia_algorithms
# import signal

Test = 4
MaxSteps = 15
t = 2 # 2 second



def transformData(width, height, lines):
    
    mainMaze = agents.Maze(width,height)
    
    for x in range(len(lines)):
        for y in range(len(lines)):
            if lines[x][y] == 2:
                cheesePosition = agents.Position(x,y)
                cheese = agents.Cheese(cheesePosition,mainMaze)
            if lines[x][y] == 3:
                mousePosition = agents.Position(x,y)
                mouse = agents.MouseAgent2(mousePosition,mainMaze)
            mainMaze.setElement(agents.Position(x,y), lines[x][y])
    
    return mouse, mainMaze, cheese

def main():

    width, height, lines = readFile.input(Test)
    mouse, mainMaze, cheese = transformData(width, height, lines)
    
    # IA Agent 1
    #ia_algorithms.runIAAgent1(mouse, mainMaze, cheese, MaxSteps, t)
    
    # IA Agent 2
    ia_algorithms.runIAAgent2(mouse, mainMaze, cheese, MaxSteps, t)
    
    """
    It seems signal doesn't work in windows'
    
    signal.signal(signal.SIGALRM, signal_handler)
    signal.alarm(10)   # Ten seconds
    try:
        ia_algorithms.runIA(mouse, mainMaze, cheese)
    except Exception as e:
        print("Timed out!")
    """

        
"""
def signal_handler(signum, frame):
    raise Exception("Timed out!")
"""

    
main()

