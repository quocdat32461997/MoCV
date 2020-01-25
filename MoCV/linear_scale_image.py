#linear_scale_image.py

#import dependencies
import numpy as np
import math
from . import histogram

__all__ = ['linear_scale']

"""
linear_scale - function to scale images linearly
"""
def linear_scale(img, A = 0, B = 255):
	#by default, the A and B are 0 and 255 respectively
	#get a nd b (smallest and largest color value) of the image that b > a

	#flatten img
	old_range = np.unique(img)
	a = np.min(old_range)
	b = np.max(old_range)
	ba = b - a
	BA = B - A

	scaled_img = img.copy()
	coef = BA / ba

	for row in range(len(scaled_img)):
		for col in range(len(scaled_img[0])):
			scaled_img[row, col] = np.floor((img[row, col] - a)* coef) + A

	return scaled_img
	

