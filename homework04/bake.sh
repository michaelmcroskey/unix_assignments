#!/bin/sh

: ${CC:="gcc"}
: ${CFLAGS:="-std=gnu99 -Wall"}
: ${SUFFIXES:=".c"}
: ${VERBOSE:=0}

for i in *$SUFFIXES
do
   	echo $i
	if [ $VERBOSE -ne 0 ]; then 
		echo $CC $CFLAGS $i -o `basename $i $SUFFIXES` -v
	fi
	$CC $CFLAGS $i -o `basename $i $SUFFIXES` || exit 1
done

`basename $i $SUFFIXES`