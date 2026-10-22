#!/bin/bash

file="/Users/santosg/Hiram_datos/IMG_1952.MOV"

ffmpeg -i $file -t 30 -vf cropdetect -f null -

