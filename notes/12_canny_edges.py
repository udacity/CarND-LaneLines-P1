# Do all the relevant imports
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy as np
import cv2


# Read in the image and convert to grayscale
# Note: in the previous example we were reading a .jpg
# Here we read a .png and convert to 0,255 bytescale
image = (mpimg.imread('../test_images/exit_ramp.png') * 255).astype('uint8')
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

plt.imshow(gray, cmap='gray')
# plt.show()

# Define a kernel size for Gaussian smoothing / blurring
kernel_size = 5  # Must be an odd number (3, 5, 7...)
blur_gray = cv2.GaussianBlur(gray, (kernel_size, kernel_size), 0)



# Define our parameters for Canny and run it
low_threshold = 50
high_threshold = 150
edges = cv2.Canny(blur_gray, low_threshold, high_threshold)



# Display the image
plt.imshow(edges, cmap='Greys_r')

plt.show()
