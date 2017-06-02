# **Finding Lane Lines on the Road** 


---

**Finding Lane Lines on the Road**

The goals / steps of this project are the following:
* Make a pipeline that finds lane lines on the road
* Reflect on your work in a written report


[//]: # (Image References)

[image1]: ./examples/grayscale.jpg "Grayscale"

---

### Reflection

### 1. Description of the pipeline. 
My pipeline consisted of 6 steps. 

1. convert the images to grayscale
2. blur the gray image
3. use canny algorithm to detect edges on the blured gray image
4. maske the edge image so that only region of interest (polygon defined by four vertices) are left unmasked
5. use hough transformation to identify lines on the masked edge image
6. use the draw_lines function to filter and fit the lines to identify lane lines, extrapolate the lane lines so their y coordinates spaning the lower 40% of the image, and draw the lane lines on the original image

Here is how I modified the draw_lines() function

1. To fit the lane line, I grouped the raw lines identified by hough transformation into left and right groups, based on their slopes. For each group, all the points of all the lines were added into a list and linear fit was applied to find the slope and interception of the lane line.
2. I noticed some of the horizontal line marks crossing the the lane lines and curb edges are also identified as lines by the hough transformation, and including them in the fit distort the result quite a bit, so I decided to filter them out. My criteria is to filter lines whose slope is very different from the expected lane line (horizontal line marks) or whose distance are too far from the expected lane line (curb edges). 
3. The key of filter is select the "expected lane line". Originally, I used the fit result from unfiltered lines as the expected lane line, but as the fit result could be quite different from the actual lane line at extreme cases, the result is not optimal. Then I used the average of the identified lane lines in the last few frames for reference, and lane lines of the solidYellowLeft.mp4 can be labeled with 100% accurate.



### 2. The potential shortcomings with the current pipeline


1. The region of interest is selected quite arbitrarily, which might not be the same if the car model or the position of the camera changes
2. The filter and fit part heavily relies on the "expected lane line", which might not be as stable as expected, especially when car is turning or road is very curvy
3. The algorithm only consideres the ideal situation where the near road is not occupied by traffic or random items. Those things, existing in the real life, could potentially disturb the result a lot


### 3. Suggest possible improvements to your pipeline

1. use color selection to identify the region of interest and filter out irrelevant objects on the road
2. use machine learning techniques to cluster the raw lines and remove the irrelevant groups, instead of relies on "expected lan line"