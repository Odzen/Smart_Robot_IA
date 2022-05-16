"""
Class RobotVisualization to visualize the Robot movements
"""

import math
import time

from tkinter import *

class RobotVisualization(object):
    def __init__(self, robot, firstShip, secondShip, items, oils, mainMaze, delay = 0.2):
        "Initializes a visualization with the specified parameters."
        # Number of seconds to pause after each frame
        self.delay = delay
        
        self.width = mainMaze.getWidth()
        self.height = mainMaze.getHeight()
        self.max_dim = max(self.width, self.height)
        self.maze = mainMaze
        self.robot = robot
        self.firstShip = firstShip
        self.secondShip = secondShip
        self.items = items
        self.oils = oils

        # Initialize a drawing surface
        self.master = Tk()
        self.w = Canvas(self.master, width=500, height=500)
        self.w.pack()
        self.master.update()

        # Draw a backing and lines
        x1, y1 = self._map_coords(0, 0)
        x2, y2 = self._map_coords(self.width, self.height)
        self.w.create_rectangle(x1, y1, x2, y2, fill = "white")
        
    def done(self):
        "Indicate that the animation is done so that we allow the user to close the window."
        mainloop()
    
