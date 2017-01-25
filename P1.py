#importing some useful packages
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy as np
import cv2
import math
from scipy.spatial import distance
import os

prev_start_left_x = 0
prev_start_left_y = 0
prev_end_left_x = 0
prev_end_left_y = 0
prev_start_right_x = 0
prev_start_right_y = 0
prev_end_right_x = 0
prev_end_right_y = 0
start_left_x = 0
start_left_y = 0
start_right_x = 0
start_right_y = 0
end_left_x = 0
end_right_x = 0
filter_right = 0

def grayscale(img):
    """Applies the Grayscale transform
    This will return an image with only one color channel
    but NOTE: to see the returned image as grayscale
    (assuming your grayscaled image is called 'gray')
    you should call plt.imshow(gray, cmap='gray')"""
    return cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
    # Or use BGR2GRAY if you read an image with cv2.imread()
    # return cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)


def canny(img, low_threshold, high_threshold):
    """Applies the Canny transform"""
    return cv2.Canny(img, low_threshold, high_threshold)


def gaussian_blur(img, kernel_size):
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

def euclideanDist(x1, y1, x2, y2):
    d = np.sqrt(((x1-x2)*(x1-x2))+((y1-y2)*(y1-y2)))
    return d

def filterBySlope(lines, left_slopes, left_lines, right_slopes, right_lines, m_low=0.4, m_high=0.8):
    slope_theta_threshold = 0.3
    for line in lines:
        for x1, y1, x2, y2 in line:
            m = (y2-y1)/(x2-x1)
            # filter out lines close to horizontal
            if np.abs(np.arctan2((y2-y1), (x2-x1))) > slope_theta_threshold:
                if m>= -m_high and m <= -m_low:
                    left_slopes.append(m)
                    if(x1 > x2):
                        left_lines.append((x1,y1,x2,y2))
                    else:
                        left_lines.append((x2,y2,x1,y1))
                elif m >= m_low and m <= m_high:
                    right_slopes.append(m)
                    if(x1 < x2):
                        right_lines.append((x1,y1,x2,y2))
                    else:
                        right_lines.append((x2,y2,x1,y1))

def consolidateLines(img, left_lines, right_lines, left_slopes, right_slopes, thickness, debug = 0):
    global start_left_x
    global start_left_y
    global start_right_x
    global start_right_y
    global end_left_x
    global end_right_x

    # debug
    if debug:
        color = [0, 255, 0]
        for line in left_lines:
                cv2.circle(img, (line[0],line[1]),2, [0, 255, 0])
                cv2.circle(img, (line[2], line[3]), 2, [0, 0, 255])
                cv2.line(img, (line[0], line[1]), (line[2], line[3]), color, thickness)
        color = [0, 0, 255]
        for line in right_lines:
                cv2.circle(img, (line[0], line[1]), 2, [0, 255, 0], -1)
                cv2.circle(img, (line[2], line[3]), 2, [0, 0, 255],-1)
                cv2.line(img, (line[0], line[1]), (line[2], line[3]), color, thickness)

    # Average left and right slopes
    avg_left_slope = np.mean(sorted(left_slopes))
    avg_right_slope = np.mean(sorted(right_slopes))

    # Compute start points
    start_left_y = int(np.mean(left_lines, axis=0)[1])
    start_left_x = int(np.mean(left_lines, axis=0)[0])

    start_right_y = int(np.mean(right_lines, axis=0)[1])
    start_right_x = int(np.mean(right_lines, axis=0)[0])

    b_left = start_left_y - avg_left_slope*start_left_x
    b_right = start_right_y - avg_right_slope*start_right_x

    # Compute end points
    end_left_x = int((img.shape[1] - start_left_y) / avg_left_slope) + start_left_x
    end_right_x = int((img.shape[1] - start_right_y) / avg_right_slope) + start_right_x

    # Project
    start_left_x = int(img.shape[1]/2-25)
    start_left_y = int(avg_left_slope*start_left_x+b_left)

    start_right_x = int(img.shape[1]/2+25)
    start_right_y = int(avg_right_slope*start_right_x+b_right)

def distanceBetweenLines(u,v):
    return distance.euclidean(u,v)

