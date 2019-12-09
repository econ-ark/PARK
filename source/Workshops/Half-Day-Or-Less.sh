#!/bin/bash
# Put all the "Generic" workshops in the Workshops directory in PARK

scriptDir="$(dirname "$0")"
scriptName=$(basename -- "$0")
textDir="${scriptName%.*}"

cd $scriptDir/$textDir

for f in *Generic*.md; do
    mkdir -p ../../../PARK/Workshops/$textDir
    cp $f ../../../PARK/Workshops/$textDir/$f
done

echo "Now execute the following:"
echo "cd "$(realpath ../../../PARK) "; git fetch ; git add . ; git commit Update Half-Day-Or-Less presentations ; git push" 

