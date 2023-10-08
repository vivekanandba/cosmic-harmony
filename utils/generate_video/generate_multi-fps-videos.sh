#!/usr/bin/env bash

python generate_images.py

# iterate through a list of fps values
for fps in 1 2 3 4 5 6 7 8 9 10
do
    python generate_video.py --fps $fps
done
