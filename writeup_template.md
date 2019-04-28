# **Finding Lane Lines on the Road** 


#### First pre-requisite thoroughly go through Udacity lectures before project tweak every program and see changes and if you are new to openCV and computer vision go through Computer Vision course by udacity.It has every aspect in detail.

---

**Finding Lane Lines on the Road**

The goals / steps of this project are the following:


* STEP1: I converted image into grayscale image

* STEP2:  Applied Gaussian blur on result image from step-1 using helper funtion gaussian_blur. Since raw grayscale image contains noise in image, its important to filter them out so rsult of further step is more robust.

* Step-3 : Applied the Canny transform on result of step-2 using helper function canny.

* STEP4:Masking region of interest using helper funtion region_of_interest .

* STEP5: Applied hough lines transform in order to identify straight lines using helper function hough_lines.

* STEP6:To draw line on original image weighted_img function applied.

In order to draw a single line on the left and right lanes, I modified the draw_lines() function and instead of drawing lines in this function i called extrapolate function to draw the lines.

extrapolate function usage linear regression by applying np.polyfit function on x and y coordinates. As result partial lines are displayed as complete lines.

Below are the steps used in extrapolate function :

*STEP1 : canculating slope of all lines
*STEP2 : select right and left lines on basis of slope value and filter out unwanted lines on basis of slope threshold
*STEP3 : separate x and y cordinates for both left and right lines
*STEP4 : applying np.polyfit for regression
*STEP5 : calculating x cordinates using y=mx+c
*STEP6 : draw the lines

### 2. Identify potential shortcomings with your current pipeline


One potential shortcoming is this code does not detect lines on curves

Another shortcoming could be weather condition which makes it difficult to detect


### 3. Suggest possible improvements to your pipeline

A possible improvement would be to accurately detect lines on curves and in extreme weather conditions.
