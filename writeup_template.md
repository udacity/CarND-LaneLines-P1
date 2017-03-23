#**Finding Lane Lines on the Road** 

##Hang's Writeup

---

**Finding Lane Lines on the Road**

The goals / steps of this project are the following:
* Make a pipeline that finds lane lines on the road
* Reflect on your work in a written report


[//]: # (Image References)

[image1]: ./examples/grayscale.jpg "Grayscale"
[yellow_img]: ./screen_cap/yellow.png "yellow color pic"
[1]: ./screen_cap/1_gray.png "gray scale coversion"
[2]: ./screen_cap/2_blur.png "gaussian blur image"
[3]: ./screen_cap/3_edge.png "canny edge detection"
[4]: ./screen_cap/4_region.png "apply region filter"
[5]: ./screen_cap/5_lines.png "line extraction"
[6]: ./screen_cap/6_avg_line.png "compute slope/intersect"
[7]: ./screen_cap/7_draw_over.png "draw over the original frame"

---

### Reflection

###1. Image processing pipeline for lane lines detection

My pipeline consisted of 7 steps, carried out on a per image frame basis. 

First, a given image is converted from color input to gray scale. 

![alt text][1]

Next a gaussian blur with kernel size 5 is applied. 

![alt text][2]

Followed by canny edge detection, 

![alt text][3]

A polygonal filtering region is applied to the detected edges to remove edge detect above horizon and near left/right side of the image. 

![alt text][4]

Then the remaining edges are feed into hough transform to detect best fit lines. It worth noting that the parameters are tuned to extract relative long lines (at least 150 pixel long) - under the assumption that  lane marking form some of the longest line on the image, and allowed for large gap (up to 100 pixels) since there are large gap for lane divier markings.  

![alt text][5]

In order to draw a single line on the left and right lanes, I modified the draw_lines() function by calculating the slope and intersect for each detected line from the two points. On inspection of the calulated values, it's clear that a relative consistant postive and negative slope represent the left and rigth lans. So I groupped the resulting parameterized lines by postive and negaive slope value, then computed average slope and intersect  from each of the two groups; given we want to draw and extrapolate line near bottom of the image to near horizon, two points are calculated for each of 2 average lines with fixed y1 and y2 that crosspond to bottom of image and about halfway up in image coordinates. 

![alt text][6]

Finally the resulting averages lines is drawn over the original input image frame. 

![alt text][7]


to maximize the effectiness in picking out yellow, we first inspect the specific color of yellow we are working with:
![alt text][yellow_img]
here using Digital color meter, we can see it's a specific range of RGB (240, 200, 70), plus minus 20. 



###2. Identify potential shortcomings with your current pipeline


One potential shortcoming would be what would happen when ... 

Another shortcoming could be ...


###3. Suggest possible improvements to your pipeline

A possible improvement would be to ...

Another potential improvement could be to ...