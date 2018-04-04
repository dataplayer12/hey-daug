#Set parameters about images in this file

import numpy as np

#image parameters
im_width=30
im_height=30
file_extension='.pgm' #specify extension of your image files here jpg, png, pgm etc.

#Currently the following types of transformations are applied to an image
#1. Gaussian blur
#2. flip or perspective transform (chosen at random)
#3. Gaussian blur on 2
#4. unsharp masking of image which makes the image sharper
#Thus, output data is 5 times of input data

#You can increase output data to six times by allowing rotation
#This may help the performance of harrcascade classifier
#My advise is to use this only for positive examples

#allow rotation from here
allow_rotation=False
if allow_rotation:
	min_angle=-5
	max_angle= 5

#kernel for unsharp masking
unsharp_kernel=np.array([[-1, -1 ,-1],[-1, 8, -1],[-1, -1, -1]])

#kernel for perspective transform
pts1 = np.float32([[2,2],[im_width-2,2],[2,im_height-2],[im_width-2,im_height-2]])
pts2 = np.float32([[0,0],[im_width,0],[0,im_height],[im_width,im_height]])
perspective_matrix=np.array([[  1.14285714e+00,   1.38777878e-17,  -2.28571429e+00],
 [ -2.08166817e-16,   1.14285714e+00,  -2.28571429e+00],
 [ -3.46944695e-17,  -1.30104261e-18,   1.00000000e+00]])
#perspective_matrix = cv2.getPerspectiveTransform(pts1,pts2)
#print perspective_matrix


#augmented data are stored with these suffixes in their name
#gb: gaussian blur, f: flip, fgb: flip with gb, p: perspective,
#pgb: perspective with gb, um: unsharp masked, r: rotated
suffixes={'gb':'_gb'+file_extension,'f':'_f'+file_extension,\
'fgb':'_fgb'+file_extension,'p':'_p'+file_extension,\
'pgb':'_pgb'+file_extension,'um':'_um'+file_extension,\
'r':'_r'+file_extension}




