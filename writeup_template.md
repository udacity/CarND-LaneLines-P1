

---

#**Finding Lane Lines on the Road**#


[//]: # (Image References)

[image1]: ./examples/grayscale.jpg "Grayscale"

#### This project is for detecting lanes using image tests and videos from the OpenCV Library.

##### The series of steps that were used to achieve objective consisted of:
  * Turn the Image into a Grayscale 
  * Smooth out with a Gaussian Blur 
  * Apply Canny Edge Detection to find the Edges 
  * Apply a Region of Interest with Vertices 
  * Find lines with the Hough Transform 
  * Define a pipeline to run the previous Functions 
  * Test on Images and Videos 


### Reflection

### 1. Modifying the draw_lines function

I first tried to figure out how to split the lines between one or another.  I started with brainstorming a few ways to modify y = mx + b and start from there.  I split the two lines that was drawn based on a negative or positive slope. From there I played around and added a hypothesis on a few of the data points on where they should be placed.  I then outputted 2 lines based on the mean of the data points I was getting from the lists. 


### 2. Creating the Pipeline and applying them to test
The Pipeline was a simple step by step process of calling the functions then running them on the images and videos.  Although easy, it took a while as I played around with the data points until I found which ones worked best.  


### 3. Suggest possible improvements on the Project 
The formation of the pipeline was pretty streamlined to what I was supposed to do.  My approach to the draw_lines function however, I know can be improved.  This function was basically done at a standpoint of straight lines, and that's why I struggled with figuring out how to apply my own methods for the optional challenge. Applying my understanding of calculus to the draw_lines method ouputted poorly, and thus I stayed with this to submit the project. Despite that, I plan on coming back and changing the function that can work better on turns. I will also really dig deeper on figuring out how to identify the lines better with the shadows in the optional challenge.
