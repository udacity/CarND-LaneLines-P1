# **Finding Lane Lines on the Road** 

## Writeup Template

### You can use this file as a template for your writeup if you want to submit it as a markdown file. But feel free to use some other method and submit a pdf if you prefer.

---

**Finding Lane Lines on the Road**

The goals / steps of this project are the following:
* Make a pipeline that finds lane lines on the road
* Reflect on your work in a written report
* Use OpenCV concepts to detect edges, smoothing, and removing noise
* Use concepts of slope, intercepts and averaging to extrapolate the lane lines


[//]: # (Image References)

[image1]: ./examples/grayscale.jpg "Grayscale"

---

### Reflection

### 1. Describe your pipeline. As part of the description, explain how you modified the draw_lines() function.

My pipeline consisted of 5 steps. First, I converted the images to grayscale, then I applied guassian blur followed by Canny filter to remove noise and detect edges. ROI was taken as a 4sided polygon and hough transform was applied to this region - the values of rho, theta, min_line_length were decided on basis of trial and error. Once satisfactory results were obtained, next step was to extrapolate lane lines.

In order to draw a single line on the left and right lanes, I modified the draw_lines() function by 
* - For every edge detected from Hough Transform, slope and intercepts were calculated
* - These slopes were then checked for negative or positive value to distinguish between Left lane and right lane
* - The mean values of slope and intercepts were calculated to draw a final line on lane
Note - The threshold values to slope were added due too much movement of lines from lanes

If you'd like to include images to show how the pipeline works, here is how to include an image: 

![alt text][image1]


### 2. Identify potential shortcomings with your current pipeline


One potential shortcoming would be what would happen when curved lanes are encountered. This is the limitation of draw_lines() function 

Another shortcoming could be beacuse of value selection based on trial and error, the code output deviates at times


### 3. Suggest possible improvements to your pipeline

A possible improvement would be to write logic of draw_lines() such that the pipeline works smoothly even at curved edges

Another potential improvement could be to refine threshold values of trial and error to obtain more acccurate values
