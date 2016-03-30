#!/usr/bin/env python2.7
# Michael McRoskey

import getopt, os, sys

def usage():
	print('''
Usage: find.py directory [options]...

Options:

    -type [f|d]     File is of type f for regular file or d for directory

    -executable     File is executable and directories are searchable to user
    -readable       File readable to user
    -writable       File is writable to user

    -empty          File or directory is empty

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

    if condition:
        return False

    ...

    return True