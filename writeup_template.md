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
[result1]: ./result1.png "Grayscale"
[result2]: ./result2.png "Grayscale"
[result3]: ./result3.png "Grayscale"

---

### Reflection

### 1. Describe your pipeline. As part of the description, explain how you modified the draw_lines() function.

My pipeline consisted of 6 steps. 

Step 1. I converted the images to grayscale.
Step 2. I defined a kernel size and apply Gaussian smoothing.
Step 3. I defined parameters for Canny and apply.
Step 4. I defined a ROI mask with four sided polygon.
Step 5. I defined the hough transform parameters.
Step 6. I drawed the lines on the edge image.

In order to draw a single line on the left and right lanes, 
I modified the draw_lines() function by calculating the scope of lines.

After calculating the scope of lines, I deleted the unreasonable lines which has a out of range about scope.

The results of my pipelines are like below images.


![alt text][result1]
![alt text][result2]


### 2. Identify potential shortcomings with your current pipeline

I think my code have some potential shortcomings.

As I just delete some unreasonable lane lines with scopes so it is dependent the 
threshold of scopes conditions.

### 3. Suggest possible improvements to your pipeline

My code is possible improved by additional stretegy.

If I can delete unuseful lines between two major lane lines of left and right side, it would be better than now.

And If I can track the two side lines continuously with curvature not straight line, it would be better than now.

![alt text][result3]