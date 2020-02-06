#!/usr/bin/python3
#test.py

#import dependencies
import cv2
import sys
import os
import MoCV

"""
_enhance_image_test - function to test histogram equalization for image-contrast enhancement
Parameters:
	test_folder_path	I/P	path to test folder for contrast enhancement
	test_img_name		I/P	name of test image
"""
def _enhance_image_test(test_folder_path, test_img_name):
	print("Testing image contrast enhancement")

	#read image 
	img = cv2.imread(os.path.join(test_folder_path, test_img_name),0)
	
	#print image out
	#cv2.imshow('image',img)
	#cv2.waitKey(0)
	#cv2.destroyAllWindows()

	#Histogram Equalizaiton to increase image contrast
	enhanced_img = MoCV.contrast.upcontrastImage(img)

	#write image
	enhanced_img_path = os.path.join(test_folder_path, "enhanced_image.png")
	cv2.imwrite(enhanced_img_path, enhanced_img)
	
	#enhanced_img = cv2.imread(enhanced_img_path)
	#cv2.imshow('enhanced_image', enhanced_img)
	#cv2.waitKey(0)
	#cv2.destroyAllWindows()

	""" end of _enhance_image_test """

"""
_segment_image_test - function to test optimal thresholding for image segmentation
Parameters:
	test_folder_path	I/P	path to test folder for image segmentation
	test_img_name		I/P	name of test image
"""
def _segment_image_test(test_folder_path, test_img_name):
	print("Testing image segmentation")

	#read_image
	img = cv2.imread(os.path.join(test_folder_path, test_img_name), 0)
	
	#print image out
	#cv2.imshow('original image', img)
	#cv2.waitKey(0)
	#cv2.destroyAllWindows()

	#segment images front and back
	front_img, back_img = MoCV.segmentation.optimal_thresholding(img)

	front_img_path = os.path.join(test_folder_path, "front_segmented_img.png")
	back_img_path = os.path.join(test_folder_path, "back_segmented_img.png")

	#write front and back images
	cv2.imwrite(front_img_path, front_img)
	cv2.imwrite(back_img_path, back_img)

	""" end of _segment_image_test """

"""
_shift_image_test - function to shift images for alpha and beta spaces
Parameters:
	test_folder_path	I/P	path to test folder for image segmentation
	test_img_name		I/P	name of test image
"""
def _shift_image_test(test_folder_path, test_img_name, alpha, beta):
	print("Testing image shift")

	#read image
	img = cv2.imread(os.path.join(test_folder_path, test_img_name), 0)

	#shift images
	shifted_img = MoCV.img_func.shift(img, alpha, beta) 
	
	#write shifted image
	shifted_img_path = os.path.join(test_folder_path, "shifted_img.png")
	cv2.imwrite(shifted_img_path, shifted_img)
	
	""" end of _shift_image_test """

"""
_scale_nn_test - function to scale images by nearest neighbor method
Parameters:
	test_folder_path        I/P     path to test folder for image segmentation
	test_img_name           I/P     name of test image
"""
def _scale_nn_test(test_folder_path, test_img_name, w_ratio, h_ratio = 0):
	print("Testing scaling by nearest neighbor")
	
	#read image
	img = cv2.imread(os.path.join(test_folder_path, test_img_name), 0)
	
	#scale image
	scaled_img = MoCV.img_func.scale_nn(img, w_ratio, h_ratio) 

	#write scaled image
	scaled_img_path = os.path.join(test_folder_path, "scaled_nn_img.png")
	cv2.imwrite(scaled_img_path, scaled_img)
	"""		end of scaleing image by nearest neighbor		"""

"""
_scale_lp_test - function to scale images by nearest neighbor method
Parameters:
        test_folder_path        I/P     path to test folder for image segmentation
        test_img_name           I/P     name of test image
"""
def _scale_lp_test(test_folder_path, test_img_name, w_ratio, h_ratio = 0):
        print("Testing scaling by bilinear interpolation")

        #read image
        img = cv2.imread(os.path.join(test_folder_path, test_img_name), 0)

        #scale image
        scaled_img = MoCV.img_func.scale_lp(img, w_ratio, h_ratio)

        #write scaled image
        scaled_img_path = os.path.join(test_folder_path, "scaled_lp_img.png")
        cv2.imwrite(scaled_img_path, scaled_img)
        """             end of scaleing image by bilinear interpolation              """

"""
test - function test all functions
Parameters:
	mode	I/P	index of CV algorithsm for testing. Look at README for indices of algorithms. -1 for all algorithms
	*args	I/P	non-keyworded parameters
"""
def test(args):
	mode = int(args[0]) #get mode
	if mode == 1: #testing enhancing image contrast
		_enhance_image_test("./tests/images/contrast", "example_img.png") 

	elif mode == 2: #testing segmenting images
		_segment_image_test("./tests/images/segmentation", "example_img.jpg")

	elif mode == 3: #testing shifting images
		alpha, beta = [int(x) for x in args[1:]] 
		_shift_image_test("./tests/images/general", "example_img.png", alpha, beta)

	elif mode == 4: #testing scaling iamges
		assert(len(args[1]) > 0), "Missing scaling ratio" #checking scaling ratio exist
		h_ratio = w_ratio = 0
		if len(args[1:]) > 1:
			h_ratio, w_ratio = [int(x) for x in args[1:]]
		else:
			h_ratio = int(args[1]) 
		_scale_nn_test("./tests/images/general", "example_img2.png", h_ratio, w_ratio)
	elif mode == 5: #testing scaling iamges
                assert(len(args[1]) > 0), "Missing scaling ratio" #checking scaling ratio exist
                h_ratio = w_ratio = 0
                if len(args[1:]) > 1:
                        h_ratio, w_ratio = [int(x) for x in args[1:]]
                else:
                        h_ratio = int(args[1])
                _scale_lp_test("./tests/images/general", "example_img2.png", h_ratio, w_ratio)

	else:
		print("Wrong test")
	"""		end of test		"""


if __name__ == "__main__":
	test(sys.argv[1:])
