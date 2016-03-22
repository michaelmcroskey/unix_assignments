#!/usr/bin/env python2.7

import getopt
import os
import sys
from sets import Set

# Global Variable

FIELDS = []
DELIM = '\t'
DFLAG = False
FFLAG = False

# Usage function

def usage(status=0):
    print '''usage: wc.py [-d DELIM -f] files ...

    -d DELIM  use DELIM instead of TAB for field delimiter
    -f FIELDS select only these FIELDS'''.format(os.path.basename(sys.argv[0]))
    sys.exit(status)

# Parse command line options

try:
    opts, args = getopt.getopt(sys.argv[1:], "hd:f:")
except getopt.GetoptError as e:
    print e
    usage(1)

for o, a in opts:
		if o == '-f':
				FFLAG = True
				FIELDS = a.split(',')
		elif o == '-d':
				DFLAG = True
				DELIM = a
		else:
				usage(1)

if FFLAG == False:
		print 'Error: please name a field flag.'
		usage(1)
		sys.exit()

if len(args) == 0:
		args.append('x')

# Main execution

for path in args:
	if path == '-':  
		stream = sys.stdin 
		start = 0
		list = []
		size = 0
		for line in stream:
			list.append(line.strip('\n').split(DELIM))
		for line in range(len(list)):
			for y in FIELDS:
				i = int(y)
				size = len(list[line])
				if i > size and size == 1:
						i = len(list[line])
				elif i > size:
						print '\n',
						continue
				number = list[line][i-1]
				print number

				
	elif path == 'x':
		stream = sys.stdin 
		start = 0
		list = []
		size = 0
		for line in stream:
			list.append(line.strip('\n').split(DELIM))
		for line in range(len(list)):
			for y in FIELDS:
				i = int(y)
				size = len(list[line])
				if i > size and size == 1:
						i = len(list[line])
				elif i > size:
						print '\n',
						continue
				number = list[line][i-1]
				print number

	else:
		stream = open(path)
		start = 0
		list = []
		size = 0
		for line in stream:
			list.append(line.strip('\n').split(DELIM))
		stream = open(path)
		for line in range(len(list)):
			for y in FIELDS:
				i = int(y)
				size = len(list[line])
				if i > size and size == 1:
						i = len(list[line])
				elif i > size:
						print '\n',
						continue
				number = list[line][i-1]
				print number
		
	stream.close()