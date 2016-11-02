# importing some useful packages
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy as np
import cv2
# matploylib inline

#   Some OpenCV functions (beyond those introduced in the lesson) that might be useful for this project are:
#
#   cv2.inRange()         for color selection
#
#       http://docs.opencv.org/2.4/modules/core/doc/operations_on_arrays.html?highlight=inrange#cv2.inRange
#
#
#   cv2.fillPoly()        for regions selection
#
#       http://docs.opencv.org/2.4/modules/core/doc/drawing_functions.html?highlight=fillpoly#cv2.fillPoly
#
#
#   cv2.line()            to draw lines on an image given endpoints
#
#       http://docs.opencv.org/2.4/modules/core/doc/drawing_functions.html?highlight=line#cv2.line
#
#
#   cv2.addWeighted()     to coadd / overlay two images cv2.cvtColor() to grayscale or change color cv2.imwrite() to
#                           output images to file
#
#       http://docs.opencv.org/2.4/modules/core/doc/operations_on_arrays.html?highlight=addweighted#cv2.addWeighted
#
#
#   cv2.bitwise_and()     to apply a mask to an image
#
#       http://docs.opencv.org/2.4/modules/core/doc/operations_on_arrays.html?highlight=bitwise_and#cv2.bitwise_and
#
#
#   Check out the OpenCV documentation to learn about these and discover even more awesome functionality!
#
#
#   Below are some helper functions to help get you started. They should look familiar from the lesson!
#
#   from helpers import FUNCTION_NAME

import math


def grayscale(img):
    """Applies the Grayscale transform
    This will return an image with only one color channel
    but NOTE: to see the returned image as grayscale
    you should call plt.imshow(gray, cmap='gray')"""
    return cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)


def canny(img, low_threshold, high_threshold):
    """Applies the Canny transform"""
    return cv2.Canny(img, low_threshold, high_threshold)


def gaussian_noise(img, kernel_size):
    """Applies a Gaussian Noise kernel"""
    return cv2.GaussianBlur(img, (kernel_size, kernel_size), 0)


def region_of_interest(img, vertices):
    """
    Applies an image mask.

    Only keeps the region of the image defined by the polygon
    formed from `vertices`. The rest of the image is set to black.
    """
    # defining a blank mask to start with
    mask = np.zeros_like(img)

    # defining a 3 channel or 1 channel color to fill the mask with depending on the input image
    if len(img.shape) > 2:
        channel_count = img.shape[2]  # i.e. 3 or 4 depending on your image
        ignore_mask_color = (255,) * channel_count
    else:
        ignore_mask_color = 255

    # filling pixels inside the polygon defined by "vertices" with the fill color
    cv2.fillPoly(mask, vertices, ignore_mask_color)

    # returning the image only where mask pixels are nonzero
    masked_image = cv2.bitwise_and(img, mask)
    return masked_image


l_prev_x1 = l_prev_y1 = l_prev_y2 = l_prev_x2 = l_abs_min_y = None
r_prev_x1 = r_prev_y1 = r_prev_y2 = r_prev_x2 = r_abs_min_y = None


def draw_left_line(img, lines, color=[255, 0, 0], thickness=15):
    global l_prev_x1, l_prev_y1, l_prev_y2, l_prev_x2, l_abs_min_y

    print('left line count: ', len(lines))

    abs_max_y = img.shape[0]

    all_x1 = []
    all_y1 = []
    all_x2 = []
    all_y2 = []
    left_slopes = []
    left_intercepts = []

    for x1, y1, x2, y2, angle, m, b in lines:
        all_x1.append(x1)
        all_y1.append(y1)
        all_x2.append(x2)
        all_y2.append(y2)
        left_slopes.append(m)
        left_intercepts.append(b)

    avg_x1 = sum(all_x1) / len(all_x1)
    avg_y1 = sum(all_y1) / len(all_y1)
    avg_x2 = sum(all_x2) / len(all_x2)
    avg_y2 = sum(all_y2) / len(all_y2)

    # Find the average of all slopes and y-intercepts to essentially center the final line along the lane line
    m = sum(left_slopes) / len(left_slopes)
    b = sum(left_intercepts) / len(left_intercepts)

    # m = (avg_y2 - avg_y1) / (avg_x2 - avg_x1)
    # b = avg_y1 - m * avg_x1

    # Smooth out our y2 by remembering the smallest y2.
    # doesn't work well on curves at which point I would switch to a
    # different algorithm for curve analysis
    if l_abs_min_y is None:
        l_abs_min_y = min(all_y2)
    y2 = min(l_abs_min_y, min(all_y2))
    l_abs_min_y = y2

    y1 = abs_max_y
    # y1 = max(all_y1)
    x1 = int((y1 - b) / m)
    x2 = int((y2 - b) / m)

    if l_prev_y1 is None:
        alp = 1
    else:
        alp = 0.1

    # Smooth out the line
    if l_prev_y1 is not None:
        y1 = int(l_prev_y1 * (1 - alp) + y1 * alp)

    if l_prev_y2 is not None:
        y2 = int(l_prev_y2 * (1 - alp) + y2 * alp)

    if l_prev_x1 is not None:
        x1 = int(l_prev_x1 * (1 - alp) + x1 * alp)

    if l_prev_x2 is not None:
        x2 = int(l_prev_x2 * (1 - alp) + x2 * alp)

    cv2.line(img, (x1, y1), (x2, y2), color, thickness)

    # keep our globals updated
    l_prev_y1 = y1
    l_prev_y2 = y2
    l_prev_x1 = x1
    l_prev_x2 = x2


