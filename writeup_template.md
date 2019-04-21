# **Finding Lane Lines on the Road** 

## Writeup Template

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

My pipeline consisted of 5 steps. 

1. Convert the images to grayscale
2. Apply the Gaussian smoothing function (blur)
3. Apply Canny edge detection algorithm 
4. Select the region of interest
5. Apply Hough transform to detect line segments
6. Combine the images and save it to output folder 

In order to draw a single line on the left and right lanes, I modified the draw_lines() function by getting the lines' slopes and interecpt and making a selection based on that.

If you'd like to include images to show how the pipeline works, here is how to include an image: 

![alt text][image1]


### 2. Identify potential shortcomings with your current pipeline

One potential shortcoming would be what would happen:

1. Current program cane be optimized to process the images faster.

2. Also, It has not been tested for high resoltion image files, grayscale images.


### 3. Suggest possible improvements to your pipeline

Although the pipeline performs better on the SolddWhiteRight.mp4 and Solidyellowlefe.mp4 videos, it does seem to fail on the challeges.mp4 where the lane involves curving with some jiggling. 
The algorithms can be tweeked to handle these by tweeking draw_line functons.

Another improvement could be to see explore the ways if there is any jittering or movement in the camera recording in the curvings.

Another potential improvement could be to handle all the color linings besides yellow and white.
