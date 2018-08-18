BOMBERMAN GAME

The game has been implemented using python3. For rendering colours to the text displayed, the termcolor library has been imported.

Instruction to run the game:
-> Open terminal
-> python3 bomberman.py

Game Controls: 
	w = up 
	a = left 
	s = down 
	d = right 
	b = plant bomb 
	q = quit

Colour scheme:
	Bomberman(B) - Blue
	Enemies(E) - Red
	Bomb(displayed as Timer) - Cyan
	Wall(X) - White
	Destructible Bricks(/) - Green
	Explosion(e) - Cyan 

Game Specifications:
* Bomberman has 3 lives.
* Bomberman gets 100 points on killing an enemy and 20 points for destroying a brick.
* Bomb has a timer which is displayed where the bomb is dropped,timer goes from 3 -> 2 -> 1 -> 0 -> explosion. Timer is not visible when the bomberman occupies the same place as the bomb.  

