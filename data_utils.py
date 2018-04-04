import os, numpy as np
import constants as cs

try:
	import cv2
except:
	import sys
	sys.path.append('/usr/local/lib/python2.7/site-packages')
	import cv2

def remove_augmented_data(folders):
	for folder in folders:
		all_images=os.listdir(folder)
		for image_name in all_images:
			img_path=folder+'/'+image_name
			for suffix in cs.suffixes.values():
				if suffix in img_path:
					try:
						os.remove(img_path)
					except:
						pass

def augment_and_save(folders):
	for folder in folders:
		all_images=os.listdir(folder)
		for image_name in all_images:
			img_path=folder+'/'+image_name
			image=cv2.imread(img_path,cv2.IMREAD_COLOR)
			if image is None:
				print('Could not read file: ', img_path)
				continue
			else:

				transform1=cv2.GaussianBlur(image,(3,3),sigmaX=0.2,sigmaY=0.2) #add gaussian blur to image
				cv2.imwrite(img_path.replace(cs.file_extension,cs.suffixes['gb']),transform1)  #image with gaussian blur

				if np.random.random() <0.5: #we either flip the image or get a perspective transform about some points
					transform2=np.fliplr(image)
					transform3= cv2.GaussianBlur(transform2,(3,3),sigmaX=0.2,sigmaY=0.2) #add gaussian blur to transform2
					cv2.imwrite(img_path.replace(cs.file_extension,cs.suffixes['f']),transform2)  #image flipped
					cv2.imwrite(img_path.replace(cs.file_extension,cs.suffixes['fgb']),transform3)   #flipped and gaussian blur
				else:
					transform2 = cv2.warpPerspective(image,cs.perspective_matrix,(cs.im_width,cs.im_height))
					transform3= cv2.GaussianBlur(transform2,(3,3),sigmaX=0.2,sigmaY=0.2) #add gaussian blur to transform2
					cv2.imwrite(img_path.replace(cs.file_extension,cs.suffixes['p']),transform2)   #image perspective transform
					cv2.imwrite(img_path.replace(cs.file_extension,cs.suffixes['pgb']),transform3) #transform with gaussian blur
				
				#implements unsharp masking
				mask= cv2.filter2D(image,-1,cs.unsharp_kernel)
				transform4= cv2.addWeighted(src1=image,alpha=1.05,src2=mask,beta=-0.05,gamma=0) #output= alpha*src1 + beta+src2 + gamma
				cv2.imwrite(img_path.replace(cs.file_extension,cs.suffixes['um']),transform4) #unsharp masked image

				if cs.allow_rotation:
					#implements rotation
					rows,cols = cs.im_width,cs.im_height
					angle=cs.min_angle+np.random.random()*(cs.max_angle-cs.min_angle)
					M = cv2.getRotationMatrix2D((cols/2,rows/2),angle,1)
					transform5= cv2.warpAffine(image,M1,(cols,rows))
					cv2.imwrite(img_path.replace(cs.file_extension,cs.suffixes['r']),transform5) #rotated image

				#break
	print('Done')