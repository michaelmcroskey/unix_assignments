#!/bin/sh

# usage: reddit.sh [options] subreddits...
# 	-r      Shuffle the links
#	-s      Sort the links
#	-n N    Number of links to display (default is 10)

usage(){
	echo;
	echo "usage: reddit.sh [options] subreddits...
	    -r      Shuffle the links
	    -s      Sort the links
	    -n N    Number of links to display (default is 10)"
	echo;
}

# n takes in a flag (:)
while getopts rsn: option; do
	case $option in
	n)
		n=$OPTARG
		;;
	# Shuffles the links
	r)
		var=1
		;;
	s)
		var=2
		;;
	*)
		usage
		;;
	esac
done

# Shifts options
shift $(($OPTIND -1))
term=$1

search(){
	curl -s http://www.reddit.com/r/$term/.json |
	python -m json.tool |
	grep "url" |
	cut -d '"' -f 4 |
	grep "http" 
}

# Shuffle (-r)
if [[ $var -eq 1 ]]; then
	search | shuf | head -n ${n:=10}

# Sort (-s)
elif [[ $var -eq 2 ]]; then
	search | sort | head -n ${n:=10}
	
# None
elif [[ $var -eq 0 ]]; then
	search | head -n ${n:=10}
fi