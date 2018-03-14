# **Finding Lane Lines on the Road** 

**Finding Lane Lines on the Road**

The goals / steps of this project are the following:
* Make a pipeline that finds lane lines on the road
* Reflect on your work in a written report


[//]: # (Image References)

[image1]: ./examples/grayscale.jpg "Grayscale"

---

### Reflection

### 1. Describe your pipeline. As part of the description, explain how you modified the draw_lines() function.

My pipeline consisted of 6 steps:
1. Convertting the RGB images to grayscaled images.
2. Applying Gaussian smoothing to the grayscaled image.
3. Using canny edge detection algorithm to detect the edges in the grayscaled image.
4. Defining a four sided polygon to mask the edge iamge.
5. Runnig a Hough Transform on the masked image to extract lines.
6. Drawing the lines on the raw image.

In order to draw a single line on the left and right lanes, I modified the draw_lines() function by:
1. Dividing the lines into two groups according to their slopes, if a line has negative slope samller than -0.5, then it is on the left line group, if a line has a positive slope bigger than 0.5, it is on the right line group. The slope and the center position of each line is stored in two lists.
2. Calcultaing the average slope of each group as the slope of the single line.
3. Calcultaing the center point of each group as the center point of the single line.
4. Defining the top and bottom of each line using the slope and the position of the center point.
5. Drawing lines between the top and bottom point of each line.


### 2. Identify potential shortcomings with your current pipeline

Potential shortcomings would be:
1. Vertical lines, which have the same x1 and x2, could not be detected because they are excluded from the two groups of left and right lines.
2. In order to make the function work with the challenge video, the threshold of the slope of the left&right lines are -0.5 and 0.5, which will exclude some line segments that might be part of the lane lines but do not meet the defined threshold.
3. The funtion will not be able to detect lane lines when there is a sharp left or right turn.
4. The masked area is fixed, if a camera was mounted to a different position, it will be very likely that the function will not work at all.


### 3. Suggest possible improvements to your pipeline

Potential improvement could be:
1. Another function should be defined to detect vertical and horizontal lines on the road, for there are certaion meanings for these lines.
2. Instead of using a straight line(with a slope and center point), it would be better to use polynomial curve fitting.
3. Instead of setting the mask mannually, it would be much better if one could define a function to set up the mask according to the positions of lines in the image/video.

