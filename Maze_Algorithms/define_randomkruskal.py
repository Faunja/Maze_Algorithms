import random

class define_Randomkruskal:
	def check_maze(self):
		for row in self.numbers:
			for column in row:
				if column != 0:
					return True
		return False

	def replace_numbers(self, firstNumber, secondNumber):
		if firstNumber < secondNumber:
			replacement = firstNumber
			replace = secondNumber
		else:
			replacement = secondNumber
			replace = firstNumber
		for row in range(self.mazeSize):
			for column in range(self.mazeSize):
				if self.numbers[row][column] == replace:
					self.numbers[row][column] = replacement
	
	def create_maze(self):
		closedBox = self.check_maze()
		self.position = [random.randrange(self.mazeSize), random.randrange(self.mazeSize)]

		if closedBox:
			canMove = False
			cantMove = [False, False, False, False]
			
			while canMove == False:
				movement = random.randint(0, 4)

				if movement == 0 and not cantMove[0]:
					cantMove[0] = self.position[1] + 1 >= self.mazeSize
					if not cantMove[0]:
						cantMove[0] = self.numbers[self.position[1]][self.position[0]] == self.numbers[self.position[1] + 1][self.position[0]]
					if not cantMove[0]:
						self.maze[self.position[1]][self.position[0]][0] = 0
						self.maze[self.position[1] + 1][self.position[0]][1] = 0
						self.replace_numbers(self.numbers[self.position[1]][self.position[0]], self.numbers[self.position[1] + 1][self.position[0]])
						canMove = True
				
				if movement == 1 and not cantMove[1]:
					cantMove[1] = self.position[1] - 1 < 0
					if not cantMove[1]:
						cantMove[1] = self.numbers[self.position[1]][self.position[0]] == self.numbers[self.position[1] - 1][self.position[0]]
					if not cantMove[1]:
						self.maze[self.position[1]][self.position[0]][1] = 0
						self.maze[self.position[1] - 1][self.position[0]][0] = 0
						self.replace_numbers(self.numbers[self.position[1]][self.position[0]], self.numbers[self.position[1] - 1][self.position[0]])
						canMove = True
				
				if movement == 2 and not cantMove[2]:
					cantMove[2] = self.position[0] - 1 < 0
					if not cantMove[2]:
						cantMove[2] = self.numbers[self.position[1]][self.position[0]] == self.numbers[self.position[1]][self.position[0] - 1]
					if not cantMove[2]:
						self.maze[self.position[1]][self.position[0]][2] = 0
						self.maze[self.position[1]][self.position[0] - 1][3] = 0
						self.replace_numbers(self.numbers[self.position[1]][self.position[0]], self.numbers[self.position[1]][self.position[0] - 1])
						canMove = True
				
				if movement == 3 and not cantMove[3]:
					cantMove[3] = self.position[0] + 1 >= self.mazeSize
					if not cantMove[3]:
						cantMove[3] = self.numbers[self.position[1]][self.position[0]] == self.numbers[self.position[1]][self.position[0] + 1]
					if not cantMove[3]:
						self.maze[self.position[1]][self.position[0]][3] = 0
						self.maze[self.position[1]][self.position[0] + 1][2] = 0
						self.replace_numbers(self.numbers[self.position[1]][self.position[0]], self.numbers[self.position[1]][self.position[0] + 1])
						canMove = True
				
				if cantMove[0] and cantMove[1] and cantMove[2] and cantMove[3]:
					break

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
		
		self.create_maze()

