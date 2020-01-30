#segmentation.py
"""
	In Computer Vision, segmentation objects and background could be done by different methods:
		Intensity-based Segmentation: Thresholding - Based on the intensity of colors in histogram
		Edge-based Segmentation - Based on edges
		Region-based Segmentation
"""

#import dependencies
from . import histogram
import numpy as np
__all__ = ['optimal_thresholding']


"""
optimal_thresholding - function to segment objects and background using Quantization 
Parameters:
	image	I/P	image
	
"""
def optimal_thresholding(image):
	#calculate histogram
	hist = histogram.histogram(image)

	#thresholding by quantization
	optimal_thd = _quantization(hist)

	#segment image based on optimal_threshold
	front = np.array([[0] * image.shape[1]] * image.shape[0])
	back = np.array([[255] * image.shape[1]] * image.shape[0])

	for row in range(image.shape[0]):
		for col in range(image.shape[1]):
			if image[row, col] > optimal_thd:
				front[row, col] = image[row, col]
			else:
				back[row, col] = image[row, col]
	#reconstruct
	return front, back

#################### helper functions ###########################

"""
_quantization - private function to perform quanization (color compression) to find the optimal threshold within the image histogram
Parameters:
	hist		I/P	image histogram
	optimal_thd	O/P	optimal_threshold
"""
def _quantization(hist):
	#by default, histogram has 0-255 brightness levels
	min_error = -1
	optimal_threshold = -1	

	#Calculate q1 and q2 by calculating means of two classes of threshold
	q2_num = sum([k * hist[k] for k in range(len(hist))]) #total of #_pixels * color 
	q2_denom = sum(hist) #total of #_pixels
	q1_num = 0
	q1_denom = 0

	#Quantization, assume all brightness levels as possible thresholds
	for t in range(len(hist)) :
		q1 = 0
		q2 = 0

		#calculate q1
		if q1_denom == 0:
			q1 = 0
		else:
			q1 = np.floor(q1_num / q1_denom)

		#calculate q2
		if q2_denom == 0:
			q2 = 0
		else:
			q2 = np.floor(q2_num / q2_denom)

		#update numerator and denominator 
		q1_num += t * hist[t]
		q2_num -= t * hist[t]
		q1_denom += hist[t]
		q2_denom -= hist[t]

		#calculate threshold by calculating total varaince two classes
		threshold = int(np.mean([q1, q2]))
		temp_error = _calculate_error(q1, q2, threshold, hist)
		if optimal_threshold < 0: #if optimal_threshold not initialized
			min_error = temp_error
			optimal_threshold = threshold
		elif temp_error < min_error: #check the next min error to find the optimal threshold
			min_error = temp_error
			optimal_threshold = threshold

	return optimal_threshold

"""
_calculate_error - function to calculate sum of variance of two classes for error at a threshold
Parameters:
	q1		I/P	class 1
	q2		I/P	class 2
	threshold	I/P	threshold
	hist		I/P	histogram
	error		O/P	total error: q1_variance + q2_variance
"""
def _calculate_error(q1, q2, threshold, hist):
	#calclulate sum of variance of class 1
	q1_variance = 0
	for color in range(threshold):
		q1_variance += hist[color] * ((color - q1) ** 2)

	#calculate sum of variance of class 2
	q2_variance = 0
	for color in range(threshold, 256):
		q2_variance += hist[color] * ((color - q2) ** 2)

	return q1_variance + q2_variance
