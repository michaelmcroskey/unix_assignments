TLDR - ldd
==========

Overview
--------

[ldd] is a command that prints shared object dependencies

Examples
--------

- **Find** the dependencies of the execv file:

		$ ldd execv

- **Produce** more information in the output:

        $ ldd -v libshared.so

- **Run** command on dynamic executable:
		
		$ ldd -r assert.o


Resources
---------

- [Linux Manual](http://man7.org/linux/man-pages/man1/ldd.1.html)
