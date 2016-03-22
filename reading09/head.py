#!/usr/bin/env python2.7

import getopt
import os
import sys

# Global Variable
N = False

# Usage function
def usage(status=0):
    print '''usage: head.py [-n NUM] files ...

    -n NUM  print the first NUM lines instead of the first 10'''.format(os.path.basename(sys.argv[0]))
    sys.exit(status)

# Parse command line options

try:
    opts, args = getopt.getopt(sys.argv[1:], "hn:")
except getopt.GetoptError as e:
    print e
    usage(1)

for o, a in opts:
    if o == '-n':
		lines = a
		N = True
    else:
        usage(1)

if len(args) == 0:
    args.append('-')

# Main execution

for path in args:
	if path == '-':
		stream = sys.stdin
	else :
		stream = open(path)
	display = 0
	
	if N == True:
	    for line in stream:
			display += 1
			if display == int(lines) + 1:
				sys.exit()
			else :
				print line,
	else :
		for line in stream:
			display += 1

			if display == 11:
			    sys.exit()
			else :
			    print line,

		stream.close()
