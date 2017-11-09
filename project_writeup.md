# **Finding Lane Lines on the Road**

[//]: # (Image References)
[image1]: ./examples/grayscale.jpg "Grayscale"

## Reflection

My pipeline consists of 5 steps:
1. Canny edge detection
1. Region of interest filtering
1. Line detection using Hough transform
1. Line filtering and grouping into left and right lane lines
1. Draw lane lines by averaging and extrapolation

They will be described in more detailed below.

### Canny edge detection

The implementation of the [Canny edge detector in OpenCV](https://docs.opencv.org/trunk/da/d22/tutorial_py_canny.html) includes image smoothing in its first stage hence pre smoothing of the image is not necessary. However the detector expects a 8-bit single channel image. Hence the image is converted into grey scale before passing to the detector. The detector returns a number of points which are recognised as being on the edge of features. One can only control the high and low gradient threshold used in the final stage of the algorithm to reject spurious points. As [recomended by John Canny himself](https://docs.opencv.org/2.4/doc/tutorials/imgproc/imgtrans/canny_detector/canny_detector.html#steps) the high threshold is set at 3 times the low threshold and the low threshold is set to 50.

### Region of interest filtering

A region of interest is drawn by eye-balling the area of the lane in the test images. It aims to include as much as possible the lane lines immediately in front of the camera and exclude as much as possible any distractions that may cause noise in the following pipeline steps.

### Line detection using Hough transform

The Hough transform is used to detect edge lines from a discrete number of edge points. The Probabilistic Hough transform we used is an efficient implementation of the detection algorithm. However instead of returning the parametric values of each line detected, it returns a number of lines segments.

In tuning the parameters of the Hough transform, I increased the minimum line length to remove short line segments.

### Line filtering and grouping into left and right lane lines

From the previous stage of the pipeline, we have now a number of line segment at edges in the camera image. These line segments are usually at the edge of the lane lines but some are detected at strong textures feature in the middle of the road or imperfections in the lane markings. Hence in this stage we need to achieve two things:
1. Remove some spurious line segments that are not related to lane lines
1. Group the line segments into ones relating to the left lane line and the right

There are 2 characteristics of the lane lines that we can intuitively use to achieve this:
1. The angle of the line segment with respect to the horizontal. The lane lines are at a large angle to the horizontal and the left lane line is at a distinct angle from the right.
1. The location of the line segment inside the area of interest. The line segment relating to the left lane line is usually inside the left half of the area of interest.

Hence we do the following filtering in this stage:
1. Rejects any lines that are relatively horizontal, i.e. any line that is between +/- 20 degrees to the horizontal.
1. Anything that is larger than +20 degrees to the horizontal and is on the right side of image belongs to the right lane line.
1. Anything that is smaller than -20 degrees to the horizontal and is on the left side of image belongs to the left lane line.

After this filtering and grouping we can fairly consistently get a number of line segment marking the left lane line edges and a number of line segment marking the right. Note that the filtering of the angles are done in Hough space with parameter theta for convenience.

### Draw lane lines by averaging and extrapolation

We need to find a single line marking the lane line from a number of segments. The easiest way is transform these segment to Hough space and average the parameters theta and rho. However, during experimentation, it is found that some times a small line segment, usually result of imperfections in the lane line markings, pointing in very different direction than the lane lines themselves, could affect the average greatly resulting in inaccuracies in the final lane line markings.

Intuitively we think that smaller line segments should not affect the output lane line too much. We can achieve this by doing a weighted average where the rho and theta of each line segment is weighted by its length. Thus shorter segments have a smaller influence on the average than longer ones.

We apply this average to the left and right groups of line segment and obtain a single parametric line for the left and right lane lines. We now need to draw this line from the bottom of the area of interest to the top. We already know the y values at the top and bottom of the area of interest, we need to calculate the x values. By rearranging the equation of the line we get `x = -y*tan(theta) + rho/cos(theta)`. Thus the two points can be calculated at the top and bottom and the lane lines can be drawn.

## 2. Potential shortcomings with the pipeline

There are a number of potential shortcomings in each of the pipeline stages and we will discuss them stage by stage.

### Canny edge detection

The thresholds are static values optimised for one test image. The thresholds might not perform so well when lighting conditions change resulting in changes of the intensity gradient at the edge of features.

### Region of interest filtering

The region of interest is a static box which does not account for yaw and pitch of the vehicle, bend in the road and other changes in perspective of the camera.

### Line detection using Hough transform

This transformation can only detect linear lines and performs poorly when the lines are curved.

### Line filtering and grouping into left and right lane lines

There are strong features in the surface texture of the tarmac which can be detected as edges and slip through the filters. These features can affect the final averaging stage and result in an inaccurate lane line marking.

### Draw lane lines by averaging and extrapolation

For each lane line, there is an inner edge and an outer edge, different number of segments can be detected on the inner edge and outer edge from frame to frame. Simply averaging these two types of edges may results in jitters in the final drawn lane line.

## 3. Suggest possible improvements to the pipeline

With the pitfalls discussed in the previous section in mind, here are some possible improvements.
1. Evaluate the overall contrast of the image and make the thresholds in the Canny edge detector a function of contrast.
1. Integrate with gyro in the car to adjust the area of interest according to the posture of the car.
1. Filter image by colour to remove large areas of the road and surroundings and focus solely on pixels with colour matching the lane lines
