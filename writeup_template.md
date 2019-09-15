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

My pipeline consisted of 5 steps. First, I converted the images to grayscale, then I filtered the result image using a gaussian blur filter with a mask size of 5, a Canny algorithm is then applied to the filtered image with the two parameters: low threshold of 100 and high threshold of 200. In the fourth step, I defined the region of interest of the image where it is expected to find the lane lines. Finally, I called the Hough transform to detect the line patterns in the edge image (result of Canny algorithm).

In order to draw a single line on the left and right lanes, I modified the draw_lines() function by, first, grouping the detected lines in two groups, left and right using slope thresholds. After that an everage line is calculated to each group, by averaging the slope and shift parameters of all lines of each group. Extrapolation step is also applied to get eqal lengths lines of both sides left and right, by using the average line equation at two extrem points defined at the bottom of the image(x=0) and near the middle of the image(y=370)

If you'd like to include images to show how the pipeline works, here is how to include an image: 

![alt text][image1]


### 2. Identify potential shortcomings with your current pipeline


One potential shortcoming would be what would happen when the discontinious lines are different in terms of spacing.

Another shortcoming could be curves, where lines do not describe the lanes perfectly but rather a higher order polynomial would be needed.


### 3. Suggest possible improvements to your pipeline

A possible improvement would be to adapt the Hough transform parameters dynamically.

Another potential improvement could be to fit the deteted segments from Hough transform to a second or third degree polynomial.
