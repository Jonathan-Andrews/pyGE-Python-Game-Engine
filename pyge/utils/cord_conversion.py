def pixel_to_gl(screen_dims:list, cords:list):
	"""
		Converts coordinates from pixel (width and height of screen in pixels) to gl coordinates (-1 to 1).

		Arguments:
			screen_dims : list : A list of the width, height (also depth if dealing with 3d) of the screen in pixels.
			cords       : list : The coordinates that will be converted.

		NOTE: I say that screen_dims can also have a 3rd dimension when in reality screens are 2d. 
		However when making a 3d object in GL, the z axis is represented with values between -1 and 1.
		So that is why i'm saying the user can do this, however i might late change this to just allowing for 2 dimensions.


	"""

	new_cords = []

	if len(screen_dims) != len(cords[0]):
		raise valueError("The length of screen_dims is not the same number of dimensions a point is being plotted in.")

	for cord in cords:		
		new_cords.append([])
		for i in range(len(cord)):
			new_cords[-1].append(map_to_range(0, screen_dims[i], -1, 1, cord[i]))

	return new_cords

def gl_to_pixel(screen_dims, cords):
	"""
		Converts coordinates from gl coordinates (-1 to 1) to pixel coordinates (width and height of screen in pixels).

		Arguments:
			screen_dims : list : A list of the width, height (also depth if dealing with 3d) of the screen in pixels.
			cords       : list : The coordinates that will be converted.

		NOTE: I say that screen_dims can also have a 3rd dimension when in reality screens are 2d. 
		However when making a 3d object in GL, the z axis is represented with values between -1 and 1.
		So that is why i'm saying the user can do this, however i might late change this to just allowing for 2 dimensions.


	"""

	new_cords = []

	if len(screen_dims) != len(cords[0]):
		raise valueError("The length of screen_dims is not the same number of dimensions a point is being plotted in.")

	for cord in cords:		
		new_cords.append([])
		for i in range(len(cord)):
			new_cords[-1].append(map_to_range(-1, 1, 0, screen_dims[i], cord[i]))

	return new_cords

def map_to_range(min_1:float, max_1:float, min_2:float, max_2:float, value:float):
	"""
		This function maps a number of one range to that of another range.

		Arguments:
			min_1 : float/int : The lowest value of the range you're converting from.
			max_1 : float/int : The highest value of the range you're converting from.
			min_2 : float/int : The lowest value of the range you're converting to.
			max_2 : float/int : The highest value of the range you're converting to.
			value : float/int : The value that will be converted.

		Example:
			mapping a RGB value between 0 - 255 to a RGB value between 0 - 1
			map_to_range(0, 255, 0, 1, 127.5) -> will return 0.5

	"""

	binary_range = (value - min_1) / (max_1 - min_1)
	return binary_range * (max_2 - min_2) + min_2