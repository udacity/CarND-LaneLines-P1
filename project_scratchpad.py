# importing some useful packages
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy as np
import cv2
import colorsys

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


#   START


class LaneLine:
    def __init__(self, x1, y1, x2, y2):
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2

    def slope(self):
        return (self.y2 - self.y1) / (self.x2 - self.x1)

    def y_intercept(self):
        return self.y1 - self.slope * self.x1

    def __str__(self):
        return "(x1, y1, x2, y2, line_equation) == (%s, %s, %s, %s, y = %s * x + %s)" % (
            self.x1, self.y1, self.x2, self.y2, self.slope, self.y_intercept)


class HoughTransformPipeline:
    def __init__(self, rho=1, theta=np.pi / 180, threshold=1, min_line_length=10, max_line_gap=1):
        self.rho = rho
        self.theta = theta
        self.threshold = threshold
        self.min_line_length = min_line_length
        self.max_line_gap = max_line_gap


class PipelineContext:
    def __init__(self, gaussian_kernel_size=5, canny_low_threshold=50, canny_high_threshold=150,
                 region_bottom_offset=55, region_vertice_weights=np.array([(1, 1), (0.48, 0.60), (0.54, 0.60), (1, 1)]),
                 hough_transform_pipeline=HoughTransformPipeline()):
        self.gaussian_kernel_size = gaussian_kernel_size  # Must be an odd number (3, 5, 7...)
        self.canny_low_threshold = canny_low_threshold
        self.canny_high_threshold = canny_high_threshold
        self.region_bottom_offset = region_bottom_offset
        self.region_vertice_weights = region_vertice_weights
        self.hough_transform_pipeline = hough_transform_pipeline
        self.vertices = None
        self.cvt_hsv = False
        self.current_frame = 0
        self.l_prev_x1 = self.l_prev_y1 = self.l_prev_y2 = self.l_prev_x2 = self.l_abs_min_y = None
        self.r_prev_x1 = self.r_prev_y1 = self.r_prev_y2 = self.r_prev_x2 = self.r_abs_min_y = None

    def reset(self):
        self.current_frame = 0
        return self

    def process_video(self, src_video_path, dst_video_path, audio=False):
        self.current_frame = 0
        VideoFileClip(src_video_path).fl_image(self.process_image).write_videofile(dst_video_path, audio=audio)

    def process_image(self, image):
        self.current_frame += 1

        if self.cvt_hsv:
            hsv_img = self.hsv(image)

            if self.current_frame == 1:
                mpimg.imsave("1_hsv_1_" + str(self.current_frame), hsv_img)

            # Define a kernel size for Gaussian smoothing / blurring
            blur_hsv = self.gaussian_noise(hsv_img, self.gaussian_kernel_size)

            if self.current_frame == 1:
                mpimg.imsave("1_hsv_blur_" + str(self.current_frame), blur_hsv)

            WHITE_MIN_RGB = np.uint8([[[50, 50, 50]]])
            WHITE_MAX_RGB = np.uint8([[[150, 150, 150]]])

            WHITE_MIN_HSV = cv2.cvtColor(WHITE_MIN_RGB, cv2.COLOR_BGR2HSV)
            WHITE_MAX_HSV = cv2.cvtColor(WHITE_MAX_RGB, cv2.COLOR_BGR2HSV)

            WHITE_MIN = np.array(WHITE_MIN_HSV, np.uint8)
            WHITE_MAX = np.array(WHITE_MAX_HSV, np.uint8)

            # YELLOW_MIN = np.array([255, 226, 143], np.uint8)
            # YELLOW_MAX = np.array([255, 199, 37], np.uint8)

            blur_hsv_white = cv2.inRange(blur_hsv, WHITE_MIN, WHITE_MAX)
            if self.current_frame == 1:
                mpimg.imsave("1_hsv_white_" + str(self.current_frame), blur_hsv_white)

            # blur_hsv_yellow = cv2.inRange(blur_hsv, YELLOW_MIN, YELLOW_MAX)
            # if self.current_frame == 1:
            #     mpimg.imsave("1_hsv_yellow_" + str(self.current_frame), blur_hsv_yellow)

            # Define our parameters for Canny and run it
            low_threshold = self.canny_low_threshold
            high_threshold = self.canny_high_threshold
            edges = self.canny(blur_hsv, low_threshold, high_threshold)

            if self.current_frame == 1:
                mpimg.imsave("1_hsv_canny_" + str(self.current_frame), edges)

        else:
            # call as plt.imshow(gray, cmap='gray') to show a grayscaled image
            gray = self.grayscale(image)

            # Define a kernel size for Gaussian smoothing / blurring
            blur_gray = self.gaussian_noise(gray, self.gaussian_kernel_size)

            # Define our parameters for Canny and run it
            low_threshold = self.canny_low_threshold
            high_threshold = self.canny_high_threshold
            edges = self.canny(blur_gray, low_threshold, high_threshold)

        # This time we are defining a four sided polygon to mask
        imshape = image.shape

        bottom_offset = self.region_bottom_offset
        img_height = imshape[0]
        img_width = imshape[1]

        # (W, H) == (x, y)
        self.vertices = np.array([
            [
                # bottom left
                (bottom_offset, img_height) * self.region_vertice_weights[0],

                # top left
                (img_width, img_height) * self.region_vertice_weights[1],

                # top right
                (img_width, img_height) * self.region_vertice_weights[2],

                # bottom right
                (img_width - bottom_offset, img_height) * self.region_vertice_weights[3]
            ]
        ], dtype=np.int32)

        masked_edges = self.region_of_interest(edges)

        # Define the Hough transform parameters
        # Make a blank the same size as our image to draw on

        hough = self.hough_lines(image, masked_edges)

        # Create a "color" binary image to combine with line image
        color_edges = np.dstack((edges, edges, edges))

        α = 0.8
        β = 1.
        λ = 0.
        weighted_hough = self.weighted_img(hough, image, α, β, λ)

        # if self.current_frame == 1:
        #     mpimg.imsave("1_orig_" + str(self.current_frame), image)
        #     mpimg.imsave("2_gray_" + str(self.current_frame), gray, cmap='gray')
        #     mpimg.imsave("3_edges_" + str(self.current_frame), edges, cmap='Greys_r')
        #     mpimg.imsave("4_hough_" + str(self.current_frame), hough)
        #     mpimg.imsave("5_color_edges_" + str(self.current_frame), color_edges)
        #     mpimg.imsave("6_weighted_huff_" + str(self.current_frame), weighted_hough)
        # else:
        #     mpimg.imsave("5_color_edges_" + str(self.current_frame), color_edges)

        return weighted_hough

    def hsv(self, img):
        """Converts colorspace from RGB to HSV
        This will return an image with HSV color space
        but NOTE: to see the returned image as HSV
        you should call plt.imshow(hsv)"""
        return cv2.cvtColor(img, cv2.COLOR_RGB2HSV)
        # return cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

    def grayscale(self, img):
        """Applies the Grayscale transform
        This will return an image with only one color channel
        but NOTE: to see the returned image as grayscale
        you should call plt.imshow(gray, cmap='gray')"""
        return cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    def canny(self, img, low_threshold, high_threshold):
        """Applies the Canny transform"""
        return cv2.Canny(img, low_threshold, high_threshold)

    def gaussian_noise(self, img, kernel_size):
        """Applies a Gaussian Noise kernel"""
        return cv2.GaussianBlur(img, (kernel_size, kernel_size), 0)

    def region_of_interest(self, img):
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
        cv2.fillPoly(mask, self.vertices, ignore_mask_color)

        # returning the image only where mask pixels are nonzero
        masked_image = cv2.bitwise_and(img, mask)
        return masked_image

    def find_least_squares_line(self, lines):
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

        all_x = (all_x1 + all_x2)
        all_y = (all_y1 + all_y2)
        mean_x = sum(all_x) / len(all_x)
        mean_y = sum(all_y) / len(all_y)

        m = sum([(xi - mean_x) * (yi - mean_y) for xi, yi in zip(all_x, all_y)]) / sum(
            [(xi - mean_x) ** 2 for xi in zip(all_x)])
        b = mean_y - m * mean_x

        return m, b

    def draw_left_line(self, img, lines, color=[255, 0, 0], thickness=5):
        # abs_max_y = img.shape[0]
        abs_max_y = self.vertices[0][0][1]

        all_y2 = []
        left_slopes = []
        left_intercepts = []

        for x1, y1, x2, y2, angle, m, b in lines:
            all_y2.append(y2)
            left_slopes.append(m)
            left_intercepts.append(b)

        # Find the average of all slopes and y-intercepts to essentially center the final line along the lane line
        # m = sum(left_slopes) / len(left_slopes)
        # b = sum(left_intercepts) / len(left_intercepts)

        # Least squares is a wee bit smoother
        m, b = self.find_least_squares_line(lines)

        # print('least squares line: y = ', m, '*x', '+', b)
        # print('left line count: ', len(lines))
        # print('my least squares line: y = ', m, '*x', '+', b)

        # m = (avg_y2 - avg_y1) / (avg_x2 - avg_x1)
        # b = avg_y1 - m * avg_x1

        # Smooth out our y2 by remembering the smallest y2.
        # doesn't work well on curves at which point I would switch to a
        # different algorithm for curve analysis
        if self.l_abs_min_y is None:
            self.l_abs_min_y = min(all_y2)
        y2 = min(self.l_abs_min_y, min(all_y2))
        self.l_abs_min_y = y2

        y1 = abs_max_y
        x1 = int((y1 - b) / m)
        x2 = int((y2 - b) / m)

        α = 0.2

        # Smooth out the line
        if self.l_prev_y1 is not None:
            y1 = int(self.l_prev_y1 * (1 - α) + y1 * α)

        if self.l_prev_y2 is not None:
            y2 = int(self.l_prev_y2 * (1 - α) + y2 * α)

        if self.l_prev_x1 is not None:
            x1 = int(self.l_prev_x1 * (1 - α) + x1 * α)

        if self.l_prev_x2 is not None:
            x2 = int(self.l_prev_x2 * (1 - α) + x2 * α)

        cv2.line(img, (x1, y1), (x2, y2), color, thickness)

        # keep our globals updated
        self.l_prev_y1 = y1
        self.l_prev_y2 = y2
        self.l_prev_x1 = x1
        self.l_prev_x2 = x2

    def draw_right_line(self, img, lines, color=[255, 0, 0], thickness=5):

        # abs_max_y = img.shape[0]
        abs_max_y = self.vertices[0][3][1]

        all_y1 = []
        slopes = []
        intercepts = []

        for x1, y1, x2, y2, angle, m, b in lines:
            all_y1.append(y1)
            slopes.append(m)
            intercepts.append(b)

        # Find the average of all slopes and y-intercepts to essentially center the final line along the lane line
        # m = sum(slopes) / len(slopes)
        # b = sum(intercepts) / len(intercepts)

        # Least squares is a wee bit smoother
        m, b = self.find_least_squares_line(lines)

        # Smooth out our y1 by remembering the smallest y1
        # doesn't work well on curves at which point I would switch to a
        # different algorithm for curve analysis

        if self.r_abs_min_y is None:
            self.r_abs_min_y = min(all_y1)
        y1 = min(self.r_abs_min_y, min(all_y1))
        self.r_abs_min_y = y1

        x1 = int((self.r_abs_min_y - b) / m)
        y2 = abs_max_y
        x2 = int((y2 - b) / m)

        α = 0.1

        # Smooth out the line
        if self.r_prev_y1 is not None:
            y1 = int(self.r_prev_y1 * (1 - α) + y1 * α)

        if self.r_prev_y2 is not None:
            y2 = int(self.r_prev_y2 * (1 - α) + y2 * α)

        if self.r_prev_x1 is not None:
            x1 = int(self.r_prev_x1 * (1 - α) + x1 * α)

        if self.r_prev_x2 is not None:
            x2 = int(self.r_prev_x2 * (1 - α) + x2 * α)

        cv2.line(img, (x1, y1), (x2, y2), color, thickness)

        # keep our globals updated
        self.r_prev_y1 = y1
        self.r_prev_y2 = y2
        self.r_prev_x1 = x1
        self.r_prev_x2 = x2

    def draw_lines(self, img, lines, color=[255, 0, 0], thickness=8):
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
            print('ERROR: frame ', self.current_frame, ' has no lines detected.')
            return

        left_lines = []
        right_lines = []

        # This iteration splits each line into their respective line side bucket.
        # Negative line angles are left lane lines
        # Positive line angles are right lane lines
        # We also filter out outlier lines such as horizontal lines by specifying a
        # range of acceptable angles. There is likely a better way but I feel
        # this is accurate enough for first pass.
        for line in lines:
            for x1, y1, x2, y2 in line:

                # An offset may be specified to compensate for pixels that are made up by
                # erroneous data such as a hood or dashboard reflection

                # compute the angle of the line - it's just easier for me to visualize in degrees
                # than float ranges
                angle = math.atan2(y2 - y1, x2 - x1) * 180.0 / np.pi

                if angle is not 0.:
                    m = (y2 - y1) / (x2 - x1)
                    b = y1 - m * x1

                    line_tuple = tuple((x1, y1, x2, y2, angle, m, b))

                    # left lane line
                    if -60 < angle <= -25:
                        left_lines.append(line_tuple)

                    # right lane line
                    elif 20 <= angle <= 45:
                        right_lines.append(line_tuple)

                    else:
                        print('OOB line detected in frame ', self.current_frame, ': ', line_tuple)

        if len(left_lines) > 0:
            self.draw_left_line(img, left_lines, color, thickness)
        else:
            print('ERROR: frame ', self.current_frame, ' has no LEFT lines detected.')

        if len(right_lines) > 0:
            self.draw_right_line(img, right_lines, color, thickness)
        else:
            print('ERROR: frame ', self.current_frame, ' has no RIGHT lines detected.')

    def hough_lines(self, orig_img, img):
        """
        `img` should be the output of a Canny transform.

        Returns an image with hough lines drawn.
        """
        lines = cv2.HoughLinesP(img, self.hough_transform_pipeline.rho, self.hough_transform_pipeline.theta,
                                self.hough_transform_pipeline.threshold, np.array([]),
                                minLineLength=self.hough_transform_pipeline.min_line_length,
                                maxLineGap=self.hough_transform_pipeline.max_line_gap)
        # line_img = np.zeros(img.shape, dtype=np.uint8)
        line_img = np.copy(orig_img) * 0  # creating a blank to draw lines on

        # mpimg.imsave("hough", line_img)

        self.draw_lines(line_img, lines)
        return line_img

    def weighted_img(self, img, initial_img, α=0.8, β=1., λ=0.):
        """
        `img` is the output of the hough_lines(), An image with lines drawn on it.
        Should be a blank image (all black) with lines drawn on it.

        `initial_img` should be the image before any processing.

        The result image is computed as follows:

        initial_img * α + img * β + λ
        NOTE: initial_img and img must be the same shape!
        """
        return cv2.addWeighted(initial_img, α, img, β, λ)


