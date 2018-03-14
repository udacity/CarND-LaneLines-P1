def lane_finding(image):
	
	gray = grayscale(image)

	# Define a kernel size and apply Gaussian smoothing
	kernel_size = 5
	blur_gray = gaussian_blur(gray, kernel_size)

	# Define our parameters for Canny and apply
	low_threshold = 50
	high_threshold = 150
	edges = canny(blur_gray, low_threshold, high_threshold)

	# This time we are defining a four sided polygon to mask
	vertices = np.array([[(0.52*image.shape[1], 0.60*image.shape[0]),(0.48*image.shape[1], 0.60*image.shape[0]), (0,image.shape[0]),(image.shape[1],image.shape[0])]], dtype=np.int32)
	masked_edges = region_of_interest(edges, vertices)

	# Define the Hough transform parameters
	# Make a blank the same size as our image to draw on
	rho = 1 # distance resolution in pixels of the Hough grid
	theta = np.pi/180 # angular resolution in radians of the Hough grid
	threshold = 35   # minimum number of votes (intersections in Hough grid cell)
	min_line_len = 5 #minimum number of pixels making up a line
	max_line_gap = 2    # maximum gap in pixels between connectable line segments

	# Run Hough on edge detected image
	# Output "lines" is an array containing endpoints of detected line segments
	lines = hough_lines(masked_edges, rho, theta, threshold, min_line_len, max_line_gap)

	# Draw the lines on the raw image
	line_image = np.copy(image)
	lines_edges = weighted_img(lines, line_image, α=0.8, β=1., γ=0.)
	
	return lines_edges