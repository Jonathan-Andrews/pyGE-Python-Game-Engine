# pyGE-Python-Game-Engine
pyGE is a game engine for python built off OpenGl and glfw. I started building this for my use to learn more about 2d/3d graphics and the maths used behind the scenes. There is still a lot of work to be done and most of this code isn't the most effecient (I.E it doesnt make use of VBOs), but that being said, again this is just for personal use.

I don't mind if other people use this or contribute to the code, but when I get a good understanding of how game engines work then I will be going through all the code and making it more efficent.

pyGE currently has support for 2d and 3d graphics that can be translated, scaled and rotated. Individual colours for each vertex or edge of a shape is currently not supported and everything will appear as white. Because this is built off OpenGl all coordinates should be between -1 and 1, however I have also written a small script in utils that converts Gl coordinates to pixel coordinates. To create a 2d or 3d object you must provide a list of all the verticies and edges, however I have also written a script that draws prmitive shapes for you, I will also in the future be adding support for blender and other 3d modeling software.

A quick example of simple bit of code.

``` python

from window import Window
from gameObjects.object3d import Object3D

# All windows or screens should be classes and should inherit from the pyge.window.Window() class.
class Game(Window):
	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs) 
    # Pass the pearant class the *args and **kwargs such as window height and width.

    # Create a 3d Object (in this case a cube)
		self.square = Object3D(
            # Provide the OpenGL coordinates for each vertex.
            [ 
								[-.5,-.5,-.5],
								[.5,-.5,-.5],
								[.5,.5,-.5],
								[-.5,.5,-.5],

								[-.5,-.5,.5],
								[.5,-.5,.5],
								[.5,.5,.5],
								[-.5,.5,.5],
						],

            # Providing edges is optional, if they are not given then the shape will be drawn connecting the verticies as given.
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
              # draw_types tells the Object3D class how to draw the object, other types include 'triangles', 'polygon'


  # on_run() is called by the pearent class and is where all you're drawing and game logic should go.
	def on_run(self):
		self.square.draw() # Draw the cube
    
    # Rotate the cube in all 3 dimentions
    # NOTE: rotation transformations are based on the polar coordinate system.
    self.square.rotate_x(0.0078)
		self.square.rotate_y(0.0078)
		self.square.rotate_z(0.0078)

if __name__ == "__main__":
	game = Game(400, 400, title='test', fps_limit=60, resizable=False)
	game.run() # This function should be called to start the window and to constantly refresh it. 
  #vNOTE: game.run() is different from game.on_run()

```
