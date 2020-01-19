#Histogram.py

"""
	Histogram-related functions
"""

#import dependencies
import matplotlib.pyplot as plt
import numpy
from . import pixel


"""
equalizeHist - function to equalize histogram that adds more contrast to images
Parameters:
	hist		I/P	dict(color:count)	
	pixels		I/P	dict(color: Pixel objects)
	equalized_hist	I/P	equalized hist 
"""
def equalizeHist(hist, pixels):
	colors = len(hist)
	pixel_num = sum(hist.values())
	new_hist = dict()
	accu_hist = hist.copy()

	#compute new colors
	for idx in hist.keys():
		prev = 0
		if idx == 0:
			prev = 0
		else:
			prev = accu_hist[idx - 1]
		accu_hist[idx] += prev	
		new_color = -calcEqualizedColor(accu_hist[idx], prev, colors, pixel_num)

		if hist[idx] > 0:
			new_hist[new_color] = pixels[idx] 

	return new_hist
"""
Histogram - function to compute histogram
Paremeters:
	arr	I/P	channel of an image need computing histogram
	res	O/P	[colors, arrays of Pixel objects, arrays of the number of colors]
"""
def calcHis(arr):
	keys = range(0, 256)
	hist = dict.fromkeys(keys, 0)
	pixels = dict.fromkeys(keys,0)

	

	#scan thru arr to find compute histogram
	for row in range(arr):
		for col in range(row):
			pix = arr[row, col]
			pixels[pix] += 1
			hist[pix].append(pixel.Pixel(row, col)) 

	return (hist, pixels)


"""
_calcEqualizedColor - function to calculate the number of pixels for each color following the Histogram Equalization
Parameters:
	color		I/P	current color
	prev_color	I/P	previous color	
	colors		I/P	total numbers of colors
	pixel_num	I/P	total number of pixels (not 0)
	res		O/P	the new num of pixels in the corresponding color
"""
def _calcEqualizedColor(color, prev_color, colors = 256, pixel_num): 
	return floor((color + prev_color) * colors / (2 * pixel_num)) 
