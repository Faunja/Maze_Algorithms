import time
from User.define_user import User
from Maze_Algorithms.define_backtracker import define_Backtracker
from Maze_Algorithms.define_huntkill import define_Huntkill
from Maze_Algorithms.define_randomkruskal import define_Randomkruskal
from Maze_Algorithms.define_ellermaze import define_Ellermaze

class define_Maze:
	def __init__(self):
		self.Backtracker = [define_Backtracker(5), 0, "Back tracker", False]
		self.Huntkill = [define_Huntkill(5), 0, "Hunt and kill", False]
		self.Randomkruskal = [define_Randomkruskal(5), 0, "Randomized Kruskal", False]
		self.Ellermaze = [define_Ellermaze(5), 0, "Eller's Maze", False]
		self.timePassed = 0
		self.mazeTimes = []
	
	def check_maze(self, Maze):
		if Maze[0].check_maze():
			Maze[0].create_maze()
			Maze[1] += 1
			return
		if not Maze[3]:
			self.mazeTimes.append([Maze[0].mazeSize, Maze[1], Maze[2]])
			hours = int(Maze[1] / 216000)
			minutes = int(Maze[1] / 3600 % 60)
			seconds = round(Maze[1] / 60 % 60, 2)
			if hours != 0:
				if 0 <= minutes < 10:
					minutes = "0"+str(minutes)
				print("{} {}, time: {}:{}:{}".format(Maze[2], Maze[0].mazeSize, hours, minutes, seconds))
			elif minutes != 0:
				if 0 <= seconds < 10:
					seconds = "0"+str(seconds)
				print("{} {}, time: {}:{}".format(Maze[2], Maze[0].mazeSize, minutes, seconds))
			else:
				print("{} {}, time: {}".format(Maze[2], Maze[0].mazeSize, seconds))
			Maze[3] = True
			Maze[1] = 0
	
	def update_maze(self):
		self.check_maze(self.Backtracker)
		self.check_maze(self.Huntkill)
		self.check_maze(self.Randomkruskal)
		self.check_maze(self.Ellermaze)
		if self.Backtracker[3] and self.Huntkill[3] and self.Randomkruskal[3] and self.Ellermaze[3]:
			self.Backtracker[0] = define_Backtracker(self.Backtracker[0].mazeSize + 5)
			self.Backtracker[3] = False
			self.Huntkill[0] = define_Huntkill(self.Huntkill[0].mazeSize + 5)
			self.Huntkill[3] = False
			self.Randomkruskal[0] = define_Randomkruskal(self.Randomkruskal[0].mazeSize + 5)
			self.Randomkruskal[3] = False
			self.Ellermaze[0] = define_Ellermaze(self.Ellermaze[0].mazeSize + 5)
			self.Ellermaze[3] = False

Maze = define_Maze()
