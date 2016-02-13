#!/usr/bin/python


import sys
import copy

class Picture(object):
	'''Class of the picture'''
	def __init__(self, rows, columns):
		self.rows = rows
		self.columns = columns
		self.grid = [[]]
		self.colored_grid = [[]]
		self.lines = []

	def findLine(self, r, c):
		'''Find the biggest line startig from given coordinates'''
		matrix = self.grid
		c2_hor = c
		r2_ver = r
		case_hor = matrix[r][c]
		case_ver = matrix[r][c]
		#hor
		for i in range(c2_hor,self.columns):
			if matrix[r][i] != "#":
				break
		c2_hor =i- 1
		#ver
	
		for j in range(r2_ver,self.rows):
			if matrix[j][c] != "#":
				break
		r2_ver = j- 1

		ecart_hor = c2_hor - c
		ecart_ver = r2_ver - r
		if ecart_ver < ecart_hor:
			return (r, c, r, c2_hor)
		else:
			return (r, c, r2_ver, c)

	def declareColor(self, r1, c1, r2, c2):
		'''Declare a line as colored'''
		for i in range(r1, r2 + 1):
			for j in range(c1, c2 + 1):
				self.colored_grid[i][j] = 1

	def paint(self):
		'''Painting the picture'''
		m = self.grid
		#print(m)
		for r in range(self.rows):
			for c in range(self.columns):
				if m[r][c] == '#' and self.colored_grid[r][c] != 1:
					print("Found" + " " + str(r) + " "+ str(c))
					line = self.findLine(r,c)
					self.declareColor(line[0],line[1],line[2],line[3])
					self.lines.append(line)

	def ReadFile(self, filename):
		'''Read input file'''
		
		self.grid = [list(line.rstrip('\n')) for line in open(filename)]
		fp = open(filename)
		lines = fp.readlines()
		first = lines[0]
		first = first.split()
		self.rows = int(first[0])
		self.columns = int(first[1])
		print(str(self.rows) + "  " + str(self.columns))
		self.grid = self.grid[1:]
		self.colored_grid = copy.deepcopy(self.grid)

		for i in range(self.rows):
			for j in range(self.columns):
				self.colored_grid[i][j] = 0
		return self

	def writeToFile(self, filename):
		'''Write result to output'''
		lines = self.lines
		f = open(filename, "w")
		f.write(str(len(lines)) + "\n" )
		for line in lines:
			strr = "PAINT_LINE "+ str(line[0]) + " " + str(line[1]) + " " +  str(line[2]) + " " +  str(line[3]) + "\n" 
			print(strr)
			f.write( strr )
		f.close()

	def getScore(self):
		'''Calculate the score'''
		num1 = 0
		num2 = len(self.lines)
		for i in range(self.rows):
			for j in range(self.columns):
				if self.grid[i][j] == "#":
					num1 += 1
		print(str(num1) + "   " + str(num2) )
		print("Your score is : " + str(num1 - num2))



def main():
	if len(sys.argv) < 3:
		sys.exit('Syntax: %s <filename> <output>' % sys.argv[0])

	pic = Picture(0, 0)
	pic = pic.ReadFile(sys.argv[1])
	pic.paint()
	pic.writeToFile(sys.argv[2])
	pic.getScore()

if __name__ == '__main__':
    main()		