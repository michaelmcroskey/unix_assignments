#!/bin/sh

usage(){
	echo "usage: disk_usage.sh [-a -n N] directory"
}

while getopts an: OPTION; do
	
	case $OPTION in
	n)
		x=$OPTARG
		;;
	a)
		y=1
		;;
	*)
		usage
		;;
	esac
	
done

shift $(($OPTIND -1))

directory=$1

if [[ ! -z $y ]]; then
	add='-a'
fi

du $add -h $directory 2> /dev/null | sort -h -r | head -n ${x:=10}

