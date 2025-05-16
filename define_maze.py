import time
from User.define_user import User
from Maze_Algorithms.define_backtracker import define_Backtracker
from Maze_Algorithms.define_huntkill import define_Huntkill
from Maze_Algorithms.define_randomkruskal import define_Randomkruskal
from Maze_Algorithms.define_ellermaze import define_Ellermaze

class define_Maze:
	def __init__(self):
		self.Maze = define_Ellermaze(5)
		self.timePassed = 0
		self.mazeTimes = []

	def update_maze(self):
		if self.Maze.check_maze():
			self.Maze.create_maze()
			self.timePassed += 1
			return
		self.mazeTimes.append([self.Maze.mazeSize, self.timePassed])
		hours = int(self.timePassed / 216000)
		minutes = int(self.timePassed / 3600 % 60)
		seconds = round(self.timePassed / 60 % 60, 2)
		if hours != 0:
			if 0 <= minutes < 10:
				minutes = "0"+str(minutes)
			print("Size {}, time: {}:{}:{}".format(self.Maze.mazeSize, hours, minutes, seconds))
		elif minutes != 0:
			print("Size {}, time: {}:{}".format(self.Maze.mazeSize, minutes, seconds))
		else:
			print("Size {}, time: {}".format(self.Maze.mazeSize, seconds))
		self.Maze = define_Ellermaze(self.Maze.mazeSize + 5)
		self.startTime = 0

Maze = define_Maze()
