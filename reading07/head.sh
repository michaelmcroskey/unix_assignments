#!/bin/sh

usage(){
	echo "usage: head.sh
	
	      -n N    Display the first N lines"
}

while getopts n:h flag; do
	case $flag in
	n)
		lines=$OPTARG
		;;
	h)
		usage
		;;
	*)
		usage
		;;
	esac
done

shift $(($OPTIND -1))

if [[ lines -eq 0 ]]; then
	lines=10
fi

awk $lines $1