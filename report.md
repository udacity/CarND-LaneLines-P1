# Finding Lane Lines on the Road
## 1.Description of my pipeline
My pipeline consisted of 6 steps.  Consider the original image 'solidYellowCurve2' as an example:

![solidYellowCurve2](https://raw.githubusercontent.com/junfeizhu/CarND-LaneLines-P1/master/test_images/solidYellowCurve2.jpg)

First, I converted the images to grayscale:

![gray](https://raw.githubusercontent.com/junfeizhu/CarND-LaneLines-P1/master/test_images_output/gray.jpg)

Then I apply the Canny transform to the grayscsle image with low_threshold = 100 and high_threshold = 200:
![edges](https://raw.githubusercontent.com/junfeizhu/CarND-LaneLines-P1/master/test_images_output/edges.jpg)

Next, I applied a Gaussian Noise Kernel to the image with kernel_size = 5:
![edges_g](https://raw.githubusercontent.com/junfeizhu/CarND-LaneLines-P1/master/test_images_output/edges_g.jpg)

Next, I masked the image with top position to be 0.6 times the total heigh of the image and the left position and right position to be 0.45 times the total length of the image and 0.55 times the total length of the image, respectively: 
![masked](https://raw.githubusercontent.com/junfeizhu/CarND-LaneLines-P1/master/test_images_output/masked.jpg)

Then I applied the hough_lines function to the image to draw a single line on the left and right lanes:
![hl](https://raw.githubusercontent.com/junfeizhu/CarND-LaneLines-P1/master/test_images_output/hl.jpg)
In order to do this, I modified the draw_line function by computing the average slopes and intercepts for the left lane and right lane respectively. The cv2.HoughLinesP function will find out all the lines in the image and pass this lines to the draw_line function. Then in the draw_line function, I computed the slopes and intercepts for all this lines.If the slope is positive, then it is for the left lane. If the slope is negative, then it is for the right lane. However, I didn't just average these slopes and intercepts. Instead, I dropped the slopes that are between -0.5 and 0.5. I did this because if a slope is close to horizontal, obviously it is not for the lane but some other objects in the image. If a slope was dropped, then the corresponding intercept was dropped as well. Then, I computed the average slope and intercept for the left lane and right lane respectively.

Finally,I used the weighted_img function with the default parameter values to map the single lines to the original image:
![out](https://raw.githubusercontent.com/junfeizhu/CarND-LaneLines-P1/master/test_images_output/out.jpg)


One potential shortcoming is that my pipeline may be very sensitive to the shade of trees or other objects on the road. This can be seen in the optioal challenge. When there are shades on the road, the lines are quite off:

![bad_result](https://raw.githubusercontent.com/junfeizhu/CarND-LaneLines-P1/master/bad_result/bad_result.png)

A possible improvement would be to use the color information. Lanes are usually white or yellow. However shades are dark. By using some color filter, it may imporve my pipeline.

