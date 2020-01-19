#contrastImage.py

from . import Histogram
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

	#computer histogram
	hist = cv2.calcHist(images = [image], channels = [0], mask = None, histSize = [256], ranges = [0, 256])	

	#equalize hist
	equalized_hist = Histogram.equalizeHist(hist)

	#convert equalized_hist to image

	return res_image 
