#importing some useful packages
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy as np
import cv2
# matploylib inline

#reading in an image
image = mpimg.imread('test_images/solidWhiteRight.jpg')

#printing out some stats and plotting
print('This image is:', type(image), 'with dimesions:', image.shape)
plt.imshow(image)  #call as plt.imshow(gray, cmap='gray') to show a grayscaled image
plt.show()

#   Some OpenCV functions (beyond those introduced in the lesson) that might be useful for this project are:
#
#   cv2.inRange()         for color selection
#   cv2.fillPoly()        for regions selection
#   cv2.line()            to draw lines on an image given endpoints
#   cv2.addWeighted()     to coadd / overlay two images cv2.cvtColor() to grayscale or change color cv2.imwrite() to
#                           output images to file
#   cv2.bitwise_and()     to apply a mask to an image
#
#   Check out the OpenCV documentation to learn about these and discover even more awesome functionality!
#
#
#   Below are some helper functions to help get you started. They should look familiar from the lesson!
#
#   from helpers import FUNCTION_NAME
#
#   Test on Images
#
#   Now you should build your pipeline to work on the images in the directory "test_images"
#   You should make sure your pipeline works well on these images before you try the videos.
#

import os
print(os.listdir("test_images/"))

#   run your solution on all test_images and make copies into the test_images directory).
#
#   Test on Videos
#
#   You know what's cooler than drawing lanes over images? Drawing lanes over video!
#
#   We can test our solution on two provided videos:
#
#       solidWhiteRight.mp4
#       solidYellowLeft.mp4
#
#   # Import everything needed to edit/save/watch video clips

from moviepy.editor import VideoFileClip
from IPython.display import HTML

def process_image(image):
    # TODO: put your pipeline here,
    # you should return the final output (image with lines are drawn on lanes)

    return result

#   Let's try the one with the solid white lane on the right first ...

white_output = 'white.mp4'
clip1 = VideoFileClip("solidWhiteRight.mp4")
white_clip = clip1.fl_image(process_image)
white_clip.write_videofile(white_output, audio=False)

#
#
#
#
