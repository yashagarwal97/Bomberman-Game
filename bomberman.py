from __future__ import print_function
import signal,copy
import sys,os
from person import *
from alarm import *
from getchunix import *
from grid import *
from bomb import *
from enemy import *
import time
#from pynput.keyboard import Key,Listener


class bomberman(person):
	def __init__(self):
		super().__init__(1,1)
		self._type="bomberman"
		self._life=3
		self.bombs=[]
		self._points=0

	def drop_bomb(self,x,y):
		xx=bomb(x,y)
		self.bombs.append(xx)

	getch= GetchUnix()
	def alarmHandler(signum,frame):
		raise AlarmException

	def inp(timeout=1):
		signal.signal(signal.SIGALRM,bomberman.alarmHandler)
		signal.alarm(timeout)
		try:
			text=bomberman.getch()
			signal.alarm(0)
			return text
		except AlarmException:
			pass
		signal.signal(signal.SIGALRM,signal.SIG_IGN)
		return ''

	def die(self):
		self._life-=1
		if self._life==0:
			wall.displayBoard()
			print("GAME OVER")
			print("Final Score="+str(self._points))
			sys.exit(0)
		else:
			self.x=1
			self.y=1
			for bom in self.bombs:
				bom.after_blast()
			self.bombs=[]
			wall.board[self.x][self.y]='B'

	
	def moveleft(self):
		dx=0
		dy=-1
		if(wall.board[self.x+dx][self.y+dy]==' '):
			wall.board[self.x][self.y]=' '
			self.x=self.x+dx
			self.y=self.y+dy
			wall.board[self.x][self.y]='B'
		elif(wall.board[self.x+dx][self.y+dy]=='E'):
			wall.board[self.x][self.y]=' '
			self.die()

	def moveright(self):
		dx=0
		dy=1
		if(wall.board[self.x+dx][self.y+dy]==' '):
			wall.board[self.x][self.y]=' '
			self.x=self.x+dx
			self.y=self.y+dy
			wall.board[self.x][self.y]='B'
		elif(wall.board[self.x+dx][self.y+dy]=='E'):
			wall.board[self.x][self.y]=' '
			self.die()

	def moveup(self):
		dx=-1
		dy=0
		if(wall.board[self.x+dx][self.y+dy]==' '):
			wall.board[self.x][self.y]=' '
			self.x=self.x+dx
			self.y=self.y+dy
			wall.board[self.x][self.y]='B'
		elif(wall.board[self.x+dx][self.y+dy]=='E'):
			wall.board[self.x][self.y]=' '
			self.die()

	def movedown(self):
		dx=1
		dy=0
		if(wall.board[self.x+dx][self.y+dy]==' '):
			wall.board[self.x][self.y]=' '
			self.x=self.x+dx
			self.y=self.y+dy
			wall.board[self.x][self.y]='B'
		elif(wall.board[self.x+dx][self.y+dy]=='E'):
			wall.board[self.x][self.y]=' '
			self.die()


	def start_game(self):
		wall.makeBoard()
		wall.makeBricks()
		enemy.e=[]
		enemy.e.append(enemy(15,1))
		enemy.e.append(enemy(1,15))
		enemy.e.append(enemy(9,9))
		enemy.e.append(enemy(19,5))
		enemy.e.append(enemy(5,19))
		cc=0
		wall.board[self.x][self.y]='B'
		for cc in range(0,5):
			wall.board[enemy.e[cc].x][enemy.e[cc].y]='E'
		

		while(True):
			#time.sleep(0.05)
			if(len(self.bombs)!=0):
				if(wall.board[self.bombs[0].x][self.bombs[0].y]!='B' and self.bombs[0].timer>=1):
					wall.board[self.bombs[0].x][self.bombs[0].y]=(str)(self.bombs[0].timer-1)
			os.system('tput reset')
			wall.displayBoard()
			print("SCORE="+str(self._points)+"          LIFE="+str(self._life))

			#time.sleep(0.1)
			#listner()
			if len(self.bombs)!=0:
				bom=self.bombs[0]
				bom.timer-=1
				if bom.timer==0:
					dic=bom.blast()
					self._points+=dic["newpoints"]
					if len(enemy.e)==0:
						wall.displayBoard()
						print("Woah! You killed all your enemies. YOU WIN.")
						print("Final Score="+str(self._points))
						sys.exit(0)
					if dic["deaths"]==1:
						self.die()
						bom.after_blast()
						continue
				elif bom.timer==-1:
					bom.after_blast()
					self.bombs.pop()
			

			k=bomberman.inp()
			if k=='q':
				print("GAME OVER")
				print("Final Score="+str(self._points))
				sys.exit(0)
			elif k=='a':
				self.moveleft()
			elif k=='w':
				self.moveup()
			elif k=='d':
				self.moveright()	
			elif k=='s':
				self.movedown()
			elif k=='b':
				if len(self.bombs)==0:
					self.drop_bomb(self.x,self.y)
			
			for cc in range(0,len(enemy.e)):
				death=enemy.e[cc].direction()
				if(death==1):
					self.die()
					break

obj=bomberman()
'''def on_press(key):
	k=key.char
	try:
		if k=='a':
			obj.moveleft()
		elif k=='w':
			obj.moveup()
		elif k=='d':
			obj.moveright()	
		elif k=='s':
			obj.movedown()
	except:
		pass
	return False

def listner():
	with Listener(on_press=bomberman.on_press) as listener:
		listener.join()
'''

obj.start_game()		