def filterByIntersect(img, left_lines, right_lines, left_slopes, right_slopes, thickness, debug=0, filter_right = 0):
    intersect_threshold = 1100
    filtered_left_slopes = []
    filtered_left_lines = []
    filtered_right_lines = []
    filtered_right_slopes = []
    font = cv2.FONT_HERSHEY_SIMPLEX

    while(len(filtered_left_lines) <= 0):
        for x in range (0, len(left_lines)):
            line = left_lines[x]
            slope = left_slopes[x]
            d = distanceBetweenLines([line[0]-line[2], line[1]-line[3]], [prev_start_left_x-prev_end_left_x, prev_start_left_y-prev_end_left_y])
            if debug:
                cv2.putText(img, str(d), (line[0], line[1]), font, 0.5, (255, 255, 255), 2)
            if d <= intersect_threshold:
                filtered_left_lines.append(line)
                filtered_left_slopes.append(slope)
                if debug:
                    cv2.line(img, (line[0], line[1]), (line[2], line[3]), [0, 255, 0], thickness)
            else:
                if debug:
                    cv2.line(img, (line[0], line[1]), (line[2], line[3]), [0, 0, 255], thickness)

        intersect_threshold += 50

    if filter_right:
        intersect_threshold = 1100
        while(len(filtered_right_lines) <= 0):
            for x in range (0, len(right_lines)):
                line = right_lines[x]
                slope = right_slopes[x]
                d = distanceBetweenLines([line[0]-line[2], line[1]-line[3]], [prev_start_right_x-prev_end_right_x, prev_start_right_y-prev_end_right_y])
                if debug:
                    cv2.putText(img, str(d), (line[0], line[1]), font, 0.5, (255, 255, 255), 2)
                if d <= intersect_threshold:
                    filtered_right_lines.append(line)
                    filtered_right_slopes.append(slope)
                    if debug:
                        cv2.line(img, (line[0], line[1]), (line[2], line[3]), [0, 255, 0], thickness)
                else:
                    if debug:
                        cv2.line(img, (line[0], line[1]), (line[2], line[3]), [0, 0, 255], thickness)

            intersect_threshold += 50

        # Consolidate lines
        consolidateLines(img, filtered_left_lines, filtered_right_lines, filtered_left_slopes, filtered_right_slopes, thickness)
    else:
        # Consolidate lines
        consolidateLines(img, filtered_left_lines, right_lines, filtered_left_slopes, right_slopes, thickness)

def draw_lines(img, lines, color=[255, 0, 0], thickness=5, debug = 0):
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

    global prev_start_left_x
    global prev_start_left_y
    global prev_end_left_x
    global prev_end_left_y
    global prev_start_right_x
    global prev_start_right_y
    global prev_end_right_x
    global prev_end_right_y
    global start_left_x
    global start_left_y
    global end_left_x
    global end_left_y
    global start_right_x
    global start_right_y
    global end_right_x
    global end_right_y
    global filter_right

    # Group lines by left slope vs right slope
    left_slopes = []
    left_lines = []
    right_slopes = []
    right_lines = []

    m_low = 0.4
    m_high = 0.8
    while len(right_lines) < 1 or len(left_lines) < 1:
        filterBySlope(lines, left_slopes, left_lines, right_slopes, right_lines, m_low, m_high)
        m_low -= 0.1
        m_high += 0.1

    # Consolidate lines
    consolidateLines(img, left_lines, right_lines, left_slopes, right_slopes, thickness)

    # Filter by Intersection and save
    intersect_threshold = 90
    if prev_end_left_x != 0:
        filterByIntersect(img, left_lines, right_lines, left_slopes, right_slopes, thickness, filter_right)

        d = distanceBetweenLines([start_left_x - end_left_x, start_left_y - img.shape[1]],
                                 [prev_start_left_x - prev_end_left_x, prev_start_left_y - prev_end_left_y])
        if(d <= intersect_threshold):
            prev_start_left_x = start_left_x
            prev_start_left_y = start_left_y
            prev_end_left_x = end_left_x
            prev_end_left_y = img.shape[1]
        else:
            if debug:
                font = cv2.FONT_HERSHEY_SIMPLEX
                cv2.putText(img, str(d), (start_left_x, start_left_y), font, 0.5, (255, 255, 255), 2)
                cv2.line(img, (prev_start_left_x, prev_start_left_y), (prev_end_left_x, prev_end_left_y), [0, 255, 0],
                         thickness)
                cv2.line(img, (start_left_x, start_left_y), (end_left_x, img.shape[1]), [0, 0, 255], thickness)
            start_left_x = prev_start_left_x
            start_left_y = prev_start_left_y
            end_left_x = prev_end_left_x
            end_left_y = prev_end_left_x

        if not filter_right:
            d = intersect_threshold
        d = distanceBetweenLines([start_right_x - end_right_x, start_right_y - img.shape[1]],
                                 [prev_start_right_x - prev_end_right_x, prev_start_right_y - prev_end_right_y])
        if (d <= intersect_threshold):
            prev_start_right_x = start_right_x
            prev_start_right_y = start_right_y
            prev_end_right_x = end_right_x
            prev_end_right_y = img.shape[1]
        else:
            start_right_x = prev_start_right_x
            start_right_y = prev_start_right_y
            end_right_x = prev_end_right_x
            end_right_y = prev_end_right_x
    else:
        prev_start_left_x = start_left_x
        prev_start_left_y = start_left_y
        prev_end_left_x = end_left_x
        prev_end_left_y = img.shape[1]
        prev_start_right_x = start_right_x
        prev_start_right_y = start_right_y
        prev_end_right_x = end_right_x
        prev_end_right_y = img.shape[1]

    # Draw lines
    color = [255, 0, 0]
    cv2.line(img, (start_left_x, start_left_y), (end_left_x, img.shape[1]), color, thickness)
    cv2.line(img, (start_right_x, start_right_y), (end_right_x, img.shape[1]), color, thickness)

