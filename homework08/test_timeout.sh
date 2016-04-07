#!/bin/sh

# Executability
if ! [[ -x timeout.py ]]; then
	echo "File can't be executed"
	exit 1
fi

# She-bang
shebang="#!/usr/bin/env python2.7"
line=$(head -n 1 timeout.py)
if [ "$line" != "$shebang" ]; then
	echo "Shebang incorrect"
	exit 1
fi

# Verify that timeout.py prints something reasonable to STDERR when the -h flag is set.
if [ $(./timeout.py -h |& wc -l) -eq 0 ]; then
	echo "./timeout.py: there is nothing for -h"
	exit 1
fi


# Verify that timeout.py exits with success when executing: ./timeout.py -t 5 sleep N
for N in 1 2 3 4
do
	./timeout.py -t 5 sleep $N
	if [ $(echo $?) -ne 0 ]; then
		echo "./timeout.py -t 5 sleep $N failed."
		exit 1
	fi
done

# Verify that timeout.py exits with failure when executing: ./timeout.py -t 1 sleep N
for N in 2 3 4 5
do
	./timeout.py -t 1 sleep $N
	if [ $(echo $?) -eq 0 ]; then
		echo "./timeout.py -t 1 sleep $N didn't fail."
		exit 1
	fi
done

# Verify that timeout.py prints something reasonable to STDERR when the -v flag is set.
if [ $(./timeout.py -v -t 1 sleep 2 |& wc -l)  -eq 0 ]; then
	echo "./timeout.py STDERR isn't understandable with -v."
	exit 1
fi

echo "./timeout.py test successful!"

