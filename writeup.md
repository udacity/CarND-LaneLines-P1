**Finding Lane Lines on the Road**

The goals / steps of this project are the following:
* Make a pipeline that finds lane lines on the road
* Reflect on your work in a written report


[//]: # (Image References)

[image1]: ./Lane_line_detection.jpg "Lane Line Processing"

---

### Reflection

  1. Describe your pipeline. As part of the description, explain how you modified the draw_lines() function.

My pipeline consisted of 5 steps. First, I converted the images to grayscale, then I detected edges using Canny approach (before this we also did gaussion smoothing to make sure we can get the accurate result out of Canny detection); Third, I used a pixel mask to select the region of interest; Forth, Hough transform is used to detect the lines on the masked edges image and to generate the line image; at the end, I overlayed the generated line image onto the original images to create the final result. 

Inside line detection, draw_lines() is called to combine and extrapolate multiple small line segments into two solid lines to mark the car lane, i.e., left lane line and right lane line. The way I do it can be summarized into 3 steps: 1) separete line segments into two groups: left lines (line tangent > 0) and right line (line tangent < 0 ).   


In order to draw a single line on the left and right lanes, I modified the draw_lines() function by adding line segment combination and extrapolation into the function. The way I do it is, first, I separate small line segments into two groups:  left lines (line tangent > 0) and right line (line tangent < 0 ); then, I compute the average line tangent and line average point, for both left and right lines; last, I use the avearge tangents and average points, as well as the boundary of area of interest, to extrapolate single solid line for left and right lanes. We know that a line in 2D space can be represented by the equation:

y - y0 = a*( x-x0 ) 

where a is the tangent of the line and (x0, y0) is some point on the line. If we set the boundary of the interested area to be y_bmin < y < y_bmax, set (x0,y0) to be the average point of line segments, set a to be the average tangent, we can extrapolate the single left/right line segment by calculating the two end points as follows,

for left line:
x_bottom = (y_bmin - y0)/a + x0
x_top = (y_bmax - y0)/a + x0

for right line:
x_bottom = (y_bmin - y0)/a + x0
x_top = (y_bmax - y0)/a + x0

Finally, in this way the left/right line segments are represented as [ (x_bottom, y_bmin), (x_top, y_bmax)]


![alt text][image1]


  2. Identify potential shortcomings with your current pipeline

One potential shortcoming would be what would happen when the camera is mounted in different positions on the car, in that case the area of interest on the image would be different than the one initialized here in the pipeline and could make the detection algorithm ineffective and inaccurate. 

Another shortcoming could be that, some computation is wasted as part of image outside of area of interest are masked out but nevertheless are still processed before the masking. 

And also one important shortcoming of this pipeline is that all steps are implemented in software and even worse, running on general purpose cpu, which is really slow and cannot be used on a real car as it needs a lot of image processing time. 

  3. Suggest possible improvements to your pipeline

A possible improvement for the first shortcoming would be to add an adaptive calibration done before drawline() is called. 

Another potential improvement for the second shortcoming could be to mask the image with area of interest as early as possible. This is can be easily done if we have a fixed stable area of interest, but would be hard to do if an adaptive calibration is needed for the area of interest, which it self needs some preprocessing. 

For the third shortcoming: considering most of the computation here are matrix operations, if we could offload some tasks, e.g. gaussion smoothing, Canny approach, Hough transform onto dedecated GPU, or even better a dedicated ASIC, which would significantly improve the realtime performance of this algorithm. We can even add more advanced processing into the pipeline. But, all this offloading increases the cost a lot on the end product, so we might need a more comprehensive cost-benefit analysis to decide where the best compromise lies, what tasks to offload, what to be used, GPU or a new dedicated ASIC. 


