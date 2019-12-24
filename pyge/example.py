import random

from window import Window
from gameObjects.object2d import Object2D
from gameObjects.object3d import Object3D
from gameObjects.primitives import *

class Game(Window):
	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)

		self.square = Object3D([
								[-.5,-.5,-.5],
								[.5,-.5,-.5],
								[.5,.5,-.5],
								[-.5,.5,-.5],

								[-.5,-.5,.5],
								[.5,-.5,.5],
								[.5,.5,.5],
								[-.5,.5,.5],
							   ],

							   [
							   	[0,1],
							   	[1,2],
							   	[2,3],
							   	[3,0],

							   	[4,5],
							   	[5,6],
							   	[6,7],
							   	[7,4],

							   	[0,4],
							   	[1,5],
							   	[2,6],
							   	[3,7]
							   ], draw_type='lines')	


	def on_run(self):
		self.square.draw()
		self.square.rotate_x(0.0078)
		self.square.rotate_y(0.0078)
		self.square.rotate_z(0.0078)

if __name__ == "__main__":
	game = Game(400, 400, title='test')
	game.run()

"""
	TODO:
		ADD USER INPUT.
		ALLOW USER TO ADD COLOURS TO VERTICIES AND FACES AND STUFF.

"""