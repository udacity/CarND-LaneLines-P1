# **Finding Lane Lines on the Road** 

## Writeup Template

### You can use this file as a template for your writeup if you want to submit it as a markdown file. But feel free to use some other method and submit a pdf if you prefer.

---

**Finding Lane Lines on the Road**

The goals / steps of this project are the following:
* Make a pipeline that finds lane lines on the road
* Reflect on your work in a written report


[//]: # (Image References)

[image1]: ./examples/final_pic.PNG "Detect the lanes"

---

### Reflection

### 1. Describe your pipeline. As part of the description, explain how you modified the draw_lines() function.

My pipeline consisted of 5 steps. First, I converted the images to grayscale, then I used gaussian filter for removing noise. I used Canny function to detect the edges, set the mask to choose the lane information, then used hough line function to catch the line from the edges information.

In order to draw a single line on the left and right lanes, I modified the draw_lines() function by averaging the points information of hough function results. Averaging is done for right lane and left lane, which is decided by the x poision. Then, the averaging line was extended to the bottom posion from the averaging line equation.

If you'd like to include images to show how the pipeline works, here is how to include an image: 

[image1]: ./examples/final_pic.PNG "Detect the lanes"


### 2. Identify potential shortcomings with your current pipeline


One potential shortcoming would be what would happen when at curve the lane is not the staraigh because of the 1st order averaging and pre-desided area to average the hogh line function.

Another shortcoming could be at the rain and cloud situation, when it is hard to see the edge at grayscale.


### 3. Suggest possible improvements to your pipeline

A possible improvement would be to use the multiorder equation at averaging.

Another potential improvement could be to use RGB and bright information.
