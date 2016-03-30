#!/bin/bash

DDOUT=/tmp/dd.$(id -u).$$

trap "rm -f $DDOUT.*" EXIT INT TERM

if ! diff -u <(cat /etc/passwd | dd 2> /dev/null) \
             <(cat /etc/passwd | ./dd.py); then
    echo "dd no arguments test failed!"
    exit 1
fi

if ! diff -u <(dd if=/etc/passwd 2> /dev/null) \
             <(./dd.py if=/etc/passwd); then
    echo "dd if= test failed!"
    exit 1
fi

dd if=/etc/passwd of=$DDOUT.0 2> /dev/null
./dd.py if=/etc/passwd of=$DDOUT.1
if ! diff -u $DDOUT.0 $DDOUT.1; then
    echo "dd of= test failed!"
    exit 1
fi

if ! diff -u <(dd if=/etc/passwd bs=2 2> /dev/null) \
             <(./dd.py if=/etc/passwd bs=2); then
    echo "dd bs= test failed!"
    exit 1
fi

if ! diff -u <(dd if=/etc/passwd bs=2 count=5 2> /dev/null) \
             <(./dd.py if=/etc/passwd bs=2 count=5); then
    echo "dd count= test failed!"
    exit 1
fi

dd if=/etc/passwd of=$DDOUT.0 bs=2 count=5 seek=1 conv=notrunc 2> /dev/null
./dd.py if=/etc/passwd of=$DDOUT.1 bs=2 count=5 seek=1
if ! diff -u $DDOUT.0 $DDOUT.1; then
    echo "dd seek= test failed!"
    exit 1
fi

if ! diff -u <(dd if=/etc/passwd bs=2 count=5 skip=1 2> /dev/null) \
             <(./dd.py if=/etc/passwd bs=2 count=5 skip=1); then
    echo "dd skip= test failed!"
    exit 1
fi

echo "dd test successful!"
