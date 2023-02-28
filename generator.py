import sys
import cv2
import numpy as np
import os
import shutil

from colorthief import ColorThief

from PIL import Image, ImageDraw, ImageEnhance

#IMAGE_RESOLUTION = (1920,1080) # HD
IMAGE_RESOLUTION = (3440,1440) # UWQHD
#IMAGE_RESOLUTION = (3440,3440) # For Printing At CVS

NUMBER_OF_LINES = 512
WORK_LOCATION = "temp"

def extract_video_samples(video_filename, extraction_location):
    if not os.path.isdir(extraction_location):
        os.mkdir(extraction_location)
    
    capture = cv2.VideoCapture(video_filename)
    fps = capture.get(cv2.CAP_PROP_FPS)
    frame_count = int(capture.get(cv2.CAP_PROP_FRAME_COUNT))
    duration = frame_count/fps

    frames_indices = list(range(1, frame_count, int(frame_count/NUMBER_OF_LINES)))

    # walk through frames by the number of vertical lines we want
    frame_number = 0
    capture_number = 0
    while True:
        is_read, frame = capture.read()
        if not is_read:
            # end of video file
            break
        
        if not len(frames_indices):
            # no more frames to grab
            break
        
        current_frame_index = frames_indices[0]

        if frame_number >= current_frame_index:
            print(f"writing frame{capture_number}.jpg")
            cv2.imwrite(os.path.join(extraction_location, f"frame{capture_number}.jpg"), frame)
            capture_number += 1
            frames_indices.pop(0)

        frame_number += 1

def get_linear_colors(extraction_location):
    colors = []
    for capture_number in range(NUMBER_OF_LINES+1):
        filename = os.path.join(extraction_location, f"frame{capture_number}.jpg")
        if not os.path.isfile(filename):
            continue
        print(f"sniffing {filename}")
        colors.append(
            ColorThief(filename).get_color(quality=1)
        )
        os.remove(filename)
    
    hex_colors = []
    for color in colors:
        red, green, blue = color
        hex_colors.append('#{:02x}{:02x}{:02x}'.format(red, green, blue))
    return hex_colors

def same_image(file_name, vertial_strips):
    img = Image.new("RGB", (IMAGE_RESOLUTION[0], IMAGE_RESOLUTION[1]))
    
    rectangle_object = (IMAGE_RESOLUTION[0]/NUMBER_OF_LINES, IMAGE_RESOLUTION[1])
    x_location = 0
    for color in vertial_strips:
        print(f"painting {color}")
        vertical_strip = ImageDraw.Draw(img)
        vertical_strip.rectangle(
            [
                (x_location, 0),
                (x_location + rectangle_object[0], rectangle_object[1])
            ],
            fill=color
        )
        x_location += rectangle_object[0]
    img.save(file_name)

def make_colors_pop(image_location, new_location):
    img = Image.open(image_location)
    img = ImageEnhance.Brightness(img).enhance(1.2)
    img = ImageEnhance.Contrast(img).enhance(1.2)
    img = ImageEnhance.Color(img).enhance(1.2)
    img.save(new_location)



if __name__ == '__main__':
    if len(sys.argv) > 2:
        print("Please supply a video file for processing")
        exit(1)
    
    video_location = sys.argv[1]
    base_name = os.path.basename(video_location)

    extract_video_samples(video_location, WORK_LOCATION)
    colors = get_linear_colors(WORK_LOCATION)
    same_image(f"{base_name}.png", colors)
    make_colors_pop(f"{base_name}.png", f"{base_name}-pop.png")
