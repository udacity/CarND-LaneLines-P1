# **Finding Lane Lines on the Road** 

**Finding Lane Lines on the Road**

The goals / steps of this project are the following:
* Make a pipeline that finds lane lines on the road
* Reflect on your work in a written report


[//]: # (Image References)

[image1]: ./test_images/detected/solidWhiteCurve_detected.jpg "TestImageDetected"
[image2]: ./test_images/solidWhiteCurve.jpg "TestImage"

---

### Reflection

### 1. The Approach

The detections of lane pipeline was pretty straightforward based on techniques taught in the lectures:
1. Use a Gaussian Kernel to filter the image
2. Perform Canny edge detection 
3. Use Hough transform to find lines from the edges

The test images can be found in the folder - "test_images" while the images with lane detections can be found in - "test_images/detected"

My path to this project was to understand the way my referenced project was implemented and then only once I had complete understanding of the project, proceed with using the code on it to create this submission.


### 2. Suggest possible improvements to your pipeline

The line connections can possibly be done in multiple ways. Another possible way this could be done would be work with hough transform and draw straight lines from hough transform.

### 3. References Citing

There are multiple resources out on the internet with respect to this project.
https://github.com/CYHSM/carnd/tree/master/CarND-LaneLines-P1 - was the project I followed.
