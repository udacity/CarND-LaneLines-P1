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

My pipeline consisted of following: 

1. Detecting edge of the picture using canny method
2. With the help of Hough Space method, detecting points in the same line
3. Filter lines and it's end points based on it's slope and end point location, class end points into two classes: left lines points & right lines points
4. Using polyfit function to fit two lines matching both left line and right line, outcome slope k and offset m
5. Based on k and m, extend line to intended range in image
6. With addWeighted function, add calculated lines into image


![alt text][image1]


### 2. Identify potential shortcomings with your current pipeline

1. In case there a sharp curve, a single straight line might not work
2. When detected picture has different area of brightness(shadow), the boundary could be mis-detected
3. When there's white car in front, it might also be mis-detected


### 3. Suggest possible improvements to your pipeline

Using adaptation fuciton, detecting average brightness of the picture. Base on the value, adujsting canny detecting value. 
