#!/bin/bash

# Body is pure markdown, which PanDoc converts to corresponding Beamer

file=Intro-To-ARK_2018-03-30_GMU

pandoc --to=beamer --output=$file_NextSteps_body-Beamer-Include.tex ./$file_NextSteps_body.md 

# Make handout version
rpl '%%\documentclass[handout]{beamer}' '\documentclass[handout]{beamer}' $file.tex
rpl '%\documentclass[handout]{beamer}' '\documentclass[handout]{beamer}' $file.tex
rpl '\documentclass[public]{beamer}' '%\documentclass[public]{beamer}' $file.tex

pdflatex ./$file.tex
bibtex   ./$file.tex
pdflatex ./$file.tex
pdflatex ./$file.tex

mv ./$file.pdf ./$file-Version-For-Presenting.pdf 
cp ./$file-Version-For-Presenting.pdf ./PARK

rpl '%%\documentclass[public]{beamer}' '\documentclass[public]{beamer}' $file.tex
rpl '%\documentclass[public]{beamer}' '\documentclass[public]{beamer}' $file.tex
rpl '\documentclass[handout]{beamer}' '%\documentclass[handout]{beamer}' $file.tex


pdflatex ./$file.tex
bibtex   ./$file.tex
pdflatex ./$file.tex
pdflatex ./$file.tex

mv ./$file.pdf ./$file-Version-For-Printing.pdf 
cp ./$file-Version-For-Printing.pdf ./PARK

#Intro-To-ARK_2017-12_NextSteps_RBA-Workshop_body-Beamer-Include.tex 