def draw_right_line(img, lines, color=[255, 0, 0], thickness=15):
    global r_prev_x1, r_prev_y1, r_prev_y2, r_prev_x2, r_abs_min_y

    abs_max_y = img.shape[0]

    all_y1 = []
    slopes = []
    intercepts = []

    for x1, y1, x2, y2, angle, m, b in lines:
        all_y1.append(y1)
        slopes.append(m)
        intercepts.append(b)

    # Find the average of all slopes and y-intercepts to essentially center the final line along the lane line
    m = sum(slopes) / len(slopes)
    b = sum(intercepts) / len(intercepts)

    # Smooth out our y1 by remembering the smallest y1
    # doesn't work well on curves at which point I would switch to a
    # different algorithm for curve analysis

    if r_abs_min_y is None:
        r_abs_min_y = min(all_y1)
    y1 = min(r_abs_min_y, min(all_y1))
    r_abs_min_y = y1

    x1 = int((r_abs_min_y - b) / m)
    y2 = abs_max_y
    x2 = int((y2 - b) / m)

    if r_prev_y1 is None:
        alp = 1
    else:
        alp = 0.1

    # Smooth out the line
    if r_prev_y1 is not None:
        y1 = int(r_prev_y1 * (1 - alp) + y1 * alp)

    if r_prev_y2 is not None:
        y2 = int(r_prev_y2 * (1 - alp) + y2 * alp)

    if r_prev_x1 is not None:
        x1 = int(r_prev_x1 * (1 - alp) + x1 * alp)

    if r_prev_x2 is not None:
        x2 = int(r_prev_x2 * (1 - alp) + x2 * alp)

    cv2.line(img, (x1, y1), (x2, y2), color, thickness)

    # keep our globals updated
    r_prev_y1 = y1
    r_prev_y2 = y2
    r_prev_x1 = x1
    r_prev_x2 = x2


def draw_lines(img, lines, color=[255, 0, 0], thickness=15):
    """
    NOTE: this is the function you might want to use as a starting point once you want to
    average/extrapolate the line segments you detect to map out the full
    extent of the lane (going from the result shown in raw-lines-example.mp4
    to that shown in P1_example.mp4).

    Think about things like separating line segments by their
    slope ((y2-y1)/(x2-x1)) to decide which segments are part of the left
    line vs. the right line.  Then, you can average the position of each of
    the lines and extrapolate to the top and bottom of the lane.

    This function draws `lines` with `color` and `thickness`.
    Lines are drawn on the image inplace (mutates the image).
    If you want to make the lines semi-transparent, think about combining
    this function with the weighted_img() function below
    """

    if lines is None or len(lines) <= 0:
        return

    left_lines = []
    right_lines = []

    # This iteration splits each line into their respective line side bucket.
    # Negative line angles are left lane lines
    # Positive line angles are right lane lines
    # We also filter out outlier lines such as horizontal lines by specifying a
    # range of acceptable angles. There is definitely a better way but I feel
    # this is accurate enough for first pass.
    for line in lines:
        for x1, y1, x2, y2 in line:

            # compute the angle of the line
            angle = math.atan2(y2 - y1, x2 - x1) * 180.0 / np.pi
            m = (y2 - y1) / (x2 - x1)
            b = y1 - m * x1

            # left lane line
            if -45 < angle <= -20:
                left_lines.append(tuple((x1, y1, x2, y2, angle, m, b)))

            # right lane line
            elif 20 <= angle <= 45:
                right_lines.append(tuple((x1, y1, x2, y2, angle, m, b)))
            else:
                if len(right_lines) > 0:
                    right_lines.append(right_lines[len(right_lines) - 1])
                if len(left_lines) > 0:
                    left_lines.append(left_lines[len(left_lines) - 1])

    if len(left_lines) > 0:
        draw_left_line(img, left_lines, color, thickness)

    if len(right_lines) > 0:
        draw_right_line(img, right_lines, color, thickness)


