TLDR - gcc
==========

Overview
--------

[gcc] is a command that comiles files into executable code

Examples
--------

- **Compile** a file named "file.c":

		Into a.exe
		$ gcc file.c
		
		Into hello.exe
		$ gcc -o hello.exe file.c

- **Compile** and assemble source files but don't link:

        $ gcc -o file.c -c

- **Compile** C++ code with dependents:
		
		$ g++ -o hello.exe file1.cpp file2.cpp


Resources
---------

- [Linux Manual](http://man7.org/linux/man-pages/man1/gcc.1.html)
