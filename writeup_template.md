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

My pipeline consisted of 6 steps.
1. I converted the images to grayscale
2. I smoothed the greyscaled image with Gauss
3. I applied Canny for the Gaussian output
4. I created a masked image for the Canny image within the region of interest
5. I made the Hough transformation for the masked image
6. Finally I drew the lines on the original image

In order to draw a single line on the left and right lanes, I modified the draw_lines() function by
1. separating left and right lines calculating m
  1a. if m is positive --> right line
  1b. if m is negative --> left line
2. finding extreme x and y of the first and last point (for left an right lines) of all lines by matching min max with x and y
  2a. if there is an positive or negative m on the wrong side, I took just lines whose x1 are greater than 490 for right lines and lower than 450 for left lines
3. after then, when I got just one line for left an one for right, I found the intersection point of left line and right line with parallel of x-axis (lower image border)
4. then I took the lowest y value of right and left line and made a new line for left or right. So both lines ending with the same y value

If you'd like to include images to show how the pipeline works, here is how to include an image: 

![alt text][image1]


### 2. Identify potential shortcomings with your current pipeline


One potential shortcoming would be what would happen when ... 

Another shortcoming could be ...


### 3. Suggest possible improvements to your pipeline

A possible improvement would be to ...

Another potential improvement could be to ...
