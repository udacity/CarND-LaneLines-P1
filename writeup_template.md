#**Finding Lane Lines on the Road** 

+My pipeline consisted of 5 steps: 
 1. First, I converted the images to grayscale, 
 2. then I smoothed the image with a gaussian blur. 
 3. My third step was to find the edges in the resulting image with the Canny Edge detector. 
 4. Then I created a maks of the image using a four-sided polygon. 
 5. With the given mask, I've used the hough transform to find the lanes that are long enough to be street lanes.

---

**Finding Lane Lines on the Road**

In order to draw a single line on the left and right lanes, I modified the draw_lines() function by 
  1. Finding the slope(m1) of left lane and slope(m2) of right lane.
  2. Find the Y-intercept of left lane using the linear equation y=m1*x+b. b is the Y-intercept.
  3. Find the X-intercept of the top of the polygon for left lane. Using (Y2-Y1/X2-X1)=m
  4. So Left lane intercepts are (0,b) and (320,X-intercept). 320 is the Vertices constant given for polygon.
  5. Draw a single line from (0,b) and (320,X-intercept)
  5. Right Lane - Find the X-intercept for the bootom of the poly using the slope m2 and equation y=m2*x+b. Here Y is image.shape[0] which will be max value of Y.
  6. Find the X-intercept for the top of the poly using (Y2-Y1/X2-X1)=m equation. Here Y intercept is the constant "320" given for Vertices of polygon.
  7. So the Right lane intercepts are (b,imag.shape[0]) and (X,320)
  8. Draw a single line from (b,imag.shape[0]) to (X,320). Also I have added a correction of 10pixels to X intercept for right lane sinc the line was aligning with the lane. This correction worked for all test images.
  


 ###2. Identify potential shortcomings with your current pipeline
  
  
 -One potential shortcoming would be what would happen when ... 
 +One potential shortcoming would be what would happen when there are lanes that are not painted correctly, then the algorithm would miss the lanes.
  
 -Another shortcoming could be ...
 +Another shortcoming could be that in a curve the polygon might mask out the lanes in front of the car. The polygon that masks the image probably needs to change according to the direction of when the car is turning.
  
  
  ###3. Suggest possible improvements to your pipeline
  
 -A possible improvement would be to ...
 +A possible improvement would be to make the masked polygon to change overtime based on the prediction on what is the turning angle of the car. That can be found based on the angle of the street lines.
  
 -Another potential improvement could be to ...
 +Another potential improvement could be to have annotated data and adjust the parameters, like the hough transform parameters such that the annotated data matches the output of the algorithm.
