# Video Linear Image Generator

An open source image generator for video files, similar to [moviepalette](https://moviepalette.com/)

## Examples

### The Ring (2002)

![The Ring (2002)](https://raw.githubusercontent.com/follower46/video_linear_image/main/examples/The%20Ring.mkv.png)

### The Abyss (1989)

![The Abyss (1989)](https://raw.githubusercontent.com/follower46/video_linear_image/main/examples/The%20Abyss.mp4.png)

### Hero (2002)

![Hero (2002)](https://raw.githubusercontent.com/follower46/video_linear_image/main/examples/Hero.mp4.png)

### Curious George (2006)

![Curious George (2006)](https://raw.githubusercontent.com/follower46/video_linear_image/main/examples/Curious%20George.mkv.png)

### The Matrix (1999)

![The Matrix (1999)](https://raw.githubusercontent.com/follower46/video_linear_image/main/examples/The%20Matrix.mp4.png)

[See more examples here](https://github.com/follower46/video_linear_image/tree/main/examples)

## Requirements

* [Python 3.11+](https://www.python.org/downloads)
* Numpy
* opencv
* Pillow
* ColorThief-Py

## Install From Source

1. Download & extract the source
2. Change directory into *video_linear_image*
3. Run `pip install -r requirements.txt`

## Run

`python3 generator.py "Bullet Train.mkv"`

## Future Improvements

* Support adding post processing to the images (vibrance mode, vignette)
* Add option to trim out credits sequence in the image (the black bar on the far right side)
* Add option for pallets instead of a single color (maybe each strip is a gradient)
* Add option for a "series" instead of a single movie (for TV shows or sequels)
