TLDR - strace
==========

Overview
--------

[strace] is a command that traces system calls and signals

Examples
--------

- **Trace** the execution of the ls command:

		$ strace ls

- **Trace** a specific system call in an executable:

        $ strace -e open ls

- **Save** the trace execution into a file:
		
		$ strace -o output.txt ls


Resources
---------

- [Linux Manual](http://man7.org/linux/man-pages/man1/strace.1.html)
