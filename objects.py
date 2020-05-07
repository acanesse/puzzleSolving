import numpy as np

class piece:
	""" Simple class to reprensent pieces """
	positionX = 0
	positionY = 0
	rotated = False
	flipped = False

	def __init__(self,s):
		self.squarres = np.zeros((s,2))
		self.size = s

	def print(self):
		print("This is a puzzle piece of size", self.size)
		print("Rotation: ",self.rotated, ", flipped: ", self.flipped)
		print("Position: x=",self.positionX,", y=",self.positionY)
		print(self.squarres, "\n")

	def fillSquare(self,xylist):
		for xy in xylist:
			x=xy[0]
			y=xy[1]
			self.squarres[y][x]=1

	def flipPiece(self):

		print("Flipping piece")
		self.squarres = np.rot90(self.squarres,2)
		self.flipped = not self.flipped
		#print(self.squarres)

	def rotatePiece(self):

		print("Rotating piece")
		self.squarres = np.rot90(self.squarres,1)
		self.rotated = not self.rotated
		#print(self.squarres)


class board:
	""" Simple class to represent the boards """

	def __init__(self,s):
		self.squarres = np.zeros((s,s))
		self.size = s
		self.numberOfPieces = 0

	def placePiece(self, piece, x, y):

		# Sort out position
		# if non flipped, x=0,1 and y=0
		# if flipped x = 0 and y =0,1
		if x>1 or y>1:
			print("Error, x and y can't be >1")
			return False
		if piece.flipped and x>0:
			print("Error, piece is flipped so x should be 0")
			return False
		elif not piece.flipped and y>0:
			print("Error, piece is not flipped so y should be 0")
			return False

		piece.positionX = x
		piece.positionY = y

		workMatrix = np.zeros((piece.size,piece.size))

		if piece.flipped == False: 
			if x == 0: workMatrix[:,:-1] = piece.squarres
			elif x == 1: workMatrix[:,1:] = piece.squarres

		else:  
			if y == 0: 
				workMatrix[:-1,:] = piece.squarres
			elif y == 1: 
				workMatrix[1:,:] = piece.squarres

		test = self.squarres + workMatrix
		for cell in np.nditer(test):
			if cell>1:
				return False

		# Success!
		self.squarres = test
		self.numberOfPieces += 1

		return True