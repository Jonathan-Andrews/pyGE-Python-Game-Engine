from math import sin, cos

from OpenGL.GL import *

class Object3D:
	def __init__(self, verticies:list, edges:list = [], draw_type:str = 'polygon'):
		"""
			The Object2D class acts as a 2d sprite.

			Arguments:
				verticies : list  : A list of the cords for the verticies, should look like [[x1, y1], [x2, y2]] * A line.
				edges     : list  : A list of the numbered verticies to join, should look like [[0, 1]] * Connecting the 2 verticies together into a line.
				draw_type : str   : How to draw the square I.E with triangles, with lines.

		"""

		self.verticies = verticies
		self.edges = edges
		self.draw_type = draw_type

	def draw(self):
		"""
			draw() draws the 2d object based on the given verticies and edges.

		"""

		# Apply orthographic project to the z coordinate of each vertex.
		projection = []

		for i in range(len(self.verticies)):
			x = self.verticies[i][0]
			y = self.verticies[i][1]
			projection.append([x,y])

		if self.draw_type == 'polygon':
			glBegin(GL_POLYGON)
		elif self.draw_type == 'triangles':
			glBegin(GL_TRIANGLES)
		elif self.draw_type == 'lines':
			glBegin(GL_LINES)
		else:
			print(f"TypeError: At Object2D().draw(): draw_type {self.draw_type} is not know, set to polygon by default.")
			glBegin(GL_POLYGON)

		# Draw if the user has provided edges to connect up the verticies.
		if len(self.edges) > 0:
			for i in range(len(self.edges)):
				for j in range(len(self.edges[i])):
					glVertex2f(projection[self.edges[i][j]][0], projection[self.edges[i][j]][1])

		# Draw if the user has only provided verticies and draw in the order they were given.
		else:
			for v in projection:
				glVertex2f(v[0], v[1])

		glEnd()

	def move(self, x_move:float = 0, y_move:float = 0, z_move:float = 0):
		"""
			move() applies movement/translation transformations to each vertex of the 2d object.

			Arguments:
				x_move : float : How much to move the x cord of each vertex.
				y_move : float : How much to move the y cord of each vertex.
				z_move : float : How much to move the y cord of each vertex.

		"""

		for i in range(len(self.verticies)):
			self.verticies[i][0] += x_move
			self.verticies[i][1] += y_move
			self.verticies[i][2] += z_move

	def scale(self, x_scale:float = 0, y_scale:float = 0, z_scale:float = 0):
		"""
			scale() applies scale transformations to each vertex of the 2d object.

			Arguments:
				x_scale : float : How much to scale the x cord of each vertex.
				y_scale : float : How much to scale the y cord of each vertex.
				z_scale : float : How much to scale the z cord of each vertex.

		"""

		for i in range(len(self.verticies)):
			self.verticies[i][0] *= 1 + x_scale
			self.verticies[i][1] *= 1 + y_scale
			self.verticies[i][2] *= 1 + z_scale

	def rotate_x(self, theta:float = 0):
		"""
			rotate() applies rotation transformations to each vertex based on the polar coordinate system. 

			Arguments:
				theta : float : The angle to be added onto the current angle of each vertex

		"""

		for i in range(len(self.verticies)):
			y_rotated = (self.verticies[i][1]*cos(theta)) + (-1*self.verticies[i][2]*sin(theta))
			z_rotated = (self.verticies[i][1]*sin(theta)) + (self.verticies[i][2]*cos(theta))

			self.verticies[i][1] = y_rotated
			self.verticies[i][2] = z_rotated


	def rotate_y(self, theta:float = 0):
		"""
			rotate() applies rotation transformations to each vertex based on the polar coordinate system. 

			Arguments:
				theta : float : The angle to be added onto the current angle of each vertex

		"""

		for i in range(len(self.verticies)):
			x_rotated = (self.verticies[i][0]*cos(theta)) + (self.verticies[i][2]*sin(theta))
			z_rotated = (-1*self.verticies[i][0]*sin(theta)) + (self.verticies[i][2]*cos(theta))

			self.verticies[i][0] = x_rotated
			self.verticies[i][2] = z_rotated


	def rotate_z(self, theta:float = 0):
		"""
			rotate() applies rotation transformations to each vertex based on the polar coordinate system. 

			Arguments:
				theta : float : The angle to be added onto the current angle of each vertex

		"""

		for i in range(len(self.verticies)):
			x_rotated = (self.verticies[i][0]*cos(theta)) + (-1*self.verticies[i][1]*sin(theta))
			y_rotated = (self.verticies[i][0]*sin(theta)) + (self.verticies[i][1]*cos(theta))

			self.verticies[i][0] = x_rotated
			self.verticies[i][1] = y_rotated
