#__init__.py of MoCV

print("Importing MoCV")

#import all modules of MoCV
__all__ = ['contrast',
	'histogram',
	'linear_scale_image',
	'segmentation',
	'geom_transform',
	'img_func']
from . import *
