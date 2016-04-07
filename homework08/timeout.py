#!/usr/bin/env python2.7

# ---------------- Import -------------------
import getopt
import os
import sys
import signal
import errno

# ----------- Global Variables --------------
seconds = 10
verbose = False

# --------------- Functions -----------------
def error(message, status=1):
    print >>sys.stderr, message
    sys.exit(status)

def usage(status=0):
    error('''Usage: timeout.py [-t seconds] command...
Options:
	-t seconds  Timeout duration before killing command (default is 10 seconds)
	-v          Display verbose debugging output
	'''
    .format('./timeout.py'), status)

def debug(message, *args):
	''' Verbose formatting '''
	if verbose == True:
		print >>sys.stderr, message.format(*args)
				
def handler(signum, frame):
	if verbose == True:
		debug('Alarm Triggered after {} seconds!', seconds)
		debug('Killing PID {}...', pid)
		os.kill(pid, signal.SIGTERM)
	else:
		os.kill(pid, signal.SIGTERM)
		sys.exit(1)

# --------------- Arguments -----------------
try:
	opts, arguments = getopt.getopt(sys.argv[1:], "t:vh")
except getopt.GetoptError as e:
	error(e)

for opt, val in opts:
	if opt == '-h':
		usage(0)
	elif opt == '-t':
		seconds = int(val) 
	elif opt == '-v':
		verbose = True
	else:
		usage(1)

command = arguments[0]
args = arguments[1]

# ------------- Main Execution --------------
debug('Executing "{} {}" for at most {} seconds...', command, args, seconds)

try:
	debug('Forking...')				# Fork process
	pid = os.fork()
	if pid == 0:    				# Child
		try:
			debug('Execing...')
			os.execlp(command, command, args)
		except OSError as e:
			debug('Unable to exec: {}', e)
			
	else:           				# Parent
		debug('Enabling alarm...') 	# Enable alarm
		signal.signal(signal.SIGALRM, handler)
		signal.alarm(seconds)
				
		try:
			debug('Waiting...')		# Wait
			pid, status = os.wait()
		except OSError as e:  		# Pending clean up
			if e.errno == errno.EINTR:  # Another wait
				pid, status = os.wait() 
			else:
				error(e)
	
		debug('Disabling alarm...')	# Disabling
		signal.alarm(0)
		debug ('Process {} terminated with exit status {}', pid, status << 8)
		if status == 0:				# Success
			sys.exit(0)
		elif status != 0:			# Failure
			sys.exit(1)
				
except OSError as e:				# Error
	debug('Unable to fork: {}', e)
	