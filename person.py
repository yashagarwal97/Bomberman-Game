from grid import *

class person:
	def __init__(self,x,y):
		self.x=x
		self.y=y
'''	def moveleft(self,c):
		dx=0
		dy=-1
		if(wall.board[self.x+dx][self.y+dy]==' '):
			wall.board[self.x][self.y]=' '
			self.x=self.x+dx
			self.y=self.y+dy
			wall.board[self.x][self.y]=c

	def moveright(self,c):
		dx=0
		dy=1
		if(wall.board[self.x+dx][self.y+dy]==' '):
			wall.board[self.x][self.y]=' '
			self.x=self.x+dx
			self.y=self.y+dy
			wall.board[self.x][self.y]=c

	def moveup(self,c):
		dx=-1
		dy=0
		if(wall.board[self.x+dx][self.y+dy]==' '):
			wall.board[self.x][self.y]=' '
			self.x=self.x+dx
			self.y=self.y+dy
			wall.board[self.x][self.y]=c

	def movedown(self,c):
		dx=1
		dy=0
		if(wall.board[self.x+dx][self.y+dy]==' '):
			wall.board[self.x][self.y]=' '
			self.x=self.x+dx
			self.y=self.y+dy
			wall.board[self.x][self.y]=c
'''