# **Finding Lane Lines on the Road** 

## Writeup Template

### You can use this file as a template for your writeup if you want to submit it as a markdown file. But feel free to use some other method and submit a pdf if you prefer.

---

**Finding Lane Lines on the Road**

The goals / steps of this project are the following:
* Make a pipeline that finds lane lines on the road
* Reflect on your work in a written report

### Reflection

### 1. Describe your pipeline. As part of the description, explain how you modified the draw_lines() function.

First, I converted the images to grayscale, then I applied the Guassian filtering. Next step, I applied the canny edge detection and determine region of interest using a polygon. Then afterward, I applied the hough transform and weighted average to have the edges I am looking for.


[image1]: ./test_images/NEW_solidYellowCurve2.jpg "lane-detected-extrapolated image"



In order to draw a single line on the left and right lanes, I modified the draw_lines() function by ...

If you'd like to include images to show how the pipeline works, here is how to include an image: 

![alt text][\test_images\NEW_solidYellowCurve2.jpg]


### 2. Identify potential shortcomings with your current pipeline


One potential shortcoming would be what would happen when the driver is chaning lane; how would I update the region of interest. Or, in the case that lighting changes, would that effect on the algorithm? what if the road is too curvey or a bit snowy, how would that affect the algorithm. Just a line to extrapolate to detect the lane should not be good extrapolation. Probably, a polynomial or spline should a better way to extrapolate the lane.

### 3. Suggest possible improvements to your pipeline

A possible improvement would be to if I could have images/videos with different ambient lighting and road conditions. In a highway, where there are multiple lanes or in the case that road is surronded by lots of trees ... I am always wondering how a snowy road would affect the lane detection algorithm.

Another potential improvement could be to ...
