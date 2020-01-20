#tutorial.py


#import dependencies
import cv2
import MoCV

#read image 
img = cv2.imread("tests/image.png", 0)

#print image out
cv2.imshow('image',img)
cv2.waitKey(0)
cv2.destroyAllWindows()

#Histogram Equalizaiton to increase image contrast
enhanced_image = MoCV.contrastImage.upcontrastImage(img)

cv2.imwrite("enhacned_image.png", enhanced_image)