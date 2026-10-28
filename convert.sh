#!/bin/bash

pat="../Hiram_datos"

file1="IMG_1952.MOV"

file2="IMG_1958.MOV"

#mkdir temporal


#ffmpeg -i $pat/$file1 -vf fps=1 output_%05d.jpg

ffmpeg -i $1 temporal/output_%05d.jpg

