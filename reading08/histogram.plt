# gnuplot ./histogram.plt

set output 'results.png'
set terminal png
set grid
set origin 0,0
set boxwidth .9 relative
set style data histograms
set style fill solid 1.0
set xrange [0:7]
set yrange [0:200]

plot 'results.dat' using 1:2 with boxes lc rgb "red"