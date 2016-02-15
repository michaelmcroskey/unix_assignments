#!/bin/sh

cd $1

for i in $( ls )
	do
		if [ -h $i ]
			then
				echo $1/$i links to $(readlink -f $i)
		fi
	done