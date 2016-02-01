TLDR - strings
==========

Overview
--------

[strings] is a command that finds and displays the printable strings in a given executable, binary, or object file

Examples
--------

- **Display** the strings in a file named "file.c":

		$ strings file.c

- **Show** the strings in a binary command executable:

        $ strings /bin/ls

- **Show** strings with a minimum length N:
		
		$ strings file -n N


Resources
---------

- [Linux Manual](http://man7.org/linux/man-pages/man1/strings.1.html)
