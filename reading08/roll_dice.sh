#!/bin/sh

usage(){
	echo "usage: roll_dice.sh [-r ROLLS -s sides]

	    -r ROLLS        Number of rolls of die (default: 10)
	    -s SIDES        Number of sides on die (default: 6)"
}

while getopts r:s:h option; do	
	case $option in
	r)	ROLLS=$OPTARG;;
	s)	SIDES=$OPTARG;;
	h)	usage
		exit 1;;
	*)	echo "Invalid Option" 
		usage
		exit 1;;
	esac
done

for ((i=1; i <= ${ROLLS:=10}; i++)); do
	shuf -i 1-${SIDES:=6} -n 1
done
