#!/usr/bin/env python2.7
# Michael McRoskey

import os, sys, stat, fnmatch, re

# Variables
type_file = type = executable = readable = writable = empty = pattern = mode = file = n = 0
nameFlag = pathFlag = regexFlag = permFlag = newerFlag = uidFlag = gidFlag = 0

# Functions
def usage():
	print('''
Usage: find.py d [options]...

Options:

    -type [f|d]     File is of type f for regular file or d for d

    -executable     File is executable and directories are searchable to user
    -readable       File readable to user
    -writable       File is writable to user

    -empty          File or d is empty

    -name  pattern  Base of file name matches shell pattern
    -path  pattern  Path of file matches shell pattern
    -regex pattern  Path of file matches regular expression

    -perm  mode     File\'s permission bits are exactly mode (octal)
    -newer file     File was modified more recently than file

    -uid   n        File\'s numeric user ID is n
    -gid   n        File\'s numeric group ID is n
''')

def include(path):
	''' Returns True if item should be included in output, otherwise False '''
	
	try:
		data = os.stat(path)
	except OSError:
		data = os.lstat(path)

	if type:
		if type_file == 'f' and not stat.S_ISREG(data.st_mode):
			return False
		elif type_file == 'd' and not stat.S_ISDIR(data.st_mode):
			return False
			
	if executable and not os.access(path, os.X_OK):
		return False
		
	if readable and not os.access(path, os.R_OK):
		return False
		
	if writable and not os.access(path, os.W_OK):
		return False
		
	if empty:
		if (stat.S_ISREG(data.st_mode)) and (os.path.getsize(path) > 0):
			return False
		try:
			if (stat.S_ISDIR(data.st_mode)) and (len(os.listdir(path)) > 0):
				return False
		except OSError:
				return False
		if os.path.islink(path) and not os.path.exists(os.readlink(path)):  
			return False
			
	if nameFlag and not fnmatch.fnmatch(os.path.basename(path), pattern):
		return False
		
	if pathFlag and not fnmatch.fnmatch(path, pattern):
		return False
		
	if regexFlag and not re.search(pattern, path):
		return False
	
	
	if permFlag and not stat.S_IMODE(data.st_mode) == mode:
		return False
		
	if newerFlag and (data.st_mtime <= os.stat(file).st_mtime):
		return False
		
	if uidFlag and not (data.st_uid == n):
		return False
		
	if gidFlag and not (data.st_gid == n):
		return False
	return True


# Parse Command line args
d = sys.argv[1]
args = sys.argv[2:]
i = 0

while i < len(args):
	if (args[i]=='-type'):
		type = 1
		type_file = args[i+1]
		i+=1
		
	elif (args[i]=='-executable'):
		executable = 1
		
	elif (args[i]=='-readable'):
		readable = 1
		
	elif (args[i]=='-writable'):
		writable = 1
		
	elif (args[i]=='-empty'):
		empty = 1
		
	elif (args[i]=='-name'):
		nameFlag = 1
		pattern = args[i+1]
		i+=1
		
	elif (args[i]=='-path'):
		pathFlag = 1
		pattern = args[i+1]
		i+=1
		
	elif (args[i]=='-regex'):
		regexFlag = 1
		pattern = args[i+1]
		i+=1
		
	elif (args[i]=='-perm'):
		permFlag = 1
		mode = int(args[i+1], 8)
		i+=1
		
	elif (args[i]=='-newer'):
		newerFlag = 1
		file = args[i+1]
		i+=1
		
	elif (args[i]=='-uid'):
		uidFlag = 1 
		n = int(args[i+1])
		i+=1
		
	elif (args[i]=='-gid'):
		gidFlag = 1
		n = int(args[i+1])
		i+=1
		
	i+=1
	
# Main Execution
if include(d):
	print d

for root, dirs, files in os.walk(d, followlinks=True):
	for name in files + dirs:
		if include(os.path.join(root, name)):
			print os.path.join(root, name)
