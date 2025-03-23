#!/bin/bash

# Body is pure markdown, which PanDoc converts to corresponding Beamer

pandoc --to=beamer --output=Intro-To-ARK_2017-12_NextSteps_RBA-Workshop_body-Beamer-Include.tex ./Intro-To-ARK_2017-12_NextSteps_RBA-Workshop_body.md 

