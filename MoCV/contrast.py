#contrastImage.py

#import dependencies
import numpy as np
import cv2
from . import histogram

__all__ = ['upcontrastImage']

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
	#hist, bins  = np.histogram(image.flatten(), bins = 256, range = (0, 255))
	hist = histogram.histogram(image)

	#equalize histogram
	colors = 256

	stretched_hist = histogram.eq_hist(hist, colors, image.size)

	#enhance image contrast
	enhanced_image = np.zeros(shape = image.shape)

	height = len(image)
	width = len(image[0])	
	for row in range(height):
		for col in range(width):
			enhanced_image[row, col] = stretched_hist[image[row, col]]

	return enhanced_image
