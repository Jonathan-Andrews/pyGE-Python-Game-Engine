"""
	A list of functions that return gameObject classes of primitive shapes.

"""

from math import cos, sin, pi

from .object2d import Object2D

# ----------------------------------------------------------------------------------------
def draw_square(x:float, y:float, height:float = 1, width:float = 1, fill:bool = False):
	"""
		Returns a Object2D class that draws a square

		Arguments:
			x         : float : The x starting point of the square I.E the bottom left corner.
			y         : float : The y starting point of the square I.E the bottom left corner.
			height    : float : The height of the square.
			width     : float : The width of the square.
			fill	  : bool  : Should the shape be filled.

	"""

	# Calculate the other x and y cords.
	cords = [[x, y]]
	cords.append([x+width, y])
	cords.append([x+width, y+height])
	cords.append([x, y+height])

	if fill:
		return Object2D(cords, [[0,1,2],[0,3,2]], draw_type='triangles')
	else:
		return Object2D(cords, [[0,1],[1,2],[2,3],[3,0]], draw_type='lines')

# ----------------------------------------------------------------------------------------
def draw_triangle(cords:list, fill=False):
	"""
		Returns a Object2D class that draws a triangle

		Arguments:
			cords : float : The x and y cords for each vertex of the triangle, should look like [[x1,y1]...]
			fill  : bool  : Should the shape be filled.

	"""

	if len(cords) > 3:
		raise TypeError("At primitives.draw_triangle(): The length of the given cords is greater than 3, a triangle should only have 3 cords.")

	if fill:
		return Object2D(cords, [[0,1,2]], draw_type='triangles')
	else:
		return Object2D(cords, [[0,1],[1,2],[2,0]], draw_type='lines')

# ----------------------------------------------------------------------------------------
def draw_circle(center_x:float, center_y:float, radius:float = 0.3, segments:int = 360, fill:bool=False):
	"""
		Returns an Object2D class that draws a circle 

		Arguments:
			center_x  : float : The x cord for the center of the circle.
			center_y  : float : The y cord for the center of the circle.
			radius 	  : float : The radius of the circle.
			segments  : int   : How many segments to make the circle from.
			fill	  : bool  : Should the shape be filled.

	"""

	edges = []
	cords = []

	for i in range(segments):
		theta = (2 * pi * i)/segments # Get the current angle
		x = radius * cos(theta) + center_x # Get the x cord
		y = radius * sin(theta) + center_y # Get the y cord

		cords.append([x, y])

	if fill:
		cords.insert(0, [center_x, center_y])
		for i in range(len(cords)-2):
			edges.append([0, i+1, i+2])

		edges.append([0, segments, 1]) # Fixes a little glitch
		return Object2D(cords, edges, draw_type='triangles')

	else:
		for i in range(len(cords)-1):
			edges.append([i, i+1])

		edges.append([segments-1,0]) # Fixes a little glitch
		return Object2D(cords, edges, draw_type='lines')

# ----------------------------------------------------------------------------------------
def draw_arc(center_x:float, center_y:float, radius:float = 0.3, arc_angle:float = 90, start_angle:float = 0, segments:int = 360, fill:bool=False):
	"""
		Returns an Object2D class that draws a circle, angles should not be given in radians.

		Arguments:
			center_x    : float : The x cord for the center of the circle.
			center_y    : float : The y cord for the center of the circle.
			radius 	    : float : The radius of the circle.
			arc_angle   : float : The angle of the arc.
			start_angle : float : The angle from where the arc should start from.
			segments    : int   : How many segments to make the circle from.
			fill	    : bool  : Should the shape be filled.

	"""
	
	edges = []
	cords = []

	for i in range(segments):
		theta = ((arc_angle * pi * i/180) / segments) + (start_angle*90/180) # Get the current angle
		x = radius * cos(theta) + center_x # Get the x cord
		y = radius * sin(theta) + center_y # Get the y cord

		cords.append([x, y])

	if fill:
		cords.insert(0, [center_x, center_y-(center_y-cords[0][1])])
		for i in range(len(cords)-2):
			edges.append([0, i+1, i+2])
		return Object2D(cords, edges, draw_type='triangles')

	else:		
		for i in range(len(cords)-1):
			edges.append([i, i+1])
		return Object2D(cords, edges, draw_type='lines')
