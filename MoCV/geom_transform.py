#geom_transform.py
"""
Module: geom_transform - implement geometric transformation
Last updated: 02/02/2020
"""

#import dependencies
import numpy as np
__all__ = ['translation', 'nn', 'linear_interpolate']

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
	h_ratio		I/P	scaling ratio for height
	w_ratio		I/P	scaling ratio for width
			O/P	color-filled image
"""
def nn(origi_img, scaled_img, h_ratio, w_ratio):
	"""
		nearest neighbor - a linear interpolation to fill pixels of scaled images by picking the neartest pixels 
	"""

	#get height and width of scaled_img and origi_img
	height = scaled_img.shape[0]
	h = origi_img.shape[0]
	width = scaled_img.shape[1]
	w = origi_img.shape[1]
	
	#visit each pixel and map back to original image
	for row in range(height):
		x = round(row / h_ratio) 
		if not x in range(h): #if out-of-bound, fill w/ zeros
			continue

		for col in range(width):
			y = round(col / w_ratio)

			#map to the nearest pixels
			if not y in range(w): #if out-of-bound, fill with zero 
				continue
			else:
				scaled_img[row, col] = origi_img[x, y]
	return scaled_img
	"""		end of nn		"""


"""
linear_interpolate - function to bilinear interpolatation trasformation
Parameters:
	origi_img	I/P	image input
	scaled_img	I/P	scaled image input - 2d array of mapped pixels
	h_ratio		I/P	scaling ratio for height
	w_ratio		I/P	scaling ratio for width
			O/P	transformed image
"""
def linear_interpolate(origi_img, scaled_img, h_ratio, w_ratio):
	#get height and width of scaled_img and origi_img
	height = scaled_img.shape[0]
	width = scaled_img.shape[1]
	h = origi_img.shape[0]
	w = origi_img.shape[1]

	#visit each pixel and map back to original image
	#extra variables are pre-computed in order to prevent re-computing within for loops
	for row in range(height):
		#get x, floor and ceil of x, compute weight b
		x = row / h_ratio
		fx = np.int(np.floor(x))
		cx = np.int(np.ceil(x))

		#if out-of-bound, fill w/ zero
		if not fx in range(h) or not cx in range(h):
			continue
		#compute weight
		b = x - fx
		nb = 1 - b
			
		for col in range(width):
			#get y, floor and ceil of y, and compute weight a
			y = col / w_ratio
			fy = np.int(np.floor(y))
			cy = np.int(np.ceil(y))
			
			#compute transformed pixels
			if fy in range(w) and cy in range(w): #if out-of-bound, fill with zeros 
				#compute weight
				a = y - fy
				na = 1 - a
				scaled_img[row, col] = na * nb * origi_img[fx, fy] + na * b * origi_img[fx, cy] + a * nb * origi_img[cx, fy] + a * b * origi_img[cx, cy]
			else:
				pass
	return scaled_img
	"""		linear_interpolate		"""
