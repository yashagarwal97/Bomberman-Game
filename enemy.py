from person import *
#from bomberman import *
from grid import *
from random import randint

class enemy(person):
	e=[]
	def __init__(self,x,y):
		super().__init__(x,y)
		self._type="enemy"

	def die(self):
		temp=-1
		l=len(enemy.e)
		for i in range(0,l):
			if(enemy.e[i]==self):
				temp=i
				break
		enemy.e.pop(temp)

	# 1-up,2-down,3-left,4-right
	def moveleft(self):
		dx=0
		dy=-1
		flag=0
		if(wall.board[self.x+dx][self.y+dy]==' '):
			if (self.x+dx!=1 or self.y+dy!=1):
				wall.board[self.x][self.y]=' '
				self.x=self.x+dx
				self.y=self.y+dy
				wall.board[self.x][self.y]='E'
		elif(wall.board[self.x+dx][self.y+dy]=='B'):
			if (self.x+dx!=1 or self.y+dy!=1):
				flag=1
				wall.board[self.x][self.y]=' '
				self.x=self.x+dx
				self.y=self.y+dy
				wall.board[self.x][self.y]='E'
				#print(wall.board[self.x][self.y])
		return flag
		#	obj.die()

	def moveright(self):
		dx=0
		dy=1
		flag=0
		if(wall.board[self.x+dx][self.y+dy]==' '):
			if (self.x+dx!=1 or self.y+dy!=1):
				wall.board[self.x][self.y]=' '
				self.x=self.x+dx
				self.y=self.y+dy
				wall.board[self.x][self.y]='E'
		elif(wall.board[self.x+dx][self.y+dy]=='B'):
			if (self.x+dx!=1 or self.y+dy!=1):
				flag=1
				wall.board[self.x][self.y]=' '
				self.x=self.x+dx
				self.y=self.y+dy
				wall.board[self.x][self.y]='E'
				#print(wall.board[self.x][self.y])
		return flag

	def moveup(self):
		dx=-1
		dy=0
		flag=0
		if(wall.board[self.x+dx][self.y+dy]==' '):
			if (self.x+dx!=1 or self.y+dy!=1):
				wall.board[self.x][self.y]=' '
				self.x=self.x+dx
				self.y=self.y+dy
				wall.board[self.x][self.y]='E'
		elif(wall.board[self.x+dx][self.y+dy]=='B'):
			if (self.x+dx!=1 or self.y+dy!=1):
				flag=1
				wall.board[self.x][self.y]=' '
				self.x=self.x+dx
				self.y=self.y+dy
				wall.board[self.x][self.y]='E'
				#print(wall.board[self.x][self.y])
		return flag

	def movedown(self):
		dx=1
		dy=0
		flag=0
		if(wall.board[self.x+dx][self.y+dy]==' '):
			if (self.x+dx!=1 or self.y+dy!=1):
				wall.board[self.x][self.y]=' '
				self.x=self.x+dx
				self.y=self.y+dy
				wall.board[self.x][self.y]='E'
		elif(wall.board[self.x+dx][self.y+dy]=='B'):
			if (self.x+dx!=1 or self.y+dy!=1):
				flag=1
				wall.board[self.x][self.y]=' '
				self.x=self.x+dx
				self.y=self.y+dy
				wall.board[self.x][self.y]='E'
				#print(wall.board[self.x][self.y])
		return flag

	def direction(self):
		while(True):
			n=randint(1,4)
			a=self.x
			b=self.y
			if(n==1):
				ret=self.moveup()
				if (self.x!=a or self.y!=b):
					return ret
			elif(n==2):
				ret=self.movedown()
				if (self.x!=a or self.y!=b):
					return ret
			elif(n==3):
				ret=self.moveleft()
				if (self.x!=a or self.y!=b):
					return ret
			elif(n==4):
				ret=self.moveright()
				if (self.x!=a or self.y!=b):
					return ret


