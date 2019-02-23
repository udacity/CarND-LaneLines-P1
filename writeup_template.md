# **Finding Lane Lines on the Road** 

## Writeup

### You can use this file as a template for your writeup if you want to submit it as a markdown file. But feel free to use some other method and submit a pdf if you prefer.

---

**Finding Lane Lines on the Road**

The goals / steps of this project are the following:
* Make a pipeline that finds lane lines on the road
* Reflect on your work in a written report


[//]: # (Image References)

[image1]: ./examples/grayscale.jpg "Grayscale"

---

### Reflection

### 1. Describe your pipeline. As part of the description, explain how you modified the draw_lines() function.

My pipeline consisted of 5 steps. First, I converted the images to grayscale, next I apply Guassian Bluring to the image, then I apply the Canny transform to filter out the pixels that we interested in. I also create a region to mask where we are interested in the original image, that from the view of the self driving car. Then we use the Hough Transformation to find the lane lines, in order to find the right lanes we desire, this phase requires detailed parameters tuning for the hyperameters of the hough transformations. Lastly, we stack the lines we find in the original image and test it on the test video by apply our pipline to a series of clips of the video.

In order to draw a single line on the left and right lanes, I modified the draw_lines() function by check the negativity of the lines, if the lines is negative we classify it as left lane and vice versa, after having all the left lines and right lines respectively I apply linear regression to find the parameters to describe the lanes and draw the extrapolated lines on the original images.

If you'd like to include images to show how the pipeline works, here is how to include an image: 

![alt text][image1]


### 2. Identify potential shortcomings with your current pipeline


One potential shortcoming would be what would happen when there is a huge turn and cury lanes, then the linear regression lines will deviate the curly lanes a lot. 

Another shortcoming could be this model is not that robust for background variation, for example if there is illumination variation, the model is not robust for this.


### 3. Suggest possible improvements to your pipeline

A possible improvement would be to use polynomial regression to model high order curves
