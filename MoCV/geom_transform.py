#geom_transform.py
"""
Module: geom_transform - implement geometric transformation
Last updated: 02/02/2020
"""

#import dependencies
import numpy as np
__all__ = ['translation']

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
