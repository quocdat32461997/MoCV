#test.py

#import dependencies
import cv2
import os
import MoCV

"""
_enhance_image_test - function to test histogram equalization for image-contrast enhancement
Parameters:
	test_folder_path	I/P	path to test folder for contrast enhancement
	test_img_name		I/P	name of test image
"""
def _enhance_image_test(test_folder_path, img_name):
	#read image 
	img = cv2.imread(os.path.join(test_folder_path, test_img_name), img_name,0)

	#print image out
	cv2.imshow('image',img)
	cv2.waitKey(0)
	cv2.destroyAllWindows()

	#Histogram Equalizaiton to increase image contrast
	enhanced_image = MoCV.contrastImage.upcontrastImage(img)

	#write image
	enhanced_img_path = os.path.join(test_folder_path, "enhanced_image.png")
	cv2.imwrite(enhanced_img_path)
	
	enhanced_img = cv2.imread(enhanced_img_path)
	cv2.imshow('enhanced_image', enhanced_img)
	cv2.waitKey(0)
	cv2.destroyAllWindows()


"""
_segment_image_test - function to test optimal thresholding for image segmentation
Parameters:
	test_folder_path	I/P	path to test folder for image segmentation
	test_img_name		I/P	name of test image
"""
def _segment_image_test(test_folder_path, img_name):
	#read_image
	img = cv2.imread(os.path.join(test_folder_path, img_name), 0)
	
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

"""
test - function test all functions
Parameters:
	mode	I/P	index of CV algorithsm for testing. Look at README for indices of algorithms. -1 for all algorithms
"""
_segment_image_test("./tests/images/contrast", "low_contrast_image.png")
