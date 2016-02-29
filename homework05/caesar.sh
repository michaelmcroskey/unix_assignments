#!/bin/sh
# usage: caesar.sh [rotation]
# This program will read from stdin and rotate (shift right) the text by
# the specified rotation.  If none is specified, then the default value is 13

usage(){
	echo;
	echo "usage: caesar.sh [rotation]
	This program will read from stdin and rotate (shift right) the text by
	the specified rotation.  If none is specified, then the default value is 13."
	echo;
}

# For help usage
while getopts 'h' option; do
	case $option in
		h)
			usage
			exit
			;;
		*)
			usage
			;;
	esac
done

# Default case cipher is 13
if [ $# -eq 0 ]
  then
    CIPHER=13;
	else
	CIPHER=$1;	
fi

if [ $1 -gt 26 ]
	then 
	CIPHER=$( expr $1 % 26);
fi


# Create alpha strings
export LOWCASE=$(echo {a..z} | sed -r 's/ //g';); 
export UPCASE=$(echo {A..Z} | sed -r 's/ //g';); 

# Remove characters up to $CIPHER and append
export C=$(echo $LOWCASE | sed -r "s/^.{$CIPHER}//g")$(echo $LOWCASE | sed -r "s/.{$( expr 26 - $CIPHER )}$//g";);
export D=$(echo $UPCASE | sed -r "s/^.{$CIPHER}//g")$(echo $UPCASE | sed -r "s/.{$( expr 26 - $CIPHER )}$//g";);

# Replace characters
tr $LOWCASE $C | tr $UPCASE $D;
