#histogram.py

#import dependencies
import numpy as np
import math
__all__ = ['eq_hist', 'histogram', 'linear_scale_hist']

"""
eq_hist - function to equalize histogram
Parameters:
	hist		I/P	histogram of image
	colors		I/P	possible colors of image
	img_size	I/P	size of image
	equalized_hist	O/P	equalized histogram
"""
def eq_hist(hist, colors, img_size):
	hist = hist * colors / (2 * img_size)
	cum_hist = hist.cumsum() #Cummulative histogram
	equalized_hist = np.floor(cum_hist)

	return equalized_hist
	
"""
linear_scale_hist - function to scale images linearly

"""
def linear_scale_hist(hist, A = 0, B = 255):
	#by default, the two ends of the new range is A = 0, B = 255
	#get two ends of the current range is a, b that b > a
	old_range = np.where(hist > 0)
	a = np.min(old_range)
	b = np.max(old_range)

	ba = b - a
	BA = B - A	

	new_hist = np.array([0] * 256) 
	for idx in np.nditer(old_range):
		new_idx = np.int((idx - a) * BA / ba + A)
		new_hist[new_idx] = hist[idx] 
	return new_hist

"""
histogram - function to comptue histogram of an image
Parameters:
	img_channel	I/P	image channel input in default/numpy array
	hist		O/P	computed histogram by numpy
"""
def histogram(img_channel):
	#hist, _ = np.histogram(im_channele, bins = 256, range = (0, 256))	
	hist = np.array([0] * 256)

	height = len(img_channel)
	width = len(img_channel[0])
	for row in range(height):
		for col in range(width):
			hist[img_channel[row, col]] += 1
			 
	return hist
