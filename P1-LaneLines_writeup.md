**Finding Lane Lines on the Road**

The goals / steps of this project are the following:

* Make a pipeline that finds lane lines on the road
* Reflect on your work in a written report


[//]: # (Image References)

[gray]: ./writeup_images/Gray_and_blurred.png "Grayscale and Blurred"
[canny]: ./writeup_images/canny.png "Canny Edge Detetction"
[roi]: ./writeup_images/roi.png "Region of interest"
[hough]: ./writeup_images/hough.png "Hough-Transformation"
[weight]: ./writeup_images/weight.png "Weighted"
[curves]: ./writeup_images/curves.png "Curves"


[result]: ./output_test_images/solidWhiteCurve.jpg "Final"





---

### Reflection

###1. Describe your pipeline. As part of the description, explain how you modified the draw_lines() function.

First, I Grayscaled the image to get a Black and White image, so the Code also works when the lane lines are in Yellow. After that i blurred the image. 

![alt text][gray]

Next step was to run the Canny edge detection with these paramters.

``` 
    low_threshold = 50
    high_threshold = 150
```
The Canny edge detection gave me this result.

![alt text] [canny]

Before using the Hough-Transformation, it is necessary to selct the main part of the image were the lane lines are. This step will reduce the erros of detcting others stuff then the lane lines. For that i cut out mostly everything out of the image to get this result where only lane lines are on the image.

![alt text] [roi]

On this image i used the Hough-Transformation with these parameters to draw lines on the points that were detected by Canny edge detection.

``` 
	rho = 1 
    theta = np.pi/180 
    threshold = 35     
    min_line_len = 5  
    max_line_gap = 2   
```


![alt text] [hough]

Then i used the weighted function to draw the lines on the orignal image.

![alt text] [weight]

At last i wrote a for loop to run it on all the images in the test_images folder. I don't had to change the Region of interest because, the camera is at the same postion with the same view at the streets. Thats why my Region of intrest is same on all images. 

It also works on Videos without any need to edit my find_lane_lines function.

#draw_lines 

The part with draw_lines was tough. For that i used slack and forums to get some tipps how to begin. After many reading and understanding.
I used a array to spearate the lines in postive and negative ones. Right lane postiv and left lane negativ. I used this formula (y2-y1)/(x2-x1) and the result to check if it is ≥ 0 then postiv and ≤ 0 for negativ. Later i changed the 0 with 0.1 and -0.1 it worked better in the second video. And this gave me this final result.

![alt text][result]


###2. Identify potential shortcomings with your current pipeline


One potential shortcoming is the code only works with images in very good lightning condition. Bad lightning and curves are breaking the code. _Challenge video_.

![alt text] [curves]






###3. Suggest possible improvements to your pipeline

The detection of the lane could be improvved unsing HSV color space for segmentation. 