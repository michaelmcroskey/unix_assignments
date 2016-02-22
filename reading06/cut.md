TLDR - cut
==========

Overview
--------

[cut] is a command that removes sections from lines of files, reading from standard input

Examples
--------

- *Cut* 3rd field of each line (need tabs)

	$ cut -f 3 dog.txt

- *Display* the 4th through 9th characters of each line

	$ cut -c 4-9 dog.txt

- *Output* words in the first line that come after the colon (as delimiter)
		
	$ cut -f 1 -d ':' /etc/passwd


Resources
---------

- [Linux Manual](http://man7.org/linux/man-pages/)

[cut]: http://man7.org/linux/man-pages/man1/cut.1.html