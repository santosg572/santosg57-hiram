#!/bin/bash

rm Rplots.pdf
Rscript $1
open Rplots.pdf

