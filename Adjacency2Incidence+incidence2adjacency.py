class Graph():
	def __init__(self, name):
		self.name=name
		self.nodes=0
		self.incMtx=[[0]*0]*0
		self.adjMtx=[[0]*0]*0
	def setAdjMtx(self,mtx):
		self.adjMtx = mtx
		self.setGraphSize(mtx)
	def setIncMtx(self,mtx):
		self.incMtx = mtx
		self.setGraphSize(mtx)
	def setGraphSize(self, mtx):
		self.nodes = len(mtx)
		self.maxEdge = int(self.nodes*(self.nodes+1)/2)
	#convert adjacent to incidence if 1; and incidence to adjacent if 0
	def convert(self,param):
		if (param):
			self.incMtx=[[0]*self.nodes for i in range(self.maxEdge*2-1)]
			x = 0
			for row in range(len(self.adjMtx)):
				for col in range(len(self.adjMtx[0])):
					if (self.adjMtx[row][col]==1):
						self.incMtx[x][col]=1
						self.incMtx[x][row]=1
					x+=1
			temp = []
			for row in self.incMtx:
				if row not in temp:
					if (1 in row):
						temp.append(row)	

			self.incMtx = Transpose(temp)

		else:
			self.adjMtx=[[0]*self.nodes for i in range(self.nodes)]
			conNodes=[]
			mtxT = Transpose(self.incMtx)
			for row in range(len(mtxT)):
				for col in range(len(mtxT[0])):
					if (mtxT[row][col]==1):
						conNodes.append(col)
				if (len(conNodes)!=0):
					self.adjMtx[conNodes[1]][conNodes[0]]=1
					self.adjMtx[conNodes[0]][conNodes[1]]=1

				conNodes=[]
#mtx function
def Transpose(mtx):
	mtxT = list(map(list, zip(*mtx)))
	for row in mtxT:
		print(row)
	return mtxT


def getMatrix():
	#input format  [a1,a2,a3..an;b1,b2,b3..bn;...]
	arr = []
	print("your matrix :")
	inp=input()
	#inp ="[1,0,0;0,1,0;0,0,1;1,1,1]"
	inp=inp[1:-1].split(';')
	for i in inp:
		row = i.split(',')
		for c in range(len(row)):
			row[c]=int(row[c])
		arr.append(row)

	for row in arr:
		print(row)

	return arr



def main():
	print("matrices format : [a1,a2,a3,..ax;b1,b2,b3,..bx;...;n1,n2,n3,..nx]")
	graph1=Graph("graph1")
	print("select matrices types: 1 for adjacent, 0 for incidence :")
	uinp = int(input())
	if ((uinp!=1) and (uinp!=0)):
		return 0
	if (uinp):
		graph1.setAdjMtx(getMatrix())
	else:
		graph1.setIncMtx(getMatrix())
		
	graph1.convert(uinp)
	print("adjacent :\n")
	for row in graph1.adjMtx:
		print(row)
	print("\nincidence:\n")
	for row in graph1.incMtx:
		print(row)

main()