#!/bin/bash

PARK=$(realpath ../PARK)

for FAQdir in FAQ/*; do
    pwd
#    echo $FAQdir
    if [ -d $FAQdir ]; then
	mkdir -p $PARK/$FAQdir
	cp $FAQdir/*.md $PARK/$FAQdir/
    fi
done

