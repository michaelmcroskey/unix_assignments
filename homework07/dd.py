#!/usr/bin/env python2.7
# Michael McRoskey

import getopt, os, sys

def usage():
	print('''
Usage: dd.py options...

Options:

      if=FILE     Read from FILE instead of stdin
      of=FILE     Write to FILE instead of stdout

      count=N     Copy only N input blocks
      bs=BYTES    Read and write up to BYTES bytes at a time

      seek=N      Skip N obs-sized blocks at start of output
      skip=N      Skip N ibs-sized blocks at start of input
''')

def open_fd(path, mode):
	try:
		return os.open(path, mode)
	except OSError as e:
		print >> sys.stderr, 'Could not open file {}: {}'.format(path, e)
		sys.exit(1)
		
def close_fd(path):
	try:
		return os.close(path)
	except OSError as e:
		print >> sys.stderr, 'Could not close file {}: {}'.format(path, e)
		sys.exit(1)

def read_fd(path, mode):
	try:
		return os.read(path, mode)
	except OSError as e:
		print >> sys.stderr, 'Could not read file {}: {}'.format(path, e)
		sys.exit(1)

def write_fd(path, mode):
	try:
		return os.write(path, mode)
	except OSError as e:
		print >> sys.stderr, 'Could not write file {}: {}'.format(path, e)
		sys.exit(1)

def lseek_fd(path, pos, how):
	try:
		return os.lseek(path, pos, how)
	except OSError as e:
		print >> sys.stderr, 'Could not lseek file {}: {}'.format(path, e)
		sys.exit(1)

infile = 0
outfile = 1
count = sys.maxint
bs = 512
seek = None
skip = None
ofFlag = 0

for opt in sys.argv[1:]:
	opts = opt.split("=")
	for i in range(len(opts)):
		if opts[i] == 'if':
			infile = opts[i+1]
			i += 1

		elif opts[i] == 'of':
			outfile = opts[i+1]
			ofFlag = 1
			i += 1
			        
		elif opts[i] == 'count':
			count = int(opts[i+1])
			i += 1
			
		elif opts[i] == 'bs':
			bs = int(opts[i+1])
			i += 1
			
		elif opts[i] == 'seek':
			seek = int(opts[i+1])
			i += 1
			
		elif opts[i] == 'skip':
			skip = int(opts[i+1])
			i += 1
			
		else :
			if not(i):
				usage()
if infile:
	source = open_fd(infile, os.O_RDONLY)
else:
	source = 0
	
if ofFlag:
	target = open_fd(outfile, os.O_CREAT|os.O_WRONLY)
else:
	target = 1	

if skip:
	lseek_fd(source, skip*bs, os.SEEK_SET)
if seek:
	lseek_fd(target, seek*bs, os.SEEK_SET)

data = read_fd(source, bs)
n = 0

while data:
	if n == count:
		break
	write_fd(target, data)
	data = read_fd(source, bs)
	n += 1
		
close_fd(source)
close_fd(target)
		