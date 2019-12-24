# Import the libraries required for this class.
try:
	import glfw
	from glfw.GLFW import *
	from OpenGL.GL import *
except ImportError as error:
	raise error

from fps import FPS

class Window:
	def __init__(self, width:int = 100, height:int = 100, title:str = "PyGameEngine Window", 
					   fps_limit:int = 60, resizable:bool = True,
					   max_width:int = GLFW_DONT_CARE, min_width:int = GLFW_DONT_CARE,
					   max_height:int = GLFW_DONT_CARE, min_height:int = GLFW_DONT_CARE):
		"""
			The window class that all applications should derive from.

			Arguments:
				width      : int  : The width of the window being created.
				height     : int  : The height of the window being created.
				title      : str  : The title of the window being created.
				fps_limit  : int  : The fps limit of the window being created.
				resizable  : bool : Should the glfw window be allowed to resize.
				max_width  : int  : The max width the window can be resized to.
				min_width  : int  : The min width the window can be resized to.
				max_height : int  : The max height the window can be resized to.
				min_height : int  : The min height the window can be resized to.

		"""

		self.width = width
		self.height = height
		self.title = title
		self.fps_limit = fps_limit

		self.__background = (0.0, 0.0, 0.0, 1.0)

		# Try to initialize glfw.
		if not glfw.init():
			raise RuntimeError("RunTimeError: At Window.__init__(): Failed to initialize glfw")

		# Before creating the window tell glfw if the window should be allowed to resize.
		glfw.window_hint(GLFW_RESIZABLE, resizable)

		# Try to create the window.
		self.window = glfw.create_window(self.width, self.height, self.title, None, None)
		if not self.window:
			glfw.terminate()
			raise RuntimeError("RunTimeError: At Window.__init__(): Failed to create a glfw window")

		# Set a callback function for when the user tries to resize the window.
		glfw.set_window_size_callback(self.window, self.resize)

		# Set the size limits of the window.
		glfwSetWindowSizeLimits(self.window, min_width, min_height, max_width, max_height)

	def run(self):
		"""
			run() must be called by the user to start, draw and refresh everything on the screen.

		"""

		# Initialize the windows fps.
		self.fps = FPS(1.0/self.fps_limit)

		# Check if the window should close
		while not glfw.window_should_close(self.window):

			# Set the current glfw context to self.window.
			glfw.make_context_current(self.window)

			# Set the background color (black).
			glClearColor(self.background[0], self.background[1], self.background[2], self.background[3])

			# Update/refresh the window.
			glfw.poll_events()
			glClear(GL_COLOR_BUFFER_BIT)

			# Check the fps counter to see if things should be drawn to the screen.
			if self.fps.tick(glfw.get_time()):
				self.on_run()
				glfw.swap_buffers(self.window)

		glfw.terminate()

	def on_run(self):
		"""
			on_run() should be overwritten and all the drawing and game logic should go here.
	
		"""

		pass

	def resize(self, win, width:int, height:int):
		"""
			resize() is called when the user tries to resize the window.

			Arguments:
				win    : N/A : I believe this is a pointer to the glfw window.
				width  : int : The width of the viewport.
				height : int : The height of the viewport.

		"""

		glViewport(0, 0, width, height)

	# getter and setter functions for self.__background
	@property
	def background(self):
		return self.__background

	@background.setter
	def background(self, colour:tuple = (0.0, 0.0, 0.0, 1.0)):
		print(len(colour))
		if len(colour) < 4:
			self.__background = (colour[0], colour[1], colour[2], 1.0)
		else:
			self.__background = colour

