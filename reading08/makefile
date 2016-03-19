all: reading08.pdf results.png

reading08.pdf:	reading08.tex results.png
	pdflatex reading08.tex
	pdflatex reading08.tex

results.png:	histogram.plt
	gnuplot ./histogram.plt

clean:
	rm -f reading08.pdf results.png reading08.aux reading08.log reading08.out