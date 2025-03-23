#!/bin/bash

# Body is pure markdown, which PanDoc converts to corresponding Beamer

if [ $# -ne 4 ]; then
  echo "usage:   ${0##*/} <source-directory> <filename> <dest-directory> <dest-branch>"
  echo "example: ${0##*/} . Intro-To-Econ-ARK ./PARK 2018-BoE"
  exit 1
fi

dirGet=$1
file=$2
dirPut=$3
branch=$4
scriptName="$(basename "$0")"
dirScript="$(dirname "$0$")"
# dirScript=/Volumes/Data/Code/ARK/PARKive/PARK-make/Intro-To-Econ-ARK/ForEconomists ; scriptName=Intro-To-Econ-ARK-make.sh ; cd $dirScript ; dirGet=. ; file=Intro-To-Econ-ARK ; dirPut=./PARK ;  branch=2018-BoE
dirGetFull="$(realpath "$dirGet")"
dirPutFull="$(realpath "$dirPut")"
cd $dirScript
echo  $dirScript/$scriptName $dirGetFull $file $dirPutFull $branch
echo dirPut=$dirPut
echo dirPutFull=$dirPutFull
cd $dirGetFull

echo mkdir -p "$(realpath "$dirPutFull")"
mkdir      -p "$(realpath "$dirPutFull")"

# Incorporate NextSteps if desired
if [ -e $file-NextSteps-body-Beamer-Include.tex ]; then 
    pandoc --to=beamer --output=$file-NextSteps-body-Beamer-Include.tex $dirGet/$file-NextSteps-body.md
fi

pwd

# Make handout version
rpl '%%\documentclass[handout]{beamer}' '\documentclass[handout]{beamer}' $file.tex
rpl '%\documentclass[handout]{beamer}' '\documentclass[handout]{beamer}' $file.tex
rpl '\documentclass[public]{beamer}' '%\documentclass[public]{beamer}' $file.tex

pdflatex $dirGetFull/$file.tex
bibtex   $dirGetFull/$file.tex
pdflatex $dirGetFull/$file.tex
pdflatex $dirGetFull/$file.tex

echo cd $dirPutFull
cd      $dirPutFull

mv $dirGetFull/$file.pdf $dirGetFull/$file-PrintMe.pdf
cd $dirPutFull
git checkout $branch
cp $dirGetFull/$file-PrintMe.pdf $dirPutFull
cd $dirGetFull

rpl '%%\documentclass[public]{beamer}' '\documentclass[public]{beamer}' $file.tex
rpl '%\documentclass[public]{beamer}' '\documentclass[public]{beamer}' $file.tex
rpl '\documentclass[handout]{beamer}' '%\documentclass[handout]{beamer}' $file.tex


pdflatex $dirGetFull/$file.tex
bibtex   $dirGetFull/$file.tex
pdflatex $dirGetFull/$file.tex
pdflatex $dirGetFull/$file.tex

mv $dirGetFull/$file.pdf $dirGetFull/$file-ViewMe.pdf
cd $dirPutFull
git checkout $branch
cp $dirGetFull/$file-ViewMe.pdf $dirPutFull

git add .
git commit -m "Modified $branch $file"
echo now do git push
echo git push 

#Intro-To-Econ-ARK_2017-12_NextSteps_RBA-Workshop_body-Beamer-Include.tex 

