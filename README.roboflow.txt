
Car - v1 2021-10-11 8:41pm
==============================

This dataset was exported via roboflow.com on April 30, 2026 at 8:45 AM GMT

Roboflow is an end-to-end computer vision platform that helps you
* collaborate with your team on computer vision projects
* collect & organize images
* understand and search unstructured image data
* annotate, and create datasets
* export, train, and deploy computer vision models
* use active learning to improve your dataset over time

For state of the art Computer Vision training notebooks you can use with this dataset,
visit https://github.com/roboflow/notebooks

To find over 100k other datasets and pre-trained models, visit https://universe.roboflow.com

The dataset includes 2400 images.
Car are annotated in YOLO26 format.

The following pre-processing was applied to each image:
* Auto-orientation of pixel data (with EXIF-orientation stripping)
* Resize to 416x416 (Stretch)

The following augmentation was applied to create 3 versions of each source image:
* 50% probability of horizontal flip
* Randomly crop between 0 and 13 percent of the image
* Random rotation of between -19 and +19 degrees
* Random brigthness adjustment of between -36 and +36 percent
* Random Gaussian blur of between 0 and 2.75 pixels
* Salt and pepper noise was applied to 10 percent of pixels

The following transformations were applied to the bounding boxes of each image:
* Randomly crop between 0 and 20 percent of the bounding box


