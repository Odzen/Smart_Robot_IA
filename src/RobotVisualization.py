"""
Class RobotVisualization to visualize the Robot movements
"""

import math
import time
from Classes import Position
from Classes import Obstacle

from tkinter import *

class RobotVisualization(object):
    def __init__(self, robot, firstShip, secondShip, items, oils, obstacles, mainMaze, delay = 1):
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
        self.obstacles = obstacles

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
                                       text=self._status_string(0, robot.getCollectedItems(), firstShip.getFuel(), secondShip.getFuel() ))
        self.time = 0
        
        
        # Draw Obstacles
        self._draw_obstacles(obstacles)
        
        # Draw Oils
        self._draw_oils(oils)
        
        # Draw Items
        self._draw_items(items)
        
        # Draw Ships
        self._draw_ships(firstShip, secondShip)
        
        
        # Draw Robot
        robotPosition = robot.getRobotPosition()
        self._draw_robot(robotPosition)
        
        self.master.update()
    
    def _map_coords(self, x, y):
        "Maps grid positions to window positions (in pixels)."
        return (250 + 450 * ((y - self.width / 2.0) / self.max_dim),
                250 + 450 * ((x - self.height / 2.0) / self.max_dim))
    
    def _status_string(self, time, items, fuel1, fuel2):
        "Returns an appropriate status string to print."
        return "Time: %04d; Items Collected: %d; Ship 1 Fuel: %d; Ship 2 Fuel: %d " % \
            (time, items, fuel1, fuel2)
            
    def _draw_robot(self, position):
        "Returns a polygon representing a robot with the specified parameters."
        
        x, y = position.getX(), position.getY()
        x1, y1 = self._map_coords(x , y)
        x2, y2 = self._map_coords(x + 1 , y + 1)
        
        if self.firstShip.isRobotDriving():
            self.w.create_rectangle(x1, y1, x2, y2, fill = "green")

        if self.secondShip.isRobotDriving():
            self.w.create_rectangle(x1, y1, x2, y2, fill = "purple")
            
        self.w.create_oval(x1, y1, x2, y2, fill = "cyan")
    
    def _draw_obstacles(self, obstacles):
        "Returns rectangles representing the obstacles with the specified parameters."
        for obstacle in obstacles:
            obstaclePosition = obstacle.getObstaclePosition()
            x, y = obstaclePosition.getX(), obstaclePosition.getY()
            x1, y1 = self._map_coords(x , y)
            x2, y2 = self._map_coords(x + 1 , y + 1)
            self.w.create_rectangle(x1, y1, x2, y2, fill = "gray")
                    
    def _draw_oils(self, oils):
        "Returns rectangles representing the oils with the specified parameters."
        for oil in oils:
            if oil.getOilState():
                oilPosition = oil.getOilPosition()
                x, y = oilPosition.getX(), oilPosition.getY()
                x1, y1 = self._map_coords(x , y)
                x2, y2 = self._map_coords(x + 1 , y + 1)
                self.w.create_rectangle(x1, y1, x2, y2, fill = "red")

                    
    def _draw_items(self, items):
        "Returns rectangles representing the items with the specified parameters."
        for item in items:
            if item.getItemState():
                itemPosition = item.getItemPosition()
                x, y = itemPosition.getX(), itemPosition.getY()
                x1, y1 = self._map_coords(x , y)
                x2, y2 = self._map_coords(x + 1 , y + 1)
                self.w.create_rectangle(x1, y1, x2, y2, fill = "yellow")

    def _draw_ships(self, firstShip, secondShip):
        "Returns rectangles representing the ships with the specified parameters."
        
        #Ship 1
        
        if not firstShip.isRobotDriving() and firstShip.getShipState():
            firstShipPosition = firstShip.getShipPosition()
            xShip1, yShip1 = firstShipPosition.getX(), firstShipPosition.getY()
            x1Ship1, y1Ship1 = self._map_coords(xShip1 , yShip1)
            x2Ship1, y2Ship1 = self._map_coords(xShip1 + 1 , yShip1 + 1)
            self.w.create_rectangle(x1Ship1, y1Ship1, x2Ship1, y2Ship1, fill = "green")
        
        #Ship 2
        if not secondShip.isRobotDriving() and secondShip.getShipState():
            secondShipPosition = secondShip.getShipPosition()
            xShip2, yShip2 = secondShipPosition.getX(), secondShipPosition.getY()
            x1Ship2, y1Ship2 = self._map_coords(xShip2 , yShip2)
            x2Ship2, y2Ship2 = self._map_coords(xShip2 + 1 , yShip2 + 1)
            self.w.create_rectangle(x1Ship2, y1Ship2, x2Ship2, y2Ship2, fill = "purple")
    
    
    
    def update(self):
        "Redraws the visualization with the specified params"
        self.w.delete("all")
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
        
        # Draw Obstacles
        self._draw_obstacles(self.obstacles)
        
        # Draw Oils
        self._draw_oils(self.oils)
        
        # Draw Items
        self._draw_items(self.items)
            
        
        # Draw Ships
        self._draw_ships(self.firstShip, self.secondShip)
    
        
        # Draw Robot
        robotPosition = self.robot.getRobotPosition()
        self._draw_robot(robotPosition)
        
        # Update text
        self.w.delete(self.text)
        self.time += 1
        self.text = self.w.create_text(
            25, 0, anchor=NW,
            text=self._status_string(self.time, self.robot.getCollectedItems(), self.firstShip.getFuel(), self.secondShip.getFuel()))
        self.master.update()
        time.sleep(self.delay)

        
    def done(self):
        "Indicate that the animation is done so that we allow the user to close the window."
        mainloop()
    
