#!/usr/bin/env python2.7

import getopt
import os
import sys

# Global Variable

N = False

# Usage function

def usage(status=0):
    print '''usage: uniq.py [-c] files ...

    -c      prefix lines by the number of occurrence'''.format(os.path.basename(sys.argv[0]))
    sys.exit(status)

# Parse command line options

try:
    opts, args = getopt.getopt(sys.argv[1:], "hc")
except getopt.GetoptError as e:
    print e
    usage(1)

for o, a in opts:
    if o == '-c':
        N = True
    else:
        usage(1)

if len(args) == 0:
    args.append('-')

# Main execution

for path in args:
    if path == '-':
    stream = sys.stdin
else :
    stream = open(path)
dict = {}
last = None
if N == True:
    for line in stream:
    if line != last:
    if last in dict:
    print '{:>7} {}'.format(dict[last], last),
    dict[line] = 1
last = line
elif line == last:
    dict[line] += 1

if line in dict:
    print '{:>7} {}'.format(dict[line], line),

    else :
        for line in stream:
        if line != last:
    if last in dict:
    print last,
    dict[line] = 1
last = line
elif line == last:
    dict[line] += 1
if line in dict:
    print line,
    stream.close()

