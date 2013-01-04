# 1. Any live cell with fewer than two live neighbours dies.
# 2. Any live cell two or three live neighbours lives on to the next generation.
# 3. Any live vell with more than three live neighbours dies, as if by overcrowding.
# 4. Any dead cell with exactly three live neighbours becomes a live cell, as if by reproduction.

from random import randint

class World:

	def __init__(self, seed=None, height=10, width=10):
		if seed == None:
			self.height = height - 1
			self.width = width - 1

			self.table = [None] * width
			for i in range(width):
				self.table[i] = [None] * height
				for x in range(height):
					rand = randint(0, 2)
					if rand == 0:
						self.table[i][x] = rand
					else:
						self.table[i][x] = 1
		else:
			self.table = seed
			self.width = len(seed)
			self.height = len(seed[0])


	def liveNeighbors(self, x, y):
	
		ret = 0
		if x > 0:
			ret += self.table[x-1][y]
			if y > 0:
				ret += self.table[x-1][y-1]

			if y < self.height:
				ret += self.table[x-1][y+1]

		if x < self.width:
			ret += self.table[x+1][y]

			if y > 0:
				ret += self.table[x+1][y-1]
			if y < self.height:
				ret += self.table[x+1][y+1]

		if y > 0:
			ret += self.table[x][y-1]
		if y < self.height:
			ret += self.table[x][y+1]
		return ret

	def deadNeighbors(self, x, y):
	#Obviously not necessary but short enough to be worth writing anyway
		return 8 - self.live(x, y)


	def gen(self):
		#create a new table
		next_gen = [None] * self.width

		for x in range(self.width):
			next_gen[x] = [None] * self.height
			for y in range(self.height):
				neighbors = self.liveNeighbors(x, y)
				if neighbors > 2: next_gen[x][y] = 0
				if neighbors > 3: next_gen[x][y] = 0

				if self.table[x][y] == 0:
					if neighbors == 3: next_gen[x][y] == 1
				if self.table[x][y] == 1:
					if neighbors == 2 or neighbors == 2: next_gen[x][y] == 1
		self.table = next_gen
