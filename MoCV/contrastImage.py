#contrastImage.py

from . import histogram
import cv2

"""
upcontrastImage - function to increase contrast of an image
Parameters:
	image		I/P	image need increasing contrast
	res_image	O/P	image after being increased contrast
"""
upcontrastImage(image):
	"""
	Perform Histogram equalization to strech images in order to increase contrast
	"""
	#compute hist of each channel and equalize
	equalized_hists = []
	
	for channel_idx in range(hists.shape[2]):
		#calculate histogram
		hist, pixels = histogram.calcHist(hists[:,:,channel_idx])
		#equalize histogram
		equalized_hists.append(histogram.equalizeHist(hist, pixels))

	#contrsuct new channel
	for channel in equalized_hists:
		for color, pixels in channel.items():
			for pixel in pixels:
				image[pixel.x, pixel.y, channel] = color	

	return image
