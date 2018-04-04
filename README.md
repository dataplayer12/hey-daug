# yo-daug
A (very) light weight data augmentation tool for training CNNs and Viola Jones detectors (Haar Cascades). This tool inflates your data by up to six times. Use with care.


Steps for use: 

1. Set the parameters for images in constants.py

2. Use data augmentation in your code:

```import data_utils as daug
folders=[folder1, folder2] #list of folder paths where training images are saved, ex. ['./pos' , './neg']
du.augment_and_save(folders)```

If you would like to remove augmented images and keep originals, use:
```du.remove_augmented_data(folders)```
