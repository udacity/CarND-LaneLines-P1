# URL: https://classroom.udacity.com/nanodegrees/nd013/parts/fbf77062-5703-404e-b60c-95b78b2f3f9e/modules/83ec35ee-1e02-48a5-bdb7-d244bd47c2dc/lessons/8c82408b-a217-4d09-b81d-1bda4c6380ef/concepts/a26d7fdd-291e-46f4-b3eb-01189cbb8afa

# Coding up a Region of Interest Mask

# Awesome! Now you've seen that with a simple color selection we have managed to eliminate almost everything in the
# image except the lane lines. At this point, however, it would still be tricky to extract the exact lines
# automatically, because we still have some other objects detected around the periphery that aren't lane lines.

# In this case, I'll assume that the front facing camera that took the image is mounted in a fixed position on the car,
# such that the lane lines will always appear in the same general region of the image. Next, I'll take advantage of
# this by adding a criterion to only consider pixels for color selection in the region where we expect to find the
# lane lines.

# Check out the code below. The variables left_bottom, right_bottom, and apex represent the vertices of a triangular
# region that I would like to retain for my color selection, while masking everything else out.


import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy as np

image = mpimg.imread('../test_images/solidWhiteRight.jpg')
print('This image is: ', type(image), 'with dimensions:', image.shape)

ysize = image.shape[0]
xsize = image.shape[1]

region_select = np.copy(image)

left_bottom = [0, 539]
right_bottom = [900, 300]
apex = [400, 0]

fit_left = np.polyfit((left_bottom[0], apex[0]), (left_bottom[1], apex[1]), 1)
fit_right = np.polyfit((right_bottom[0], apex[0]), (right_bottom[1], apex[1]), 1)
fit_bottom = np.polyfit((left_bottom[0], right_bottom[0]), (left_bottom[1], right_bottom[1]), 1)

print('fit_left: ', fit_left)
print('fit_left[0]: ', fit_left[0])
print('fit_left[1]: ', fit_left[1])

print('fit_right: ', fit_right)
print('fit_bottom:', fit_bottom)

XX, YY = np.meshgrid(np.arange(0, xsize), np.arange(0, ysize))

print('XX: ', XX)
print('YY: ', YY)


region_thresholds = (YY > (XX*fit_left[0]+fit_left[1])) & \
                    (YY > (XX*fit_right[0]+fit_right[1])) & \
                    (YY < (XX*fit_bottom[0]+fit_bottom[1]))

region_select[~region_thresholds] = [255, 0, 0]

plt.imshow(region_select)

plt.show()