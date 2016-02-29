#!/bin/sh

# broify.sh

var=0
DELIM=#

usage(){
	echo;
	echo "usage: broify.sh
	  -d DELIM    Use this as the comment delimiter.
	  -W          Don't strip empty lines."
	echo;
}


while getopts d:W flag; do
	case $flag in
	# no comments
	d)
		DELIM=$OPTARG
		;;
	# keep blank lines, remove tabs
	W)
		var=1
		;;
	*)
		usage
		;;
	esac
	
done

# -W flag
if [[ $var -eq 1 ]]; then
	sed -r "s|$DELIM.*||g" |
	sed -r 's|[ \t]*$||g'
	
elif [[ $var -eq 0 ]]; then
	sed -r "s|$DELIM.*||g" |
	sed -r 's|[ \t]*$||g' |
	sed -r '/^\s*$/d'
fi