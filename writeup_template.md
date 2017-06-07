# **Finding Lane Lines on the Road** 

---

**Finding Lane Lines on the Road**

The goals / steps of this project are the following:
* Make a pipeline that finds lane lines on the road
* Reflect on your work in a written report


[//]: # (Image References)

[blurredGrayscaleExamples]: ./examples/blurredGrayscaleExamples.png "Original (left) and blurred grayscale images (right)"
[pipelineOutputs]: ./examples/pipelineOutputs.png "Pipeline intermediate outputs"

---

### Reflection

### 1. Description of pipeline

My pipeline consisted of the following steps: creating an image mask to eliminate background noise, finding edges and lines within a region of interest, classifying lines into right and left groups, fitting a single lane line to each group and drawing it on the image.

I created the image mask by converting to the HLS color space, which allows one to easily select a range of colors, lightnesses, and saturations.  For example, yellow colors can be selected using the range [180-255, 180-255, 50-150]  (i.e. yellow hue of most brightnesses and saturations) and white colors can be selected using the range [0-255, 200-255, 0-255] (i.e. any color of sufficient brightness).  I then returned a blurred, grayscale image where the selected areas were unchanged, but all other regions were colored black:

![alt text][blurredGrayscaleExamples]

I found edges and lines in the image using the provided helper functions.  I played around with different minimum line lengths and maximum line gaps and settled on 30 for minimum line length and 60 for maximum line gap.  Having minimum line length be too small creates lots of false positivies, but having minimum line length too large prevents lanes from being found if only the majority of the visible line is made up of the short road refelectors rather than paint stripes.

![alt text][pipelineOutputs]


### 2. Identify potential shortcomings with your current pipeline

By far, the biggest shortcoming of this pipeline is that it is extremely difficult and time consuming to hand-tune the hyperparameters.  Finding a set of values that worked for even the five example images was somewhat difficult because tweaking the parameters for one example image "broke" the results of a previous example image.  Having an labeled "training set" with which to find good ranges for the hyperparameters would be very helpful - you can see why machine/deep learning has completely taken over!

Another shortcoming of my pipeline is the region of interest.  If the road curves a lot, if the car is going up or down a hill, or if the car is changing lanes, the lines will go outside the region of interest I used.  I found that a more exapansive region of interest lead to too many false positives in the raw lines step, preventing accurate selection of the left and right groups of lines.


### 3. Suggest possible improvements to your pipeline

One potential improvement would be to iteratively find the lane lines starting from nearer to the car, eliminating the need for a region of interest. For example you could do a first pass to come up with a guess for where the lines nearest the car are.  Then fit a polynomial to the line nearest the car and search for more line segments of the correct color by extrapolaing the fitted line as you move upward in the image.  I think this is going on to some extent in our brains/eyes if I told you to point out the furthest visible point on a lane line.  Iterative lane-finding would potentially allow for lines to be identified further from the car and also more accurately determine the curvature of the lines.

A nother potential improvement would be to use a Kalman filter to smooth lane lines from frame to frame so that the occasional frame with incorrect lines doesn't have as much of an affect.

I wonder to what extent Canny edge detectors and Hough transforms are still used in today's vision pipelines in industry.  Based on the trouble I've had tuning hyper-parameters and the possibility that a given region cannot be labeled using color or position alone, it seems likely that semantic segmentation or other deep learning methods will be needed to incorporate larger scale structure (such as other parked or moving cars, road barriers, trees, etc.), when deciding where the lane is.  If I was making a decision about the vision pipeline of a real self-driving car, I would probably only view my pipeline as perhaps a tool to create labled video with wich to train neural networks.

