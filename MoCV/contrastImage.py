#contrastImage.py

from . import histogram
import numpy as np
import cv2

"""
upcontrastImage - function to increase contrast of an image
Parameters:
	image		I/P	image need increasing contrast
	res_image	O/P	image after being increased contrast
"""
def upcontrastImage(image):
	"""
	Perform Histogram equalization to strech images in order to increase contrast
	"""
	#compute hist of each channel and equalize
	equalized_hists = []
	
	#convert gray-scale to 3-dim image
	image = np.expand_dims(image, axis = 2) 
	
	#equalize histogram to increase contrast
	for channel_idx in range(image.shape[2]):
		#calculate histogram
		hist, pixels = histogram.calcHist(image[:,:,channel_idx])
		#equalize histogram
		equalized_hists.append(histogram.equalizeHist(hist, pixels))


	new_image = np.zeros(shape = image.shape)
	#contrsuct new image
	for channel_idx in range(len(equalized_hists)):
		channel = equalized_hists[channel_idx]
		for color in channel.keys():
			print(color)
			pixels = channel[color]
			print(len(pixels))
			for pixel in pixels:
				new_image[pixel.x, pixel.y, channel_idx] = color	

	return new_image 
