#!/bin/bash

# Body is pure markdown, which PanDoc converts to corresponding Beamer

if [ $# -ne 3 ]; then
  echo "usage:   ${0##*/} <source-directory> <filename> <dest-directory>"
  echo "example: ${0##*/} . Intro-To-HARK ../../../Intro-To-HARK-Custom"
  exit 1
fi

dirGet=$1
dirGetFull="$(realpath "$1")"
file=$2
dirPut=$3
dirPutFull="$(realpath "$3")"

echo "$(realpath "$0")" $dirGetFull $file $dirPutFull
echo dirPut=$dirPut
echo dirPutFull=$dirPutFull
cd $dirGetFull
echo mkdir -p "$(realpath "$dirPutFull")"

mkdir -p "$(realpath "$dirPutFull")"

if [ -e $file-NextSteps-body-Beamer-Include.tex ]; then 
    pandoc --to=beamer --output=$file-NextSteps-body-Beamer-Include.tex $dirGet/$file-NextSteps-body.md
fi

pwd

# Make handout version
rpl '%%\documentclass[handout]{beamer}' '\documentclass[handout]{beamer}' $file.tex
rpl '%\documentclass[handout]{beamer}' '\documentclass[handout]{beamer}' $file.tex
rpl '\documentclass[public]{beamer}' '%\documentclass[public]{beamer}' $file.tex

pdflatex $dirGet/$file.tex
bibtex   $dirGet/$file.tex
pdflatex $dirGet/$file.tex
pdflatex $dirGet/$file.tex

mv $dirGet/$file.pdf $dirPut/$file-PrintMe.pdf 
cp $dirGet/$file-PrintMe.pdf $dirPut/PARK

rpl '%%\documentclass[public]{beamer}' '\documentclass[public]{beamer}' $file.tex
rpl '%\documentclass[public]{beamer}' '\documentclass[public]{beamer}' $file.tex
rpl '\documentclass[handout]{beamer}' '%\documentclass[handout]{beamer}' $file.tex


pdflatex $dirGet/$file.tex
bibtex   $dirGet/$file.tex
pdflatex $dirGet/$file.tex
pdflatex $dirGet/$file.tex

mv $dirGet/$file.pdf $dirPut/$file-ViewMe.pdf 
cp $dirGet/$file-ViewMe.pdf $dirPut/PARK

#Intro-To-HARK_2017-12_NextSteps_RBA-Workshop_body-Beamer-Include.tex 

