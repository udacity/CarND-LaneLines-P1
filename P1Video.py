# Import everything needed to edit/save/watch video clips
from moviepy.editor import VideoFileClip
from IPython.display import HTML
from P1 import *
import sys

def process_image(image):
    # NOTE: The output you return should be a color image (3 channel) for processing video below
    # TODO: put your pipeline here,
    # you should return the final output (image with lines are drawn on lanes)
    result = FindingLanes(image)
    return result

if __name__ == "__main__":

    if(len(sys.argv) < 3):
        print("Usage: ./P1Video.py <input_file> <output_file>\n")
        sys.exit(1)

    input = sys.argv[1]
    output = sys.argv[2]
    clip2 = VideoFileClip(input)
    output_clip = clip2.fl_image(process_image)
    output_clip.write_videofile(output, audio=False)