#**Finding Lane Lines on the Road** 

##Writeup Template

###You can use this file as a template for your writeup if you want to submit it as a markdown file. But feel free to use some other method and submit a pdf if you prefer.

---

**Finding Lane Lines on the Road**

The goals / steps of this project are the following:
* Make a pipeline that finds lane lines on the road
* Reflect on your work in a written report


[//]: # (Image References)

[image1]: ./examples/grayscale.jpg "Grayscale"

---

### Reflection

###1. Describe your pipeline. As part of the description, explain how you modified the draw_lines() function.

My pipeline consisted of 5 steps. First, I converted the images to grayscale, then I smoothed the image with a gaussian blur. My third step was to find the edges in the resulting image with the Canny Edge detector. Then I created a maks of the image using a four-sided polygon. With the given mask, I've used the hough transform to find the lanes that are long enough to be street lanes. 

In order to draw a single line on the left and right lanes, I modified the draw_lines() function by ...

If you'd like to include images to show how the pipeline works, here is how to include an image: 

![alt text][image1]


###2. Identify potential shortcomings with your current pipeline


One potential shortcoming would be what would happen when there are lanes that are not painted correctly, then the algorithm would miss the lanes.

Another shortcoming could be that in a curve the polygon might mask out the lanes in front of the car. The polygon that masks the image probably needs to change according to the direction of when the car is turning.


###3. Suggest possible improvements to your pipeline

A possible improvement would be to make the masked polygon to change overtime based on the prediction on what is the turning angle of the car. That can be found based on the angle of the street lines.

Another potential improvement could be to have annotated data and adjust the parameters, like the hough transform parameters such that the annotated data matches the output of the algorithm.
