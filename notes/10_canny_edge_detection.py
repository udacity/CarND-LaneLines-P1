# Video 1
# input:    gray - a grayscale image
# output:   edge - another image
# low_threshold and high_threshold determine how strong the edges must be to be detected.
# you can think of the strength of an edge as being defined by how different the values are
# in adjacent pixels in the image. In other words, "the strength of the gradient".

edge = cv2.Canny(gray, low_threshold, high_threshold)


# Video 2

# When looking at grayscale images you see bright points, dark points and all the gray points in between.
# Rapid changes in brightness are where we find the edges.
# In image is just a mathematical formula of X and Y so we can perform mathematical operations on it just like
# any other function.
# For example, we can take the derivative of an image which is just a measure of change of this function.
# A small derivative means small change; big derivative, BIG change.
# Images are 2-dimensional so it makes sense to take the derivative with respect to X and Y simultaneously.
# This is called "The Gradient" and in computing it, we're measuring how fast pixels values are changing at each
# point in an image and in which direction they're changing most rapidly.
#
# Computing the gradient gives us thick edges. With the Canny algorithm, we will thin out these edges to find the
# individual pixels that follow the strongest gradients. We'll then extend those strong edges to include pixels all
# the way down to the lower threshold that we defined when calling the Canny function.


# Note! The standard location of the origin (x=0, y=0) for images is in the top left corner with y values increasing
# downward and x increasing to the right. This might seem weird at first, but if you think about an image as a
# matrix, it makes sense that the "00" element is in the upper left.

# Definition of Cross Section: A cross section is the shape we get when cutting straight through an object.

# Quiz: We intend to find edges where pixels are changing rapidly when taking cross sections.

