#**Finding Lane Lines on the Road** 


[//]: # (Image References)
[input_image]: ./test_images/challenge.jpg=100x100

[output_image]: ./test_images_output/challenge.jpg 


---

### Reflection

###1. Describe your pipeline. As part of the description, explain how you modified the draw_lines() function.


The pipeline first preprocesses the image by converting it to grayscale 
and blurring it using the GaussianBlur function.

It then applies a Canny filter over the image and highlights only the pixels 
with change in intensity within a pre-determined range.

After that, the part of the image that is outside of the region of interest is masked. This region is specified 
by the four vertices of a polygon.
 
Hough Transform are then computed to identify lines on the image. 

In order to draw a single line on the left and right lanes, I first computed the slope of each line. 
If the slope is positive, it is considered to be part to the left lane. 
If it is negative, it is part of the right lane. 
Since the lanes on a highway are unlikely to turn sharply, lines that are too horizontal are discarded as noise.

After that, I take the averages of all the left lane lines and right lanes lines respectively. This gives me two lines.
I then extrapolate the lines to go from the bottom to the top of my region of interest. 

This two lines are then overlaid onto the original image (which is slightly darken to give better contrast)
to form the annotated image.
This annotated image is the output of the pipeline.


###2. Identify potential shortcomings with your current pipeline

One shortcoming is that this method requires very consistent lane markings. 
In cases when the colour of the lanes are too faded out or if there is a big gap due 
to temporary construction or when a car a changing lane, the pipeline might not be able to see the line correctly.

In addition, it is susceptible to shadow, changing lighting conditions, and other unexpected 
markings or objects on the road.
Rainy conditions might also make the road too reflective for this pipeline to work.
Indeed, if there is snow on the ground, it probably won't work at all.

###3. Suggest possible improvements to your pipeline

A possible improvement would be to to block off the center of the road unless we are making
a lane change since a lane should not be in the center of the road. 

Another potential improvement could be to discard slope changes that are drastically different from the frame before.
Those drastic changes are very likely to be noise. In addition, we can also average out temporally adjacent 
lines together as well. 

To make this pipeline more robust, it will likely require a combination of other features in addition to lane marking.
Some features might be the location of the car in front of our car, and the colour of the lanes.