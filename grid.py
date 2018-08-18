RED   = "\033[1;31m"  
BLUE  = "\033[1;34m"
CYAN  = "\033[1;36m"
GREEN = "\033[0;32m"
WHITE = '\033[1;37m'
END1 = '\033[0m'
END2 = '\033[1m'
class wall:
	board =[]
	# board[21*21]
	# all objects are of size 2*4		
		#print('#', end='', flush=True)
	def makeBoard():
		line=[]
		for i in  range(1,22):
			line.append('X')
		wall.board.append(line)
		line=[]

		for i in range(1,20):
			line=[]
			if (i%2==0):
				for j in range(1,22):
					if (j%2!=0):
						line.append('X')
					else:
						line.append(' ')
			else:
				line.append('X')
				for j in range(1,20):
					line.append(' ')
				line.append('X')
			wall.board.append(line)

		line=[]
		for i in  range(1,22):
			line.append('X')
		wall.board.append(line)
		line=[]

	def makeBricks():
		i=5
		while i<=17:
			j=2
			while j<=18:
				wall.board[i][j]='/'
				j+=4
			i+=4

	def displayBoard():
		line1=""
		for i in range(0,84):
			line1+='X'

		print(line1)
		for i in range(1,20):
			for r in range(1,3):
				for j in range(0,21):
					for k in range(1,5):
						if(wall.board[i][j]=='B'):
							print(BLUE+wall.board[i][j]+END2,end='',flush=True)
						elif(wall.board[i][j]=='E'):
							print(RED+wall.board[i][j]+END2,end='',flush=True)
						elif(wall.board[i][j]=='/'):
							print(GREEN+wall.board[i][j]+END1,end='',flush=True)
						elif(wall.board[i][j]=='0' or wall.board[i][j]=='1' or wall.board[i][j]=='2' or wall.board[i][j]=='3'):
							print(CYAN+wall.board[i][j]+END2,end='',flush=True)
						elif(wall.board[i][j]=='e'):
							print(CYAN+wall.board[i][j]+END2,end='',flush=True)
						else:
							print(WHITE+wall.board[i][j]+END2,end='',flush=True)
				print()
		print(line1)

#x=wall()
#x.makeBoard()
#x.displayBoard()

