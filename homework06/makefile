all: homework06.pdf sex.png race.png

homework06.pdf:	homework06.tex sex.png race.png
	pdflatex homework06.tex
	pdflatex homework06.tex

sex.png:	plot.plt
	gnuplot ./plot.plt
	
race.png:	plot.plt
	gnuplot ./plot.plt

clean:
	rm -f homework06.pdf homework06.aux homework06.log homework06.out sex.png race.png