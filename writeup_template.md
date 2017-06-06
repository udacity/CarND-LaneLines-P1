# **Finding Lane Lines on the Road** 

---

**Finding Lane Lines on the Road**

The goals / steps of this project are the following:
* Make a pipeline that finds lane lines on the road
* Reflect on your work in a written report


[//]: # (Image References)

[image1]: ./examples/grayscale.jpg "Grayscale"

[hlsColor]: ./examples/hslColor.png "HLS color space"

---

### Reflection

### 1. Description of pipeline

My pipeline consisted of the following steps: creating an image mask to eliminate background noise, finding edges and lines within a region of interest, classifying lines into right and left groups, fitting a single lane line to each group and drawing it on the image.

I created the image mask by converting to the HLS color space.

create an image mask by selecting areas that are yellow, white, or 

My pipeline consisted of 5 steps. First, I converted the images to grayscale, then I .... 

In order to draw a single line on the left and right lanes, I modified the draw_lines() function by ...

If you'd like to include images to show how the pipeline works, here is how to include an image: 

![alt text][hlsColor]


### 2. Identify potential shortcomings with your current pipeline


One potential shortcoming would be what would happen when ... 

Another shortcoming could be ...


### 3. Suggest possible improvements to your pipeline

A possible improvement would be to ...

Another potential improvement could be to ...
