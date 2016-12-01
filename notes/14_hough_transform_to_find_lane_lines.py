# URL: https://classroom.udacity.com/nanodegrees/nd013/parts/fbf77062-5703-404e-b60c-95b78b2f3f9e/modules/83ec35ee-1e02-48a5-bdb7-d244bd47c2dc/lessons/8c82408b-a217-4d09-b81d-1bda4c6380ef/concepts/90e3a984-eb68-48d3-8724-e58303a8d2cc
#
#   Implementing a Hough Transform on Edge Detected Image
#
#   Now that you know how the Hough Transform works, we're going to code it up and find the lane lines in the image we
#   detected edges in with the Canny function.
#
#   Here's the image we're working with:
#
#      <test_images/edges_exitramp.jpg>
#
#   Let's look at the input parameters for the OpenCV function HoughLinesP that we will use to find lines in the image.
#   You will call it like this:
#
#   lines = cv2.HoughLinesP(edges, rho, theta, threshold, np.array([]),
#                                              min_line_length, max_line_gap)
#
#   In this case, we are operating on the image edges (the output from Canny) and the output from HoughLinesP will be
#   lines, which will simply be an array containing the endpoints (x1, y1, x2, y2) of all line segments detected by the
#   transform operation. The other parameters define just what kind of line segments we're looking for.
#
#   First off, rho and theta are the distance and angular resolution of our grid in Hough space. Remember that, in
#   Hough space, we have a grid laid out along the (Θ, ρ) axis. You need to specify rho in units of pixels and theta
#   in units of radians.
#
#   So, what are reasonable values? Well, rho takes a minimum value of 1, and a reasonable starting place for theta
#   is 1 degree (pi/180 in radians). Scale these values up to be more flexible in your definition of what constitutes
#   a line.
#
#   The threshold parameter specifies the minimum number of votes (intersections in a given grid cell) a candidate line
#   needs to have to make it into the output. The empty np.array([]) is just a placeholder, no need to change it. min_
#   line_length is the minimum length of a line (in pixels) that you will accept in the output, and max_line_gap is the
#   maximum distance (again, in pixels) between segments that you will allow to be connected into a single line. You
#   can then iterate through your output lines and draw them onto the image to see what you got!
#
#   So, here's what its going to look like:
#
#

# Do relevant imports
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy as np
import cv2

# Read in and grayscale the image
image = mpimg.imread('exit_ramp.jpg')
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Define a kernel size and apply Gaussian smoothing
kernel_size = 5
blur_gray = cv2.GaussianBlur(gray, (kernel_size, kernel_size), 0)

# Define our parameters for Canny and apply
low_threshold = 50
high_threshold = 150
edges = cv2.Canny(blur_gray, low_threshold, high_threshold)

# Define the Hough transform parameters
# Make a blank the same size as our image to draw on
rho = 1
theta = np.pi/180
threshold = 1
min_line_length = 10
max_line_gap = 1
line_image = np.copy(image) * 0  # creating a blank to draw lines on

# Run Hough on edge detected image
lines = cv2.HoughLinesP(edges, rho, theta, threshold, np.array([]),
                        min_line_length, max_line_gap)

# Iterate over the output "lines" and draw lines on the blank
for line in lines:
    for x1, y1, x2, y2 in line:
        cv2.line(line_image, (x1, y1), (x2, y2), (255, 0, 0), 10)

# Create a "color" binary image to combine with line image
color_edges = np.dstack((edges, edges, edges))

# Draw the lines on the edge image
combo = cv2.addWeighted(color_edges, 0.8, line_image, 1, 0)
plt.imshow(combo)
plt.show()

#
#   As you can see I've detected lots of line segments! Your job, in the next exercise, is to figure out which
#   parameters do the best job of optimizing the detection of the lane lines. Then, you'll want to apply a region of
#   interest mask to filter out detected line segments in other areas of the image. When you're finished you'll be
#   ready to apply the skills you've learned to do the project at the end of this lesson.
#
