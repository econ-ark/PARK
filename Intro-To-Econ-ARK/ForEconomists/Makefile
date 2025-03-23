
PACKAGE=cfpbpresentation

SAMPLES = sample-pdflatex.tex sample-xelatex.tex sample-lualatex.tex
#SAMPLES = sample-pdflatex.tex 

WD = $(shell pwd)
CURRDIR = $(notdir ${WD})



PDF = $(PACKAGE).pdf ${SAMPLES:%.tex=%.pdf}


all:  ${PDF}  ${HTML}

sample-%.tex: sample.tex
	ln -s $< $@


%.pdf:  %.dtx   $(PACKAGE).cls ${PDFIMAGES}
	pdflatex $<
	- bibtex $*
	pdflatex $<
	- makeindex -s gind.ist -o $*.ind $*.idx
	- makeindex -s gglo.ist -o $*.gls $*.glo
	pdflatex $<
	while ( grep -q '^LaTeX Warning: Label(s) may have changed' $*.log) \
	do pdflatex $<; done


%.cls:   %.ins %.dtx  
	pdflatex $<

sample-%.pdf:  sample-%.tex   $(PACKAGE).cls
	$* sample-$*
	- bibtex sample-$*
	$* sample-$*
	$* sample-$*
	while ( grep -q '^LaTeX Warning: Label(s) may have changed' sample-$*.log) \
	do $* sample-$*; done



.PRECIOUS:  $(PACKAGE).cls $(PACKAGE).4ht

clean:
	$(RM)  *.log *.aux \
	*.glo *.idx *.toc *.tbc *.lom *.loc \
	*.ilg *.ind *.out *.lof *.hd \
	*.lot *.bbl *.blg *.gls $(PACKAGE).sty *.ist \
	*.dvi *.ps *.thm *.tgz *.zip \
	sample-*tex.tex  *.nav *.snm \
	*.4ct *.4tc *.lg *.idv *.tmp *.xref *.4ht 

distclean: clean
	$(RM) $(PDF) 

#
# Archive for the distribution. Includes typeset documentation
#
archive:  all clean
	cd ..; \
	tar -czvf $(PACKAGE).tgz  --exclude 'debug*' \
	--exclude '*~' --exclude '*.tgz' --exclude '*.zip'  \
	--exclude CVS $(CURRDIR); \
	mv $(PACKAGE).tgz $(CURRDIR); \
	cd $(CURRDIR)


zip:  all clean
	cd ..; \
	zip -r  $(PACKAGE).zip $(CURRDIR) \
	-x 'debug*' -x '*~' -x '*.tgz' -x '*.zip' -x CVS -x '*/CVS/*'; \
	mv $(PACKAGE).zip $(CURRDIR); \
	cd $(CURRDIR)
