Homework 03
===========

Activity 01: Make It (5 Points)
-------------------------------
1) Given the following pairs of files, identify which one of the two is larger and discuss why:

a. libgcd.a vs libgcd.so
	
	libgcd.so is the larger file because it is a shared library and needs to connect everything via file paths, which can take up more file space

b. gcd-static vs gcd-dynamic

	gcd-static is the larger file because 
	

2) What libraries does gcd-static depend on? What libraries does gcd-dynamic depend on? How did you find out?

	gcd-static loads the entire library (accounting for the 90x file size as dynamic) as opposed to dynamic, which will just reference the libraries and load them at run time. gcd-dynamic depends on:
		linux-vdso.so.1 =>  (0x00007fff13f7f000)
		libgcd.so => not found
		libc.so.6 => /lib64/libc.so.6 (0x0000003ea5600000)
		/lib64/ld-linux-x86-64.so.2 (0x0000003ea5200000)
	
	I used the command:
	$ ldd gcd-dynamic
	
	gcd-static returned the error:
	not a dynamic executable
	
	I used the command
	$ ldd gcd-static

3) Try to run the gcd-dynamic application. Did it work? Why or why not? Which environment variable could we set to allow gcd-dynamic to execute and what would we set it to?

	./gcd-dynamic: error while loading shared libraries: libgcd.so: cannot open shared object file: No such file or directory
	
	This clearly did not work. This is because one of the paths was not found. I need to set the environmental variable LD_LIBRARY_PATH to specify another path for the linker to look for libraries. I used the command:
	$ setenv LD_LIBRARY_PATH .

What are the advantages and disadvantages to static and dynamic linking? If you were to create an application which type of executable would you want to produce by default? Explain your choice and discuss your reasoning.

	Static linking will ensure that your file will run regardless of misplaced files or broken connections, however, those file sizes will be much larger. I would defaultly produce static linking, only because of the assured output. However, dynamic would be nice if my libraries were to adapt/change and update. There seems to be a lot more issues with dynamic libraries with tracking down the linked libraries if they aren't in the same directory or whatever. However, the file size would be certainly worth it.

Activity 02: Fix It (7 Points)
------------------------------

1) How did you download and extract the is_palindrome.tar.gz archive? What commands did you use?

	First cd to the folder you want to extract the file to, in this case "homework03"
	
	$ curl https://www3.nd.edu/~pbui/teaching/cse.20189.sp16/static/tar/is_palindrome.tar.gz | tar xvz
	
2) What flags did you use to force gcc to include debugging symbols in the is_palindrome executable? How does including these symbols affect the size of the executable? Explain and provide evidence.

	$ gcc -g executable -gdwarf-2
	
	As the homework mentioned, 

3) Line 41
buffer improperly declared

Activity 03: Trace It (3 Points)
--------------------------------