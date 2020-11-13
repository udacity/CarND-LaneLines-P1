# **Finding Lane Lines on the Road** 

## Writeup Template

### You can use this file as a template for your writeup if you want to submit it as a markdown file. But feel free to use some other method and submit a pdf if you prefer.

---

**Finding Lane Lines on the Road**

The goals / steps of this project are the following:
* Make a pipeline that finds lane lines on the road
* Reflect on your work in a written report


[//]: # (Image References)

[image1]: ./examples/grayscale.jpg "Grayscale"

---

### Reflection

### 1. Describe your pipeline. As part of the description, explain how you modified the draw_lines() function.

My pipeline consisted of 6 steps. 

- create grayscale image
- apply Gaussian blur
- apply Canny Edge finder
- apply proper plolygon mask to leave only the region pertinent to driving line separators
- apply  Hough transform to identify line segments
- extrapolate the line segments marked by the Hough transform to create just two lines the left and the right


![alt text](single_image_pipeline/CannyEdges.png "Canny")
![alt text](single_image_pipeline/polygon.png "Polygon")
![alt text](single_image_pipeline/hough.png "Hough")
![alt text](single_image_pipeline/extrapolated.png "Extrapolated")


### 2. Identify potential shortcomings with your current pipeline

On regular straight segments it works great but has very short-lived intermittent glitches. They should be OK.
On the advanced video it was obvious that it does not work well on turns.


### 3. Suggest possible improvements to your pipeline

I suspect the intermittent glitches are OK.
I believe the improvement may be to have a dynamic mask that changes the polygon shape when the car is turning.
Because the region of interest on turns is quite different from the region of interest on straight segments.
