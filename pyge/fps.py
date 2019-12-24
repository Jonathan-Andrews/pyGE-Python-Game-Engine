"""
	A quick little script to handle the fps_limit and similar things

"""

class FPS:
	def __init__(self, fps_limit: int):
		"""
			The FPS class handles the fps_limit of a pyGE window.

			Arguments:
				fps_limit : int : The fps limit of the pyGE window.

		"""

		self.fps_limit = fps_limit
		self.last_update_time = 0

	def tick(self, time_now: float):
		"""
			tick() calculates the amount of time that has passed since its last 'return 1' to see if it should do it gain.

			Arguments:
				time_now : float : The output from glfw.get_time()

		"""

		if time_now - self.last_update_time >= self.fps_limit:
			self.last_update_time = time_now
			return 1
		else:
			return 0