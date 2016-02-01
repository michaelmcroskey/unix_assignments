Reading 03
==========

Commands
--------

1) View all the text in ls.

	View binary text
	$ cat /bin/ls
	
	Just human readable
	$ strings /bin/ls

2) Determine which shared libraries ls requires.

	$ ldd /bin/ls

3) View all the system calls made during an invocation of ls.

	$ strace /bin/ls

4) Debug the hello-debug program to fix errors.

	$ strace -o strace.out hello-debug

5) Check the hello-dynamic program for memory leaks or errors.

	$ valgrind hello-dynamic

6) Profile the hello-profile program to find any bottlenecks.

	$ gprof hello-profile