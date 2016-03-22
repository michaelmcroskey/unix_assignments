#!/usr/bin/env python2.7

import getopt
import os
import sys

# Global Variable

WORD = False
INPUT = 0
CHAR = False
LINE = False

# Usage function

def usage(status=0):
    print '''usage: wc.py [-c -l -w] files ...

    -c      print the byte/character counts
    -l      print the newline counts
    -w      print the word counts'''.format(os.path.basename(sys.argv[0]))
    sys.exit(status)

# Parse command line options

try:
    opts, args = getopt.getopt(sys.argv[1:], "hclw")
except getopt.GetoptError as e:
    print e
    usage(1)


for o, a in opts:
	if o == '-c':
		CHAR = True
		INPUT = 1
	elif o == '-l':
		LINE = True
		INPUT = 2
	elif o == '-w':
		WORD = True
		INPUT = 3
	else:
		usage(1)
				
if CHAR == False and LINE == False and WORD == False:
	print 'Error: please add a flag.'
	usage(1)
	sys.exit(1)

if len(args) == 0:
	args.append('x')

# Main execution

for path in args:
	if path == 'x':
		stream = sys.stdin 
		if CHAR == True and INPUT == 1: 
			x = 0
			for line in stream:
				x += sum(c != ' ' for c in line) + sum(c == ' ' for c in line)
			print x
		
		elif LINE == True and INPUT == 2:
			x = 0
			for line in stream:
				x += len(line.splitlines())
			print x

		elif WORD == True and INPUT == 3:
			x = 0
			for line in stream:
				x += len(line.split())
			print x


	elif path == '-':
		stream = sys.stdin 
		if CHAR == True and INPUT == 1: 
			x = 0
			for line in stream:
				x += sum(c != ' ' for c in line) + sum(c == ' ' for c in line)
			print x, path
		
		elif LINE == True and INPUT == 2:
			x = 0
			for line in stream:
				x += len(line.splitlines())
			print x, path

		elif WORD == True and INPUT == 3:
			x = 0
			for line in stream:
				x += len(line.split())
			print x, path

	else:
		stream = open(path)
		if CHAR == True and INPUT == 1: 
			x = 0
			for line in stream:
				x += sum(c != ' ' for c in line) + sum(c == ' ' for c in line)
			print x, path
		
		elif LINE == True and INPUT == 2:
			x = 0
			for line in stream:
				x += 1
			print x, path

		elif WORD == True and INPUT == 3:
			x = 0
			for line in stream:
				x += len(line.split())
			print x, path


	stream.close()

