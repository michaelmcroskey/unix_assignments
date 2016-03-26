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


#
#for arg in sys.argv:
#	print arg

# fs = os.open("etc/passwd", os.O_RDONLY)
# os.read(fd, 10)
# os.close(3)
#
# os.lseek(fd, 0, os.SEEK_SET)

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

#try:                                
#	opts, args = getopt.getopt(sys.argv[1:],"h",["if=","of=","count=","bs=","seek=","skip="])
#	
#except getopt.GetoptError:
#	usage()                         
#	sys.exit(2)
#
#infile = 0
#outfile = 1
#count = sys.maxint
#bs = 512
#seek = None
#skip = None
#
for opt in sys.argv[1:]:
	opts = opt.split("=")
	for i in range(len(opts)):
		if opts[i] == 'if':
			infile = opts[i+1]
			source = open_fd(infile, os.O_RDONLY)
			i += 1

		elif opts[i] == 'of':
			outfile = opts[i+1]
			target = open_fd(outfile, os.O_CREAT|os.O_WRONLY)
			i += 1
			        
		elif opts[i] == 'count':
			count = opts[i+1]
			i += 1
			
		elif opts[i] == 'bs':
			bs = opts[i+1]
			i += 1
			
		elif opts[i] == 'seek':
			seek = opts[i+1]
			lseek_fd(infile, skip*bs, os.SEEK_SET)
			i += 1
			
		elif opts[i] == 'skip':
			skip = opts[i+1]
			lseek_fd(outfile, skip*bs, os.SEEK_SET)
			i += 1
			
		else :
			if not(i):
				usage()

	           
#for opt, arg in opts:
#	if opt == '--if':
#		infile = arg
#		source = open_fd(infile, os.O_RDONLY)
#		
#	if opt == '--of':
#		outfile = arg
#		target = open_fd(outfile, os.O_CREAT|os.O_WRONLY)
#		        
#	if opt == '--count':
#		count = arg
#		
#	if opt == '--bs':
#		bs = arg
#		
#	if opt == '--seek':
#		seek = arg
#		lseek_fd(infile, skip*bs, os.SEEK_SET)
#		
#	if opt == '--skip':
#		skip = arg
#		lseek_fd(outfile, skip*bs, os.SEEK_SET)
#	
#	if opt == '-h':
#		usage()
#
#data = read_fd(source, bs)
#n = 0
#while data:
#	if n == count:
#		break
#	write_fd(target, data)
#	data = read_fd(source, bs)
#	n += 1
#		
#close_fd(source)
#close_fd(target)
		