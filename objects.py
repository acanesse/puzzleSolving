class piece:
	""" Simple class to reprensent pieces """
	positionX = 0
	positionY = 0
	rotated = False
	flipped = False

	def __init__(self):
		self.cases = [[0,0],[0,0],[0,0]]

	def fillCase(self,xylist):
		for xy in xylist:
			self.cases[xy[1]][xy[0]]=1

	def flipPiece(self):

		c = self.cases
		sqarreMatrix = []
		



	def rotatePiece(self):

		if self.rotated == False:
			self.cases = [ [self.cases[1][0],self.cases[1][1],self.cases[2][1]] , [self.cases[0][0],self.cases[1][0],self.cases[2][0]] ]
			self.rotated = True

		elif self.rotated == True:
			pass
			self.rotated = False

		else:
			print("What did you do to you poor piece!?\nIt's not rotated it's broken!")


	def getPositions(self):
		positions = []
		for y,row in enumerate(self.cases):
			#print("y=",y)
			for x,value in enumerate(row):
				#print("x=",x)
				if value == 1:
					positions.append([x,y])

		return positions



class board:
	""" Simple class to represent the boards """

	def __init__(self):
		self.cases = [[0,0,0],[0,0,0],[0,0,0]]
		self.numberOfPieces = 0

	def placePiece(self, piece, xshift, yshift):
		piece.positionX = xshift
		piece.positionY = yshift
		positions = piece.getPositions()
		print(positions)
		hypotheticalBoard = self.cases

		for p in positions:
			x = p[0]+xshift
			y = p[1]+yshift
			if x>2 or y>2:
				print("You can't put your piece there")
				return False
			if(hypotheticalBoard[y][x]>0):
				print("Case already occupied in ", x,y)
				return False
			else: 
				hypotheticalBoard[y][x] +=1

		self.cases = hypotheticalBoard
		self.numberOfPieces += 1
		return True