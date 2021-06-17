**Finding Lane Lines on the Road**

The goals / steps of this project are the following:
* Make a pipeline that finds lane lines on the road in a given set of images.
* Use the pipeline to find the lane lines on the road in various video recordings 
* Reflect on your work in a written report 

[//]: # (Image References)

[image1]: ./MD_images/solidWhiteCurve.jpg "Original image"
[image2]: ./examples/grayscale.jpg "Grayscale"
[image3]: ./MD_images/edges.jpg "Canny edge detection"
[image4]: ./MD_images/Hough_Lines.jpg "Lane line drawn"
[image5]: ./MD_images/solidWhiteCurvefinal.jpg "Lane line drawn"
---
**Reflection**

My pipeline consisted of 5 steps. 
1. Converted the images to grayscale.
1. Used canny edge detection on grayscales images to find the lanes.
1. Calculated the vertices from the image and used applied an image mask to identify the relevant lane lines.
1. Drew the Hough lines on the canny transformed image using the draw_lines() function.
1. Copied the hough lines from the canny transformed image unto the original image. This shows the detected lane lines on the original image.

The images below are the transformation progression of the : 

![SolidWhiteCurve][image1] ![SolidWhiteCurve][image2] ![SolidWhiteCurve][image3] ![SolidWhiteCurve][image4] ![SolidWhiteCurve][image5]

**draw_lines()** 

The draw_lines() function was modified to continously draw hough transform lines on the left and right lanes. The following steps was used to accomplish this.
1. Find the slopes of the hough lines drawn on the canny image and use a threshold to isolate which lines are valid. 
1. Remove all lines whose slopes do not reach the threshold leaving only valid lines.
1. Seperate the lines belonging to the left and right lanes using the sign of the slope.  
1. After seperating the lines to left and right, use poly fit to find the slope and y-intercept of the new line to be drawn.
1. Draw new lines.

**Identify potential shortcomings with your current pipeline**


* One potential shortcoming would be what would happen when the road doesn't have a subtle bend as in the test images and video but has a very large curve. The program will be unable to differentiate the slopes between left and right.

* Another shortcoming would be that in varying lighting conditions the program will have trouble detecting the lanes using canny  transform.


**Suggest possible improvements to your pipeline**

* A possible improvement would be to use machine learning for mapping variations in road conditions.

* Another potential improvement could be to use a varying slope threshold for different road and lane conditions.
