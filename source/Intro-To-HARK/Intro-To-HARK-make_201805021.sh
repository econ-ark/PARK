#!/bin/bash
# Compile and post to PARK

cd ./Latest
pdflatex Intro-To-HARK
bibtex   Intro-To-HARK
pdflatex Intro-To-HARK
pdflatex Intro-To-HARK

cp Intro-To-HARK.pdf ../../../PARK/Intro-To-HARK.pdf

