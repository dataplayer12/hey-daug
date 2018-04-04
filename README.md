# yo-daug
A (very) light weight data augmentation tool for training CNNs and Viola Jones detectors


Steps for use: 

1. Set the parameters for images in constants.py

use augmentation function in your code as follows:

>>>import data_utils as du

>>>folders=[folder1, folder2] #list of folder paths where training images are saved, ex. ['./pos' , './neg']

>>>du.augment_and_save(folders)

#if you want to remove augmented images and restore only original images, use

du.remove_augmented_data(folders)
