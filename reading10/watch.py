#!/usr/bin/env python2.7

import getopt, os, sys, tempfile, time

# Global Variables
PROGRAM_NAME = os.path.basename(sys.argv[0])
INTERVAL = float(2)

# Functions
def error(message, status=1):
    print >>sys.stderr, message
    sys.exit(status)

def usage(status=0):
    error('''Usage: watch.py [-n INTERVAL] COMMAND

opts:

    -n INTERVAL   Specify update INTERVAL (in seconds)
'''
    .format(PROGRAM_NAME), status)

# Parse the command line arguments
try:
    opts, args = getopt.getopt(sys.argv[1:], "hn:")
except getopt.GetoptError as e:
    error(e)

for opt, val in opts:
	if opt == '-h':
		usage(0)
	elif opt == '-n':
		INTERVAL = float(val)
	else:
		usage(1)

COMMAND = ''.join(args)
go = True

# Main Execution
try:
	while go:
		os.system('clear')
		print "Every", INTERVAL, "s: ", COMMAND
		try:
			os.system(COMMAND) # Calls the COMMAND you want
		except OSError:
			go = False
			break
			sys.exit(0)
			exit()
		time.sleep(INTERVAL)
# Avoid Command-C
except KeyboardInterrupt:
	print "\n"
	sys.exit(0)

