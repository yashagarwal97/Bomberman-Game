from grid import *
from enemy import *

class bomb:
	def __init__(self,x,y):
		self.timer=4		
		self.x=x
		self.y=y

	def blast(self):
		a=self.x
		b=self.y
		dic={}
		newpoints=0
		deaths=0
		if (wall.board[a][b+1]!='X'):
			if (wall.board[a][b+1]=='/'):
				newpoints+=20
			elif (wall.board[a][b+1]=='E'):
				newpoints+=100
				for ob in enemy.e:
					if (ob.x==a and ob.y==b+1):
						ob.die()
						break
			elif (wall.board[a][b+1]=='B'):
				deaths=1
			wall.board[a][b+1]='e'
		
		if (wall.board[a+1][b]!='X'):
			if (wall.board[a+1][b]=='/'):
				newpoints+=20
			elif (wall.board[a+1][b]=='E'):
				newpoints+=100
				for ob in enemy.e:
					if (ob.x==a+1 and ob.y==b):
						ob.die()
						break
			elif (wall.board[a+1][b]=='B'):
				deaths=1
			wall.board[a+1][b]='e'

		if (wall.board[a][b-1]!='X'):
			if (wall.board[a][b-1]=='/'):
				newpoints+=20
			elif (wall.board[a][b-1]=='E'):
				newpoints+=100
				for ob in enemy.e:
					if (ob.x==a and ob.y==b-1):
						ob.die()
						break
			elif (wall.board[a][b-1]=='B'):
				deaths=1
			wall.board[a][b-1]='e'			
		
		if (wall.board[a-1][b]!='X'):
			if (wall.board[a-1][b]=='/'):
				newpoints+=20
			elif (wall.board[a-1][b]=='E'):
				newpoints+=100
				for ob in enemy.e:
					if (ob.x==a-1 and ob.y==b):
						ob.die()
						break
			elif (wall.board[a-1][b]=='B'):
				deaths=1
			wall.board[a-1][b]='e'
		
		if (wall.board[a][b]!='X'):
			if (wall.board[a][b]=='/'):
				newpoints+=20
			elif (wall.board[a][b]=='E'):
				newpoints+=100
				for ob in enemy.e:
					if (ob.x==a and ob.y==b):
						ob.die()
						break
			elif (wall.board[a][b]=='B'):
				deaths=1
			wall.board[a][b]='e'
		dic["newpoints"]=newpoints
		dic["deaths"]=deaths
		return dic

	def after_blast(self):
		a=self.x
		b=self.y
		if (wall.board[a][b+1]=='e'):
			wall.board[a][b+1]=' '
		if (wall.board[a+1][b]=='e'):
			wall.board[a+1][b]=' '
		if (wall.board[a][b-1]=='e'):
			wall.board[a][b-1]=' '			
		if (wall.board[a-1][b]=='e'):
			wall.board[a-1][b]=' '
		if (wall.board[a][b]=='e' or wall.board[a][b]=="3" or wall.board[a][b]=="2" or wall.board[a][b]=="1" or wall.board[a][b]=="0"):
			wall.board[a][b]=' '



		
