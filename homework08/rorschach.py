#!/usr/bin/env python2.7

# ---------------- Import -------------------
import getopt
import os
import sys
import yaml
import re
import fnmatch
import time
import shlex
import signal

# ----------- Global Variables --------------
rules = 'rules.yaml'
seconds = 2
DIRECTORIES = '.'
verbose = False
modified = {}

# --------------- Functions -----------------
def error(message, status=1):
    print >>sys.stderr, message
    sys.exit(status)

def handler(signum, frame):
	os.kill(pid, signal.SIGTERM)

def usage(status=0):
    error('''Usage: rorschach.py [-r RULES -t SECONDS] dirs...
Options:

    -r RULES    Path to rules file (default is .rorschach.yml)
    -t SECONDS  Time between scans (default is 2 seconds)
    -v          Display verbose debugging output
    -h          Show this help message
	'''
    .format('./rorschach.yml'), status)

def check_directory():
	for directory in DIRECTORIES:
		
		try:
			for root, dirs, files in os.walk(directory):
				for name in files + dirs:
					
					try:
						if (os.path.join(root,name)) not in modified.keys():
							try:
								modified.update({os.path.join(root,name): os.stat(os.path.join(root,name))[8]})
								
							except getopt.GetoptError as e:
								error(e)
					except getopt.GetoptError as e:
						error(e)
		except getopt.GetoptError as e:
			error(e)
			
	# chech_file on dictionary
	for directory in DIRECTORIES:
		
		try:
			for root, dirs, files in os.walk(directory):
				for name in files + dirs:
					
					try:
						check = check_file(os.path.join(root, name), name)
					except getopt.GetoptError as e:
						error(e)
		except getopt.GetoptError as e:
			error(e)
					

def check_file(file, name):
	for d in rules:
		for key, val in d.iteritems():
			
			if key == 'pattern':
				pattern = val
				try:
					if fnmatch.fnmatch(file, pattern) and os.stat(file)[8] != modified[file]:
						execute_action(file, name)
				except getopt.GetoptError as e:
				    error(e)
			
def execute_action(file, name):
	# Define lists
	shlexList = []
	arguments = []
	list = []
	
	for d in rules:
		for key, val in d.iteritems():
			
			if key == 'action':
				
				shlexList = shlex.split(val)
				list.append(shlexList[0]) 
				
				for paths in range(len(shlexList)):
					
					if shlexList[paths] == '{path}':
						path = file
						arguments.append(path)

						try: 
							pid = os.fork()
						except getopt.GetoptError as e:
							error(e)
							
						if pid == 0: # Child Process
							try:
								os.execvp(list[0], (list[0],) + tuple(arguments))
							except getopt.GetoptError as e:
								error(e)
						else:
							modified.update({file : os.stat(file)[8]})
							signal.signal(signal.SIGTERM, handler)
							pid, status = os.wait()
							
					elif shlexList[paths] == '{name}':
						nameVar = name 
						arguments.append(nameVar)
						
						try:
							pid = os.fork()
						except getopt.GetoptError as e:
							error(e)
							
						if pid == 0: # Child process
							try:
								os.execvp(list[0], (list[0],) + tuple(arguments))
							except getopt.GetoptError as e:
								error(e)
						else:
							modified.update({file : os.stat(file)[8]})
							signal.signal(signal.SIGTERM, handler)
							pid, status = os.wait()
							
					arguments[:] = []

# --------------- Arguments -----------------
try:
    opts, args = getopt.getopt(sys.argv[1:], "r:t:vh")
except getopt.GetoptError as e:
    error(e)

for opt, val in opts:
	if opt == '-h': 
		usage(0)
	elif opt == '-t':
		seconds = val 
	elif opt == '-r':
		rules = val 
	elif opt == '-v':
		verbose = True
	else:
		usage(1)
				
dirs = args

# ------------- Main Execution --------------
stream = file(rules, 'r')
rules = yaml.load(stream)

try:
	while True:
		time.sleep(seconds)
		check_directory()	
except getopt.GetoptError as e:
	sys.exit(0)
