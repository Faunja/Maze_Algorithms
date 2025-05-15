import time
from User.define_user import User
from Maze_Algorithms.define_backtracker import define_Backtracker
from Maze_Algorithms.define_huntkill import define_Huntkill
from Maze_Algorithms.define_randomkruskal import define_Randomkruskal

class define_Maze:
	def __init__(self):
		self.Maze = define_Randomkruskal(5)
		self.timePassed = 0
		self.sleepTime = 2
		self.sleptTime = time.time()
		self.mazeTimes = []

	def update_maze(self):
		if self.Maze.check_closedBox():
			self.Maze.create_maze()
			self.timePassed += 1
			self.sleptTime = time.time()
			return
		if self.sleepTime > time.time() - self.sleptTime:
			return
		self.mazeTimes.append([self.Maze.mazeSize, self.timePassed])
		print("Size {}, time: {}".format(self.Maze.mazeSize, self.timePassed))
		self.Maze = define_Randomkruskal(self.Maze.mazeSize + 5)
		self.startTime = 0

Maze = define_Maze()
