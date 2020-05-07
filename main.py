import objects as obj

print("hello, welcome to the puzzle sovling code")

p1 = obj.piece()
p1.fillCase([[0,0],[0,2]])
p2 = obj.piece()
p2.fillCase([[1,0],[0,2]])
p3 = obj.piece()
p3.fillCase([[0,1],[1,2]])
p4 = obj.piece()
p4.fillCase([[0,2],[1,2]])
pieces = [p1,p2,p3,p4]

print(p1.cases)
print(p2.cases)
print(p3.cases)
print(p4.cases)

b = obj.board()
p1.flipPiece()
b.placePiece(p1,0,0)
#b.placePiece(p1,0,0)
#b.placePiece(p1,0,0)

print(b.cases)