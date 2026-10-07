#!/bin/bash

pat="../Hiram_datos"

file1="IMG_1952.MOV"

file2="IMG_1958.MOV"

mkdir temporal


#ffmpeg -i $pat/$file1 -vf fps=1 output_%04d.jpg

ffmpeg -i $pat/$file1 temporal/output_%04d.jpg

