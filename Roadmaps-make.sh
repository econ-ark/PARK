#!/bin/bash
# Copy Roadmap content to PARK

mkdir -p ../PARK/Roadmaps/HARK
cd ../PARK

for f in Intro-To-HARK.tex Intro-To-HARK-From.tex Roadmap_Notes*; do
    git set 
for f in Tools.pdf; do
    cp -r ./Roadmaps/HARK/$f ../PARK/Roadmaps/HARK/
    git add -f Tools.pdf 
done
done


git commit -m 'Update PARK/Roadmap/HARK/Tools.pdf'