def hough_lines(img, rho, theta, threshold, min_line_len, max_line_gap):
    """
    `img` should be the output of a Canny transform.

    Returns an image with hough lines drawn.
    """
    lines = cv2.HoughLinesP(img, rho, theta, threshold, np.array([]), minLineLength=min_line_len,
                            maxLineGap=max_line_gap)
    line_img = np.zeros((img.shape[0], img.shape[1], 3), dtype=np.uint8)
    draw_lines(line_img, lines, color=[255, 0, 0], thickness=3)
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

def show_img(img, name):
    cv2.imshow(name, img)
    cv2.waitKey(0)

def FindingLanes(img_color, debug=0):

    # Convert to gray
    img_gray = grayscale(img_color)
    if debug:
        show_img(img_gray, 'gray')

    # Define a kernel size and apply Gaussian smoothing
    kernel_size = 5
    blur_gray = gaussian_blur(img_gray, kernel_size)

    # Define our parameters for Canny and apply
    low_threshold = 50
    high_threshold = 150
    edges = canny(blur_gray, low_threshold, high_threshold)
    if debug:
        show_img(edges, 'edges')

    # Next we'll create a masked edges image using cv2.fillPoly()
    imshape = img_color.shape
    vertices = np.array([[(0, imshape[0]), (490, 290), (490, 290), (imshape[1], imshape[0])]], dtype=np.int32)
    masked_edges = region_of_interest(edges, vertices)
    if debug:
        show_img(masked_edges, 'masked_image')

    # Find lines with Hough transform
    # Make a blank the same size as our image to draw on
    rho = 2  # distance resolution in pixels of the Hough grid
    theta = np.pi / 180  # angular resolution in radians of the Hough grid
    threshold = 15  # minimum number of votes (intersections in Hough grid cell)
    min_line_length = 40  # minimum number of pixels making up a line
    max_line_gap = 20  # maximum gap in pixels between connectable line segments
    line_img = hough_lines(masked_edges, rho, theta, threshold, min_line_length, max_line_gap)
    if debug:
        show_img(line_img, 'line_img')

    # Draw over original image
    blended_img = weighted_img(line_img, img_color, α=0.8, β=1., λ=0.)
    if debug:
        show_img(blended_img, 'blended_img')

    return blended_img

if __name__ == "__main__":
    test_dir = 'test_images'
    for subdir, dirs, files in os.walk(test_dir):
        for img_file in files:
            prev_start_left_x = 0
            prev_start_left_y = 0
            prev_end_left_x = 0
            prev_end_left_y = 0
            prev_start_right_x = 0
            prev_start_right_y = 0
            prev_end_right_x = 0
            prev_end_right_y = 0
            start_left_x = 0
            start_left_y = 0
            start_right_x = 0
            start_right_y = 0
            end_left_x = 0
            end_right_x = 0
            filter_right = 0

            img_file_full = os.path.join(test_dir,img_file)
            # Load an color image from file
            img_color = mpimg.imread(img_file_full)
            debug = 0
            blended_img = FindingLanes(img_color, debug)
            result_file = os.path.join(test_dir,'results',img_file)
            if debug:
                show_img(blended_img, 'blended_img')
                print(result_file)
            cv2.imwrite(result_file, blended_img)

    cv2.destroyAllWindows()



