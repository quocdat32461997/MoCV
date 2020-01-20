#contrastImage.py

import numpy as np
import math
import cv2

"""
upcontrastImage - function to increase contrast of an image
Parameters:
	image		I/P	image need increasing contrast
	enhanced_image	O/P	image after being increased contrast
"""
def upcontrastImage(image):
	"""
	Perform Histogram equalization to strech images in order to increase contrast
	"""

	#compute histogram
	histo, bins  = np.histogram(image.flatten(), bins = 256, range = (0, 255))

	#equalize histogram
	k = 256
	n = image.size

	histo = histo * k / (2 * n) 
	cum_histo = histo.cumsum() #Cumulative Histo	
	cums_histo = np.floor(cum_histo)

	#enhance image contrast
	enhanced_image = np.zeros(shape = image.shape)

	for row in range(image.shape[0]):
		for col in range(image.shape[1]):
			enhanced_image[row, col] = cum_histo[image[row, col]]

	return enhanced_image
