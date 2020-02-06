#img_func.py
"""
Module: image_function - module to implement resize (zoom in /out), rotate, and flip images
Last udpated: Feb. 2, 2020
"""

#import dependencies
import numpy as np
from . import geom_transform as gtf
__all__ = ['shift', 'scale_nn', 'scale_lp']

"""
shift - function to shift images
Parameters:
	img	I/P	image input
	alpha	I/P	the num of spaces shift horizontally
	beta 	I/P	the num of spaces shift vertically
		O/P	shifted image
"""
def shift(img, alpha, beta):
	#call Translation algorithm from Geometric Transform to shfit images by alpha and beta
	return gtf.translation(img, alpha, beta) 
	"""		end of shift		"""



"""
scale_nn - function to scale images w/o changing its gray-scale levels by nearest neighor interpolating technique
Parameters:
	img		I/P	image input
	h_ratio		I/P	ratio for scaling height
	w_ratio		I/P	ratio for scaling width
	scaled_img	O/P	scaled image output
"""
def scale_nn(img, h_ratio, w_ratio = 0):
	#Assume to scale around (0, 0)
	assert(h_ratio != 0), "Ratio cannot be zero or 0" #scaling ratio cannot be zero or 0
	h_ratio = round(h_ratio)
	w_ratio = round(w_ratio)
	if w_ratio == 0: #only one given scaling ratio
		w_ratio = h_ratio

	#get width and height after scaling
	scaled_w = img.shape[1] * w_ratio #scaling ratio always integer as image size not decimal
	scaled_h = img.shape[0] * h_ratio

	#create empty image after scaling
	scaled_img = np.array([[0] * scaled_w] * scaled_h)

	#scale by nearest neighbor
	scaled_img = gtf.nn(img, scaled_img, h_ratio, w_ratio)
	return scaled_img
	"""		end of scaled_nn		"""

"""
scale_lp - function to do geometric trasnformation by bilinear transformation
Parameters:
	img		I/P	image input
	h_ratio		I/P	ratio for scaling height
	w_ratio		I/P	ratio for scaling width
	saled_img	O/P	scaled image output
"""
def scale_lp(img, h_ratio, w_ratio = 0):
	#Assume to scale around (0, 0)
	assert(h_ratio != 0), "Ratio cannot be zero or 0" #scaling ratio cannot be zero or 0
	if w_ratio == 0: #only one given scaling ratio
		w_ratio = h_ratio
	h_ratio = round(h_ratio)
	w_ratio = round(w_ratio)

	#get width and height after scaling
	scaled_width = img.shape[1] * w_ratio #scaling ratio always integer as image size not decimal
	scaled_height = img.shape[0] * h_ratio

	#create empty image after scaling
	scaled_img = np.array([[0] * scaled_width] * scaled_height)

	#biliner interpolate
	scaled_img = gtf.linear_interpolate(img, scaled_img, h_ratio, w_ratio)

	return scaled_img
	"""		end of scale_lp		"""
