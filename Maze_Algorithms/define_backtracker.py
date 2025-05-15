import pygame, random, copy
from pygame.locals import *

class define_Backtracker:
	def check_position(self, checkedPosition, prePositions):
		for prePosition in prePositions:
			if checkedPosition == prePosition:
				return True
		if checkedPosition[0] == len(self.maze) or checkedPosition[0] < 0:
			return True
		if checkedPosition[1] == len(self.maze) or checkedPosition[1] < 0:
			return True
		return False

	def check_closedBox(self):
		for row in self.maze:
			for column in row:
				if column[0] and column[1] and column[2] and column[3]:
					return True
		return False

	def create_maze(self):
		closedBox = self.check_closedBox()

		if closedBox:
			canMove = False
			cantMove = [False, False, False, False]
			
			canAppend = True
			if self.position in self.oldPositions:
				canAppend = False
			if canAppend == True:
				self.oldPositions.insert(self.insertPosition, self.position.copy())
				self.insertPosition += 1
			while canMove == False:
				movement = random.randint(1, 4)
				
				if movement == 1:
					cantMove[0] = self.check_position([self.position[0], self.position[1] + 1], self.oldPositions)
					if cantMove[0] == False:
						self.maze[self.position[1]][self.position[0]][0] = 0
						self.position[1] += 1
						self.maze[self.position[1]][self.position[0]][1] = 0
						canMove = True
				
				if movement == 2:
					cantMove[1] = self.check_position([self.position[0], self.position[1] - 1], self.oldPositions)
					if cantMove[1] == False:
						self.maze[self.position[1]][self.position[0]][1] = 0
						self.position[1] -= 1
						self.maze[self.position[1]][self.position[0]][0] = 0
						canMove = True
				
				if movement == 3:
					cantMove[2] = self.check_position([self.position[0] - 1, self.position[1]], self.oldPositions)
					if cantMove[2] == False:
						self.maze[self.position[1]][self.position[0]][2] = 0
						self.position[0] -= 1
						self.maze[self.position[1]][self.position[0]][3] = 0
						canMove = True
				
				if movement == 4:
					cantMove[3] = self.check_position([self.position[0] + 1, self.position[1]], self.oldPositions)
					if cantMove[3] == False:
						self.maze[self.position[1]][self.position[0]][3] = 0
						self.position[0] += 1
						self.maze[self.position[1]][self.position[0]][2] = 0
						canMove = True
				
				if cantMove[0] and cantMove[1] and cantMove[2] and cantMove[3]:
					self.position = self.oldPositions[self.insertPosition - 2].copy()
					self.insertPosition -= 1
					break

	def __init__(self, mazeSize):
		self.mazeSize = mazeSize
		
		self.maze = []
		for row in range(self.mazeSize):
			self.maze.append([])
			for column in range(self.mazeSize):
				self.maze[row].append([1, 1, 1, 1])
		self.oldPositions = []
		self.position = [0, 0]
		self.insertPosition = 0
		
		self.create_maze()
