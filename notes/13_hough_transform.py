# URL: https://classroom.udacity.com/nanodegrees/nd013/parts/fbf77062-5703-404e-b60c-95b78b2f3f9e/modules/83ec35ee-1e02-48a5-bdb7-d244bd47c2dc/lessons/8c82408b-a217-4d09-b81d-1bda4c6380ef/concepts/a21e50a1-bf49-4ec4-ab1d-5b25d0aa4428
#
# Using the Hough Transform to Find Lines from Canny Edges
#
# Hough is pronounced "Huff", like "tough" is pronounced "tuff"
#
# In image space, a line is plotted as x vs. y, but in 1962, Paul Hough devised a method for representing lines in
# parameter space, which we will call “Hough space” in his honor.
#
# In Hough space, I can represent my "x vs. y" line as a point in "m vs. b" instead. The Hough Transform is just the
# conversion from image space to Hough space. So, the characterization of a line in image space will be a single point
# at the position (m, b) in Hough space.
#
# So now I’d like to check your intuition… if a line in image space corresponds to a point in Hough space, what would
# two parallel lines in image space correspond to in Hough space?
#
# Question 1 of 5
#
# Q: What will be the representation in Hough space of two parallel lines in image space?
# A: C
#
# Explanation:
#
#           That's right! Parallel lines have the same slope, which is to say, the same “m” parameter in our line model.
#           So, in parameter space, two parallel lines would be represented by two points at the same m value, but
#           different b values.
#
#
#
#
#
# Alright, so a line in image space corresponds to a point in Hough space. What does a point in image space correspond
# to in Hough space?
#
# A single point in image space has many possible lines that pass through it, but not just any lines, only those with
# particular combinations of the m and b parameters. Rearranging the equation of a line, we find that a
# single point (x,y) corresponds to the line b = y - xm.
#
# So what is the representation of a point in image space in Hough space?
#
# Question 2 of 5
#
# Q: What does a point in image space correspond to in Hough space?
# A: A
#
# Explanation:
#
#           That's right! A point in image space describes a line in Hough space. So a line in an image is a point in
#           Hough space and a point in an image is a line in Hough space… cool!
#
#
#
#
# What if you have 2 points in image space. What would that look like in Hough space?
#
# Question 3 of 5
#
# Q: What is the representation in Hough space of two points in image space?
# A: C
#
# Explanation:
#
#           That's correct! Two points in image space correspond to two lines in Hough Space. Not only that, but these
#           lines must intersect… why?
#
#
#
#
# Alright, now we have two intersecting lines in Hough Space. How would you represent their intersection at the
# point (m0, b0) in image space?
#
#
# Question 4 of 5
#
# Q: What does the intersection point of the two lines in Hough space correspond to in image space?
# A: A) A line in image space that passes through both (x1,y1) and x2,y2)
#
# Explanation:
#
#           That's right! The intersection point at (m0, b0) represents the line y = m0x + b0 in image space and it
#           must be the line that passes through both points!
#
#
#
#
#   So this is how we’re going to find lines!
#
#   Suppose I’ve run my Canny Edge Detection Algorithm to find all points associated with edges in an image.
#
#   I can then consider every point in this edge detected image as a line in Hough space. And where many lines in Hough
#   space intersect, I declare I have found a line in image space!
#
#   The strategy here is to divide up our Hough space into a grid, and define intersecting lines as all lines passing
#   through a given grid cell.
#
#   We have a problem though… vertical lines have infinite slope in (m, b) representation, in which case we need a new
#   parameterization (i.e. a new set of coordinates). So, let’s redefine our line in polar coordinates, where we use
#   angle (Θ) and distance (ρ) from the origin to define lines. (FYI: Θ is the Greek letter theta and ρ is the Greek
#   letter rho.)
#
#   With polar coordinates, each point in image space now corresponds to a sine curve in Hough space.
#
#   So, if we translate many points from image space to polar coordinate Hough space, we'll find many sine curves. The
#   intersection of those sine curves in (Θ, ρ) Hough space gives the parameterization of a line, just like the
#   intersection of straight lines in (m, b) Hough space gave us the parameterization of a line.
#
#   Q: What happens if we run a Hough Transform on an image of a square? What will the corresponding plot in Hough
#   space look like?
#
#
#   A: That's right! The four major intersections between curves in Hough space correspond to the four sides
#      of the square.
#
#
#
#   Conclusion:
#
#       Now you know how the Hough Transform works, but to accomplish the task of finding lane lines, we need to
#       specify some parameters to say what kind of lines we want to detect (i.e., long lines, short lines, bendy
#       lines, dashed lines, etc.). To do this, we'll be using an OpenCV function called HoughLinesP that takes
#       several parameters.
#
#
#
# NOTE: I got all quiz questions correct on the first attempt. I took my time to understand each phase and it really
#       helped me grasp the concepts to the point I was confident to move on to the next section.
