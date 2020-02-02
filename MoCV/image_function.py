#image_function.py
"""
Module: image_function - module to implement resize (zoom in /out), rotate, and flip images
Last udpated: Feb. 2, 2020
"""

#import dependencies
from . import geom_transform as gtf

"""
shift - function to shift images
Parameters:
	image	I/P	image input
	alpha	I/P	the num of spaces shift horizontally
	beta 	I/P	the num of spaces shift vertically
		O/P	shifted image
"""
def shift(image, alpha, beta):
	#call Translation algorithm from Geometric Transform to shfit images by alpha and beta
	return gtf.translation(image, alpha, beta) 
