# gnuplot ./data.plt

set output 'race.png'
set terminal png
set grid
set boxwidth .9 relative
set title "CSE Ethnicities at ND ('13-'18)"
set xlabel "Graduation Year"
set ylabel "Percentage of Students"
set xrange [2013:2018]
set yrange [0:100]
set ytics "20"
set datafile separator ","
plot "data.csv" using 1:4 title 'Caucasian' with lines, \
     "data.csv" using 1:5 title 'Oriental' with lines, \
	 "data.csv" using 1:6 title 'Hispanic' with lines, \
	 "data.csv" using 1:7 title 'African American' with lines, \
	 "data.csv" using 1:8 title 'Native American' with lines, \
	 "data.csv" using 1:9 title 'Multiple Selection' with lines, \
	 "data.csv" using 1:10 title 'Undeclared' with lines

set output 'sex.png'
set terminal png
set grid
set boxwidth .9 relative
set title "CSE Genders at ND ('13-'18)"
set xlabel "Graduation Year"
set ylabel "Percentage of Students"
set xrange [2013:2018]
set yrange [0:100]
set ytics "10"
set datafile separator ","
plot "data.csv" using 1:2 title 'Male' with lines, \
     "data.csv" using 1:3 title 'Female' with lines
	