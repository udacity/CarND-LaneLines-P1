import numpy as np

def select_color(image):
    print('image type: ', type(image), 'image dimensions: ', image.shape)

    # Grab the x and y size and make a copy of the image
    ysize = image.shape[0]
    xsize = image.shape[1]
    color_select = np.copy(image)
    line_image = np.copy(image)

    # Define color selection criteria
    # MODIFY THESE VARIABLES TO MAKE YOUR COLOR SELECTION
    red_threshold = 200
    green_threshold = 200
    blue_threshold = 200

    rgb_threshold = [red_threshold, green_threshold, blue_threshold]

def select_region(image, left_bottom, right_bottom, apex):
    ysize = image.shape[0]
    xsize = image.shape[1]

    region_select = np.copy(image)

    # Define the vertices of a triangular mask.
    # Keep in mind the origin (x=0, y=0) is in the upper left
    # MODIFY THESE VALUES TO ISOLATE THE REGION
    # WHERE THE LANE LINES ARE IN THE IMAGE
    # left_bottom = [0, 539]
    # right_bottom = [900, 300]
    # apex = [400, 0]

    # Perform a linear fit (y=Ax+B) to each of the three sides of the triangle
    # np.polyfit returns the coefficients [A, B] of the fit
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

    region_thresholds = (YY > (XX * fit_left[0] + fit_left[1])) & \
                        (YY > (XX * fit_right[0] + fit_right[1])) & \
                        (YY < (XX * fit_bottom[0] + fit_bottom[1]))

    region_select[~region_thresholds] = [255, 0, 0]

    return region_select
