#geom_transform.py
"""
Module: geom_transform - implement geometric transformation
Last updated: 02/02/2020
"""

#import dependencies
import numpy as np
__all__ = ['translation', 'nn']

"""
translation - function to move the image with alpha and beta spaces
Parameters:
	image	I/P	the image input
	alpha	I/P	the num of spaces to move images horizontally
	beta	I/P	the num of spaces to move images vertically
	new_img	O/P	the moved image
"""
def translation(image, alpha, beta):
	#check alpha and beta in image range
	try:
		if alpha > image.shape[1] or beta > image.shape[0]:
			 raise NameError("Translation Error")
	except NameError:
		print('Alpha of ' + str(alpha) or ' Beta of ' + str(beta) + ' is out of image shape.')

	new_img = np.array([[255] * image.shape[1]] * image.shape[0])

	height = new_img.shape[0]
	width = new_img.shape[1]
	for row in range(height):
		if row + alpha in range(height):
			for col in range(width):
				if col + beta in range(width):
					new_img[row, col] = image[row + alpha, col + beta] 

	return new_img
"""		end of translation		"""

"""
nn - function nearest neigbor to map pixels of scaled images to the original images for image interpolation. By default, assume that scale around (0, 0)
Parameters:
	orgi_img	I/P	original image input
	scaled_img	I/P	scaled image input - 2d array of mapped pixels
			O/P	color-filled image
"""
def nn(origi_img, scaled_img):
	"""
		nearest neighbor - a linear interpolation to fill pixels of scaled images by picking the neartest pixels 
	"""

	#get height and width of scaled_img and origin_img
	height = scaled_img.shape[0]
	h = origi_img.shape[0]
	width = scaled_img.shape[1]
	w = origi_img.shape[1]
	
	#get scaling ratio of width and height
	h_ratio = origi_img.shape[0] / scaled_img.shape[0]
	w_ratio = origi_img.shape[1] / scaled_img.shape[1]
	
	#visit each pixel and map back to original image
	for row in range(height):
		for col in range(width):
			x = round(row * h_ratio) #get scaled_pixels
			y = round(col * w_ratio)

			#map to the nearest pixels
			if not x in range(h) or not y in range(w): #if out-of-bound, fill with zero 
				scaled_img[row, col] = 0
			else:
				scaled_img[row, col] = origi_img[x, y]
	return scaled_img
"""		end of nn		"""
	
