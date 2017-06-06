# **Finding Lane Lines on the Road** 

---

**Finding Lane Lines on the Road**

The goals / steps of this project are the following:
* Make a pipeline that finds lane lines on the road
* Reflect on your work in a written report


[//]: # (Image References)

[blurredGrayscaleExamples]: ./examples/blurredGrayscaleExamples.png "Original (left) and blurred grayscale images (right)"
[pipelineOutputs]: ./examples/pipelineOutputs.png "Pipeline intermediate outputs"

---

### Reflection

### 1. Description of pipeline

My pipeline consisted of the following steps: creating an image mask to eliminate background noise, finding edges and lines within a region of interest, classifying lines into right and left groups, fitting a single lane line to each group and drawing it on the image.

I created the image mask by converting to the HLS color space, which allows one to easily select a range of colors, lightnesses, and saturations.  For example, yellow colors can be selected using the range [180-255, 180-255, 50-150]  (i.e. yellow hue of most brightnesses and saturations) and white colors can be selected using the range [0-255, 200-255, 0-255] (i.e. any color of sufficient brightness).  I then returned a blurred, grayscale image where the selected areas were unchanged, but all other regions were colored black:

![alt text][blurredGrayscaleExamples]

I found edges and lines in the image using the provided helper functions.

![alt text][pipelineOutputs]




My pipeline consisted of 5 steps. First, I converted the images to grayscale, then I .... 

In order to draw a single line on the left and right lanes, I modified the draw_lines() function by ...

If you'd like to include images to show how the pipeline works, here is how to include an image: 






### 2. Identify potential shortcomings with your current pipeline


One potential shortcoming would be what would happen when ... 

Another shortcoming could be ...


### 3. Suggest possible improvements to your pipeline

A possible improvement would be to ...

Another potential improvement could be to ...
