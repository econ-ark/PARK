#!/bin/bash

cd ./WhyPython

cd ./Latest
pdflatex WhyPython
bibtex   WhyPython
pdflatex WhyPython
pdflatex WhyPython

cp WhyPython.pdf ./PARK

