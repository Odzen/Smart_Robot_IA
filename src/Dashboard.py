import tkinter as tk
from urllib import robotparser

from RobotVisualization import RobotVisualization

from RobotVisualization import *
from SearchAlgorithms.UninformedSearch import BreadthFirst
from SearchAlgorithms.UninformedSearch import UniformCost
from SearchAlgorithms.UninformedSearch import DepthFirst
from SearchAlgorithms.InformedSearch import Avara
from SearchAlgorithms.InformedSearch import AStar

class Dashboard():
    def __init__(self, root, robot, firstShip, secondShip, items, oils,obstacles, mainMaze, delay):
        self.root=root
        root.title("Smart Robot")
        
        self.robot = robot
        self.firstShip = firstShip
        self.secondShip = secondShip
        self.items = items
        self.oils = oils 
        self.obstacles = obstacles
        self.mainMaze = mainMaze
        self.delay = delay

        # the width, height and colors are temporary,
        # until we have more of the GUI working.
        buttonPanel = tk.Frame(self.root, background="green", width=200, height=200)
        self.canvasPanel = tk.Frame(self.root, background="white", width=500, height=500)

        # because these two panels are side-by-side, pack is the
        # best choice:
        buttonPanel.pack(side="left", fill="y")
        self.canvasPanel.pack(side="left")

        # fill in these two areas:
        self._create_buttons(buttonPanel)
        
        self.canvas = RobotVisualization(self.robot, self.firstShip, self.secondShip, self.items, self.oils, self.obstacles, self.mainMaze, self.canvasPanel, self.delay)

    def _create_buttons(self, parent):
        b1=tk.Button(parent,text="BREADTH FIRST", command= self.buttonClickBreadth)
        b2=tk.Button(parent,text="DEPTH FIRST", command= self.buttonClickDepth)
        b3=tk.Button(parent,text="UNIFORM COST", command= self.buttonClickUniform)
        b4=tk.Button(parent,text="AVARA", command= self.buttonClickAvara)
        b5=tk.Button(parent,text="A_STAR", command= self.buttonClickAStar)
        b6=tk.Button(parent,text="REFRESH", command= self.refresh)

        b1.grid(row = 0,column = 0, sticky = "we")
        b2.grid(row = 0,column = 1, sticky = "we")
        b3.grid(row = 1,column = 0, sticky = "we")
        b4.grid(row = 1,column = 1, sticky = "we")
        b5.grid(row = 2,column = 0, sticky = "we")
        b6.grid(row = 2,column = 1, sticky = "we")
    
    # TODO -> Right now this doesn't work properly
    def refresh(self):
        # destroy all widgets from frame
        
        self.canvas.getW().delete("all")
        self.canvasPanel.pack(side="left")
        canvasPanel = tk.Frame(self.root, background="white", width=500, height=500)
        self.canvas = RobotVisualization(self.robot, self.firstShip, self.secondShip, self.items, self.oils, self.obstacles, self.mainMaze, canvasPanel, self.delay)
        
        
    
    def buttonClickBreadth(self):
        # BREADTH FIRST
        breadth_First = BreadthFirst.Breadth_First(self.robot, self.firstShip, self.secondShip, self.items, self.oils, self.obstacles, self.mainMaze)
        path_breadth = breadth_First.constructPath()
        breadth_First.giveDirectionsRobot(path_breadth, self.canvas)
        breadth_First.report(path_breadth)
    
    def buttonClickDepth(self):
        # DEPTH FIRST
        depth_First = DepthFirst.DepthFirst(self.robot, self.firstShip, self.secondShip, self.items, self.oils, self.obstacles, self.mainMaze)
        path_depth = depth_First.constructPath()
        print(path_depth)
        depth_First.giveDirectionsRobot(path_depth, self.canvas)
        depth_First.report(path_depth)
        
    def buttonClickUniform(self):    
        #UNIFORM COST
        uniform_cost = UniformCost.UniformCost(self.robot, self.firstShip, self.secondShip, self.items, self.oils, self.obstacles, self.mainMaze)
        path_cost = uniform_cost.constructPath()
        uniform_cost.giveDirectionsRobot(path_cost, self.canvas)
        uniform_cost.report(path_cost)
    
    def buttonClickAvara(self):    
        # AVARA
        avara = Avara.Avara(self.robot, self.firstShip, self.secondShip, self.items, self.oils, self.obstacles, self.mainMaze)
        avara_path = avara.constructPath()
        print(avara_path)
        avara.giveDirectionsRobot(avara_path, self.canvas)
        avara.report(avara_path)
        
    def buttonClickAStar(self):
        #A_STAR
        a_star = AStar.AStar(self.robot, self.firstShip, self.secondShip, self.items, self.oils, self.obstacles, self.mainMaze)
        a_star_path = a_star.constructPath()
        print(a_star_path)
        a_star.giveDirectionsRobot(a_star_path, self.canvas)
        a_star.report(a_star_path)
    
        