TLDR - comm
==========

Overview
--------

[comm] is a command that compares two sorted files line by line, taking three different flags

Examples
--------

- *Suppress* lines unique to the first file:

	$ comm -1 dog.txt cat.txt

- *Suppress* lines unique to the second file:
	
	$ comm -2 dog.txt cat.txt
				
- Find *differences* between the 2 files:

	$ comm -3 dog.txt cat.txt

- Find *similarities* between the 2 files:

	$ comm -12 dog.txt cat.txt


Resources
---------

- [Linux Manual](http://man7.org/linux/man-pages/)

[comm]: http://man7.org/linux/man-pages/man1/cut.1.html