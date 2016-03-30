#!/usr/bin/env python2.7

import getopt, os, sys, tempfile

# Global Variables
PROGRAM_NAME = os.path.basename(sys.argv[0])
temp = tempfile.NamedTemporaryFile(delete=False)

# Functions
def usage(status=0):
    error('''Usage: imv.py FILES...'''.format(PROGRAM_NAME), status)

def error(message, status=1):
    print >>sys.stderr, message
    sys.exit(status)

# Read in the file names
files = sys.argv[1:]
if files[0] == '-h':
	usage(1)
	
# Main Execution
for name in files:
	temp.write(name+"\n")
temp.close()

# Open editor
try:
	success = os.system('${EDITOR:-nano} '+temp.name) # Default Nano
except OSError:
	sys.exit(1)

# Continue if successful
if success == 0:
	list =[]
	file = open(temp.name, 'r')
	changes = []
	
	# Append and strip new line
	for lines in file:
		changes.append(lines.strip('\n'))
	list = zip(changes, files)
	
	# Rename
	for changed, old in list:
		try:
			os.rename(old, changed)
		except OSError as e:
			print >>sys.stderr, 'Could not rename file {}: {}'.format(old, e)
			sys.exit(1)

# Remove temporary file
os.unlink(temp.name)


