# URL: https://classroom.udacity.com/nanodegrees/nd013/parts/fbf77062-5703-404e-b60c-95b78b2f3f9e/modules/83ec35ee-1e02-48a5-bdb7-d244bd47c2dc/lessons/8c82408b-a217-4d09-b81d-1bda4c6380ef/concepts/c87c2a1c-c80e-4383-bf66-c1182ae91661


# Combining Color and Region Selections
#
# Now you've seen how to mask out a region of interest in an image. Next, let's combine the mask and color selection to
# pull only the lane lines out of the image.
#
# Check out the code below. Here we’re doing both the color and region selection steps, requiring that a pixel meet
# both the mask and color selection requirements to be retained.

import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy as np

# Read in the image
image = mpimg.imread("../test_images/solidWhiteRight.jpg")

print('image shape: ', image.shape)

# Grab the x and y sizes and make two copies of the image
# With one copy we'll extract only the pixels that meet our selection,
# then we'll paint those pixels red in the original image to see our selection
# overlaid on the original.

ysize = image.shape[0]
xsize = image.shape[1]

color_select = np.copy(image)
line_image = np.copy(image)

# Define our color criteria
red_threshold = 0
green_threshold = 0
blue_threshold = 0
rgb_threshold = [red_threshold, green_threshold, blue_threshold]

# Define a triangle region of interest (Note: if you run this code,
# Keep in mind the origin (x=0, y=0) is in the upper left in image processing
# you'll find these are not sensible values!!
# But you'll get a chance to play with them soon in a quiz ;)

left_bottom = [0, 539]
right_bottom = [900, 300]
apex = [400, 0]

fit_left = np.polyfit((left_bottom[0], apex[0]), (left_bottom[1], apex[1]), 1)
fit_right = np.polyfit((right_bottom[0], apex[0]), (right_bottom[1], apex[1]), 1)
fit_bottom = np.polyfit((left_bottom[0], right_bottom[0]), (left_bottom[1], right_bottom[1]), 1)

# Perform a "bitwise or" to mask pixels below the threshold
color_thresholds = (image[:, :, 0] < rgb_threshold[0]) | \
                   (image[:, :, 1] < rgb_threshold[1]) | \
                   (image[:, :, 2] < rgb_threshold[2])

# Find the region inside the lines
XX, YY = np.meshgrid(np.arange(0, xsize), np.arange(0, ysize))
region_thresholds = (YY > (XX * fit_left[0] + fit_left[1])) & \
                    (YY > (XX * fit_right[0] + fit_right[1])) & \
                    (YY < (XX * fit_bottom[0] + fit_bottom[1]))

# Mask color selection
color_select[color_thresholds] = [0, 0, 0]

# Find where image is both colored right and in the region
line_image[~color_thresholds & region_thresholds] = [255, 0, 0]

# Display our two output images
plt.imshow(color_select)
plt.imshow(line_image)

plt.show()