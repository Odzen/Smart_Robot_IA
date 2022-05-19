"""
Class RobotVisualization to visualize the Robot movements
"""

import math
import time
from Classes import Position
from Classes import Obstacle

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
        self.master = Tk() # Window
        self.w = Canvas(self.master, width=500, height=500) # Canvas widget
        self.w.pack() # To add the widget w to the window
        self.master.update()

        # Draw a backing and lines
        x1, y1 = self._map_coords(0, 0)
        x2, y2 = self._map_coords(self.width, self.height)
        self.w.create_rectangle(x1, y1, x2, y2, fill = "white")
        
        # Draw white squares for dirty tiles
        self.tiles = {}
        for i in range(self.width):
            for j in range(self.height):
                x1, y1 = self._map_coords(i, j)
                x2, y2 = self._map_coords(i + 1, j + 1)
                self.tiles[(i, j)] = self.w.create_rectangle(x1, y1, x2, y2,
                                                             fill = "white")
        
        # Draw gridlines
        for i in range(self.width + 1):
            x1, y1 = self._map_coords(i, 0)
            x2, y2 = self._map_coords(i, self.height)
            self.w.create_line(x1, y1, x2, y2)
        for i in range(self.height + 1):
            x1, y1 = self._map_coords(0, i)
            x2, y2 = self._map_coords(self.width, i)
            self.w.create_line(x1, y1, x2, y2)
        
        
        # Draw some status text
        self.text = self.w.create_text(25, 0, anchor=NW,
                                       text=self._status_string(0))
        self.time = 0
        
        # Draw Robot
        robotPosition = robot.getRobotPosition()
        self._draw_robot(robotPosition)
        
        # Draw Walls
        self._draw_walls(mainMaze)
        
        # Draw Oils
        self._draw_oils(oils)
        
        
        self.master.update()
    
    def _map_coords(self, x, y):
        "Maps grid positions to window positions (in pixels)."
        return (250 + 450 * ((y - self.width / 2.0) / self.max_dim),
                250 + 450 * ((x - self.height / 2.0) / self.max_dim))
    
    def _status_string(self, time):
        "Returns an appropriate status string to print."
        return "Time: %04d" % \
            (time)
            
    def _draw_robot(self, position):
        "Returns a polygon representing a robot with the specified parameters."
        x, y = position.getX(), position.getY()
        x1, y1 = self._map_coords(x , y)
        x2, y2 = self._map_coords(x + 1 , y + 1)
        return self.w.create_oval(x1, y1, x2, y2, fill = "black")
    
    def _draw_walls(self, maze):
        "Returns a polygon representing a robot with the specified parameters."
        for i in range(self.width):
            for j in range(self.height):
                currentPosition = Position.Position(i, j)
                if type(maze.getElement(currentPosition)) == Obstacle.Obstacle:
                    x1, y1 = self._map_coords(i , j)
                    x2, y2 = self._map_coords(i + 1 , j + 1)
                    self.w.create_rectangle(x1, y1, x2, y2, fill = "brown")
                    
    def _draw_oils(self, oils):
        "Returns a polygon representing a robot with the specified parameters."
        for oil in oils:
            oilPosition = oil.getOilPosition()
            x, y = oilPosition.getX(), oilPosition.getY()
            x1, y1 = self._map_coords(x , y)
            x2, y2 = self._map_coords(x + 1 , y + 1)
            self.w.create_rectangle(x1, y1, x2, y2, fill = "red")
    
    
    def done(self):
        "Indicate that the animation is done so that we allow the user to close the window."
        mainloop()
    
