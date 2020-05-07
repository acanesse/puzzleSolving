import objects as obj

print("hello, welcome to the puzzle sovling code")

# Initialisation
p1 = obj.piece(3)
p1.fillSquare([[0,0],[0,2]])
p2 = obj.piece(3)
p2.fillSquare([[1,0],[0,2]])
p3 = obj.piece(3)
p3.fillSquare([[0,1],[1,2]])
p4 = obj.piece(3)
p4.fillSquare([[0,2],[1,2]])
pieces = [p1,p2,p3,p4]

b = obj.board(3)

positions = [0,1]
#while(b.numberOfPieces<4):
for p in pieces:
	fits = False
	for x in positions:
		for y in positions:
			fits = b.placePiece(p,x,y)
			if fits == True : break
		if fits == True : break



print("Finnal board:\n", b.squarres)
for p in pieces:
	p.print()