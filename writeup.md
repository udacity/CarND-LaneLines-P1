# **Lane Lines Project: Writeup** 

## Author
Michael McConnell

**Finding Lane Lines on the Road**

The goals / steps of this project are the following:
* Make a pipeline that finds lane lines on the road
* Reflect on your work in a written report

--- 
### Code
The code to detect lane lines can be found in the P1.ipynb file. The primary changes can be found in the process_single_img function which implements the computer vision pipeline for detecting lines. This detection is suplimented by an angle threshold and line averaging implemented in the draw_lines function. The resulting detected lane markings are overlayed on the provided images. Final output can be found in the test_images_output and test_video_output folders. 

[//]: # (Image References)

---

### Reflection

#### 1. Pipeline

My pipeline consisted of 6 steps. 
##### 1. Convert image to greyscale
The intial image was converted to greyscale. This is done to get the image in a single channel form which can be processed by a canny edge detector used in future steps. Example of the conversion to greyscale can be seen below.


In order to draw a single line on the left and right lanes, I modified the draw_lines() function by ...

If you'd like to include images to show how the pipeline works, here is how to include an image: 

![Base Image](./pipeline_steps/base.jpg =480x)
*Base image before pipeline is applied*
\s
![Greyscale Image](./pipeline_steps/greyscale.jpg =480x)
*After image is converted to greyscale*
\s


### 2. Identify potential shortcomings with your current pipeline


One potential shortcoming would be what would happen when ... 

Another shortcoming could be ...


### 3. Suggest possible improvements to your pipeline

A possible improvement would be to ...

Another potential improvement could be to ...
