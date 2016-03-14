#!/bin/sh

roll_dice.sh -r 1000 | awk '{a[$1]++} END {for (i in a) print i, a[i]}' | sort | awk '{print $1 "	" $2}' > results.dat