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

My pipeline consisted of 6 steps as follows: 
Step 1: Apply grayscaling the images,
[image1]: ./test_images_output/gray.jpg "Grayscale"
Step 2: Apply Gaussian noise kernel,
[image2]: ./test_images_output/gaussian.jpg "Gaussian"
Step 3: Apply Canny transform,
[image3]: ./test_images_output/edge.jpg "Canny"
Step 4: Apply image mask based on region of interest,
[image4]: ./test_images_output/region.jpg "Region of interest"
Step 5: Apply Hough transform and cut off lines based region of interest,
[image5]: ./test_images_output/lines.jpg "Hough"
Step 6: Apply weighted images.
[image6]: ./test_images_output/result.jpg "Result"

In order to draw a single line on the left and right lanes, I modified the draw_lines() function by the following steps:
Step 1: Detect the right and left lines separetely by rough estimation of slope ((y2-y1)/(x2-x1)). If the slope is above a certain positive threshold, the detected line is considered as the right line. The slope is below a certain negative threshold, on the other hand, the detected line is considered as the left line.
Step 2: Average the position of each of the lines by least-squares method.
Step 3: Extrapolate the lines to the top and bottom of the lane based on region of interest.

### 2. Identify potential shortcomings with your current pipeline


One potential shortcoming would be what would happen when the vehicle goes into a steep curve.

Another shortcoming could be what would happen when the lines are consist of a series of bott's dot.


### 3. Suggest possible improvements to your pipeline

A possible improvement would be to average the position of each of the lines by polynomial approximation.