def hough_lines(orig_img, img, rho, theta, threshold, min_line_len, max_line_gap):
    """
    `img` should be the output of a Canny transform.

    Returns an image with hough lines drawn.
    """
    lines = cv2.HoughLinesP(img, rho, theta, threshold, np.array([]), minLineLength=min_line_len,
                            maxLineGap=max_line_gap)
    # line_img = np.zeros(img.shape, dtype=np.uint8)
    line_img = np.copy(orig_img) * 0  # creating a blank to draw lines on

    draw_lines(line_img, lines)
    return line_img


# Python 3 has support for cool math symbols.

def weighted_img(img, initial_img, α=0.8, β=1., λ=0.):
    """
    `img` is the output of the hough_lines(), An image with lines drawn on it.
    Should be a blank image (all black) with lines drawn on it.

    `initial_img` should be the image before any processing.

    The result image is computed as follows:

    initial_img * α + img * β + λ
    NOTE: initial_img and img must be the same shape!
    """
    return cv2.addWeighted(initial_img, α, img, β, λ)


#   START

def process_image(image):
    # call as plt.imshow(gray, cmap='gray') to show a grayscaled image
    gray = grayscale(image)
    # plt.imshow(gray, cmap='gray')
    # plt.show()

    # Define a kernel size for Gaussian smoothing / blurring
    kernel_size = 5  # Must be an odd number (3, 5, 7...)
    blur_gray = gaussian_noise(gray, kernel_size)

    # Define our parameters for Canny and run it
    low_threshold = 50
    high_threshold = 150
    edges = canny(blur_gray, low_threshold, high_threshold)

    # Display the image
    # plt.imshow(edges, cmap='Greys_r')
    # plt.show()


    # region mask

    # This time we are defining a four sided polygon to mask
    imshape = image.shape

    bottom_offset = 55
    img_height = imshape[0]
    img_width = imshape[1]

    # (W, H) == (x, y)
    vertices = np.array([
        [
            (bottom_offset, img_height),  # bottom left
            (img_width * 0.48, img_height * 0.60),  # top left
            (img_width * 0.54, img_height * 0.60),  # top right
            (img_width - bottom_offset, img_height)  # bottom right
        ]
    ], dtype=np.int32)

    masked_edges = region_of_interest(edges, vertices)

    # Define the Hough transform parameters
    # Make a blank the same size as our image to draw on
    #
    # Defaults:
    # rho = 1
    # theta = np.pi/180
    # threshold = 1
    # min_line_length = 10
    # max_line_gap = 1

    rho = 2
    theta = np.pi / 180
    threshold = 40
    min_line_length = 20
    max_line_gap = 50

    result = hough_lines(image, masked_edges, rho, theta, threshold, min_line_length, max_line_gap)

    # Create a "color" binary image to combine with line image
    color_edges = np.dstack((edges, edges, edges))

    α = 0.8
    β = 1.
    λ = 0.
    result = weighted_img(result, image, α, β, λ)

    return result


#
#   Test on Images
#
#   Now you should build your pipeline to work on the images in the directory "test_images"
#   You should make sure your pipeline works well on these images before you try the videos.
#


import os

for image_name in os.listdir("test_images/"):
    if image_name == '.DS_Store':
    # if image_name == '.DS_Store' or image_name != 'whiteCarLaneSwitch.jpg':
    # if image_name == '.DS_Store' or image_name != 'solidWhiteCurve.jpg':
    # if image_name == '.DS_Store' or image_name != 'solidYellowCurve.jpg':
    # if image_name == '.DS_Store' or image_name != 'solidYellowCurve2.jpg':
    # if image_name == '.DS_Store' or image_name != 'horzLineTest.jpg':
        continue
    image = mpimg.imread('test_images/' + image_name)
    result = process_image(image)
    mpimg.imsave("RENDERED_" + image_name, result)


# Import everything needed to edit/save/watch video clips
from moviepy.editor import VideoFileClip

white_output = 'white.mp4'
clip1 = VideoFileClip("solidWhiteRight.mp4")
white_clip = clip1.fl_image(process_image)
white_clip.write_videofile(white_output, audio=False)

yellow_output = 'yellow.mp4'
clip2 = VideoFileClip('solidYellowLeft.mp4')
yellow_clip = clip2.fl_image(process_image)
yellow_clip.write_videofile(yellow_output, audio=False)

# challenge_output = 'extra.mp4'
# clip2 = VideoFileClip('challenge.mp4')
# challenge_clip = clip2.fl_image(process_image)
# challenge_clip.write_videofile(challenge_output, audio=False)

# me_output = 'me2.mp4'
# clip2 = VideoFileClip('custom_me_night_2.mp4')
# me_clip = clip2.fl_image(process_image)
# me_clip.write_videofile(me_output, audio=False)