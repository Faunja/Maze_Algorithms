import pygame, random, copy
from pygame.locals import *
from User.define_user import User
from Maze_Algorithms.define_backtracker import define_Backtracker
from Maze_Algorithms.define_huntkill import define_Huntkill

class define_Maze:
	def __init__(self):
		self.Maze = define_Huntkill(5)
		self.timePassed = 0
		self.mazeTimes = []

	def update_maze(self):
		if self.Maze.check_closedBox():
			self.Maze.create_maze()
			self.timePassed += 1
			return
		self.mazeTimes.append([self.Maze.mazeSize, self.timePassed])
		print("Size {}, time: {}".format(self.Maze.mazeSize, self.timePassed))
		self.Maze = define_Huntkill(self.Maze.mazeSize + 5)
		self.startTime = 0

Maze = define_Maze()
