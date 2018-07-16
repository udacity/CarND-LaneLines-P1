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

First of all, the pipeline is written as a function. This is done to enable the use of the same pipeline for both the images as the videos. The pipeline consists of .. steps:

1. Convert image to greyscale
2. Define a kernel size and apply Gaussian smoothing
3. Define parameters for Canny and apply
4. Create a masked edges image
5. Defining a four sided polygon to mask
6. Define the Hough transform parameter
7. Make a blank the same size as our image to draw on
8. Run Hough on edge detected image
9. Define variables to use for averaging and extrapolation and iterate over the output "lines"
   - split left and right line
   - skip all gradients not in between ±0.5 en ±2 to get rid of outliers
   - find and store (variable) the end (left) and start (right) point of the line most-to-top of the picture
   - calculate average gradient for both left and right line
   - find line position on the bottom edge of the picture Y=(max y-resolution)
   - extrapolate form bottom edge to y-top (= top of earlier defined polygon)
 10. Create a "color" binary image to combine with line image
 11. Draw the lines on the edge image
 
 Included below are images showing the two important steps:
 1. Find max coordinate for both left and right and draw a line to the bottom of the image
 2. From bottom extrapolate to top of polygoon and draw line to the top
 
 
   
  
![alt text][image1]


### 2. Identify potential shortcomings with your current pipeline


One potential shortcoming would be what would happen when ... 

Another shortcoming could be ...


### 3. Suggest possible improvements to your pipeline

A possible improvement would be to ...

Another potential improvement could be to ...
