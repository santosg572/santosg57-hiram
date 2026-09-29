#!/bin/bash

ffmpeg -i $1 -vf fps=1 output_%05d.jpg