#
#   Test on Images
#
#   Now you should build your pipeline to work on the images in the directory "test_images"
#   You should make sure your pipeline works well on these images before you try the videos.
#



# This pipeline context is sufficient for all test_images as well as for solidYellowLeft.mp4 and solidWhiteRight.mp4
pipeline_context = PipelineContext(gaussian_kernel_size=3, canny_low_threshold=50, canny_high_threshold=150,
                                   region_bottom_offset=55,
                                   region_vertice_weights=np.array([(1, 1), (0.48, 0.60), (0.54, 0.60), (1, 1)]),
                                   hough_transform_pipeline=HoughTransformPipeline(rho=2, theta=np.pi / 180,
                                                                                   threshold=40,
                                                                                   min_line_length=10,
                                                                                   max_line_gap=120))

import os
# for image_name in os.listdir("test_images/"):
#     if image_name == '.DS_Store':
#         continue
#     pipeline_context.reset
#     result = pipeline_context.process_image(mpimg.imread('test_images/' + image_name))
#     mpimg.imsave("RENDERED_" + image_name, result)

# Import everything needed to edit/save/watch video clips
from moviepy.editor import VideoFileClip

pipeline_context.process_video('solidWhiteRight.mp4', 'white.mp4')
pipeline_context.process_video('solidYellowLeft.mp4', 'yellow.mp4')

# This pipeline context is sufficient for all test_images as well as for solidYellowLeft.mp4 and solidWhiteRight.mp4
pipeline_context = PipelineContext(gaussian_kernel_size=3, canny_low_threshold=50, canny_high_threshold=150,
                                   region_bottom_offset=55,
                                   region_vertice_weights=np.array(
                                       [(1, 0.95), (0.40, 0.65), (0.60, 0.65), (1, 0.935)]),
                                   hough_transform_pipeline=HoughTransformPipeline(rho=2, theta=np.pi / 180,
                                                                                   threshold=40,
                                                                                   min_line_length=15,
                                                                                   max_line_gap=250))

# pipeline_context.process_video('challenge.mp4', 'extra.mp4')
# pipeline_context.process_video('custom_me_night_2.mp4', 'custom_me_night_2_RENDERED.mp4')
