TLDR - head
==========

Overview
--------

[head] is a command that prints the first N lines (or other measure) of a file

Examples
--------

- *Display* first 10 entries in folder (default)
	
	$ ls | head

- *View* first 23 lines of a file

	$ head -n 23 dog.txt 

- *Exclude* last 10 lines (print all but last 10)
		
	$ head -n -10 cat.txt


Resources
---------

- [Linux Manual](http://man7.org/linux/man-pages/)

[head]: http://man7.org/linux/man-pages/man1/head.1.html