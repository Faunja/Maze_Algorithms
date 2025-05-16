import random

class define_Ellermaze:
	def check_maze(self):
		if self.position[0] != self.mazeSize - 1 or self.position[1] != self.mazeSize - 1:
			return True
		return False

	def replace_numbers(self, firstNumber, secondNumber):
		if firstNumber < secondNumber:
			replacement = firstNumber
			replace = secondNumber
		else:
			replacement = secondNumber
			replace = firstNumber
		for number in range(self.mazeSize):
			if self.numbers[self.position[1]][number] == replace:
				self.numbers[self.position[1]][number] = replacement
	
	def create_maze(self):
		if self.siding and self.position[1] != self.mazeSize - 1:
			if random.randint(0, 1) and self.numbers[self.position[1]][self.position[0]] != self.numbers[self.position[1]][self.position[0] + 1]:
				self.maze[self.position[1]][self.position[0]][3] = 0
				self.maze[self.position[1]][self.position[0] + 1][2] = 0
				self.replace_numbers(self.numbers[self.position[1]][self.position[0]], self.numbers[self.position[1]][self.position[0] + 1])
		elif self.siding:
			if self.numbers[self.position[1]][self.position[0]] != self.numbers[self.position[1]][self.position[0] + 1]:
				self.maze[self.position[1]][self.position[0]][3] = 0
				self.maze[self.position[1]][self.position[0] + 1][2] = 0
				self.replace_numbers(self.numbers[self.position[1]][self.position[0]], self.numbers[self.position[1]][self.position[0] + 1])

		if self.flooring:
			if random.randint(0, 1):
				self.maze[self.position[1]][self.position[0]][0] = 0
				self.maze[self.position[1] + 1][self.position[0]][1] = 0
				self.numbers[self.position[1] + 1][self.position[0]] = self.numbers[self.position[1]][self.position[0]]
				self.hole = True
			else:
				self.floors.append(self.position.copy())
			if self.position[0] == self.mazeSize - 1:
				self.checkfloor = True
			else:
				if self.number != self.numbers[self.position[1]][self.position[0] + 1]:
					self.checkfloor = True
					self.number = self.numbers[self.position[1]][self.position[0] + 1]
			if self.checkfloor:
				if not self.hole:
					hole = random.choice(self.floors)
					self.maze[hole[1]][hole[0]][0] = 0
					self.maze[hole[1] + 1][hole[0]][1] = 0
					self.numbers[hole[1] + 1][hole[0]] = self.numbers[hole[1]][hole[0]]
					self.hole = True
				self.checkfloor = False
				self.floors = []
				self.hole = False

		self.position[0] += 1
		if self.check_maze():
			if self.position[0] == self.mazeSize - 1 and self.siding:
				self.position[0] = 0
				self.siding = False
				self.flooring = True
				self.number = self.numbers[self.position[1]][self.position[0]]
			elif self.position[0] == self.mazeSize:
				self.position = [0, self.position[1] + 1]
				self.siding = True
				self.flooring = False

	def __init__(self, mazeSize):
		self.mazeSize = mazeSize
		
		self.maze = []
		self.numbers = []
		for row in range(self.mazeSize):
			self.maze.append([])
			self.numbers.append([])
			for column in range(self.mazeSize):
				self.maze[row].append([1, 1, 1, 1])
				self.numbers[row].append(row * self.mazeSize + column)
		self.position = [0, 0]

		self.siding = True
		self.flooring = False
		self.number = self.numbers[self.position[1]][self.position[0]]
		self.checkfloor = False
		self.floors = []
		self.hole = False
		
		self.create_maze()