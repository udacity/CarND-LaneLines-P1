# **Finding Lane Lines on the Road** 

## Writeup Template

### You can use this file as a template for your writeup if you want to submit it as a markdown file. But feel free to use some other method and submit a pdf if you prefer.

---

**Finding Lane Lines on the Road**

The goals / steps of this project are the following:
* Make a pipeline that finds lane lines on the road
* Reflect on your work in a written report

---

### Reflection

### 1. Describe your pipeline. As part of the description, explain how you modified the draw_lines() function.

My pipeline consisted of 6 steps.

1.First, I converted the images to grayscale
2.I applied on the grayscale image a gussian filter with the kernel of size 5.
3.After determining the min and max thresholds for the canny transformation, I found the edges.
4.on the canny image, the region of the interest was drwan by using vertices.
5.Based on the region of the interest and with help of the hough_lines function the lane lines were extracted.
6.at the end I added the weights of the original image and the lane line image.


In order to draw a single line on the left and right lanes, I modified the hough_lines() function by sperating slopes and intercepts belonging to the left  or right lane line using np.plolyfit then to calculate the coordinates of the first and end points of each lane line I averaged them on the zero axis and the make_coordinate function was used to calculate the coordinates of the left and right lane lines.

If you'd like to include images to show how the pipeline works, here is how to include an image: 

![alt text][image1]


### 2. Identify potential shortcomings with your current pipeline


One potential shortcoming would be what would happen when curves will be tilted.

Another shortcoming could be in determination of vertices and regulation of parameters. 


### 3. Suggest possible improvements to your pipeline

A possible improvement would be in curven when auto goes left or right.

Another potential improvement could be to automatic determination of parameters and verices.

