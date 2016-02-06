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

3) For each of the three classes of bugs, describe how you diagnosed the problem, what the problem was, and how you fixed it. Be sure to explain the commands you used to track down the bugs and why your modifications address the issues you found.
	
	- First I used valgrind to find out that there was a memory leak in the program by making the file and then running: $ valgrind --leak-check=yes ./is_palindrome
	This showed a specific line where there was an issue, line 41 for me. Buffer was improperly declared.
	
	- Next I made sure to properly allocate and more importantly free memory using malloc and free after using the commands:
	$ gdb ./is_palindrome
	I realized I needed to subtract 1 from strlen(s) in line 28, needed to malloc in line 39
	
	- I had to free sanitized in line 23 because it wasn't being freed from the heap. 
	
4) I think it was the hardest to realize that strlen(s) was causing the memory to look out of bounds and trying to figure out where to add/subtract 1. I think extreme care needs to go in defining boundaries of arrays, especially when using pointers and strings in the future.



Activity 03: Trace It (3 Points)
--------------------------------

1) Initial contact with the courier:
	$ /afs/nd.edu/user15/pbui/pub/bin/COURIER
	
	He said
	 ________________________________________ 
	/ Hmm... you sure you put the package in \
	\ the right place?                       /
	 ---------------------------------------- 
	
2) Finding the package location
	$ strings /afs/nd.edu/user15/pbui/pub/bin/COURIER
	
	Returned:
	Uh... who are you?
	/tmp/%s.deaddrop
	Hmm... you sure you put the package in the right place?
	Whoa whoa... you can't give everyone access to the package! Lock it down!
	Uh... what happened to the package?  I just saw it a moment ago, but now I can' open it...
	What are you trying to pull here?  The package is the wrong size!
	Well, everything looks good... I'm not sure what '%s' means, but I'll pass it on.
	
3) So I cd'd to /tmp and figured I needed to make ____.deadrop, but didn't know what so I did my username

	$ touch mmcrosk1.deaddrop
	
4) Then I returned to the courier using that path to get:

	 ______________________________________ 
	/ Whoa whoa... you can't give everyone \
	\ access to the package! Lock it down! /
	 -------------------------------------- 
	
5) ...which I should have expected because I could've seen every message earlier that the courier had stored... but anyway I realized it would be a file permission thing, so limited the permissions to me (after first limiting it to no one with 000):
	
	$ /tmp
	$ chmod 700 mmcrosk1.deaddrop 
	
	
	Response when I returned:
	
	/ What are you trying to pull here? The \
	\ package is the wrong size!            /
	
6) So I thought I needed to increase the size of the file by editing it

	$ nano mmcrosk1.deadrop
	
	I wrote a nice little message for the courier
	
7) Then I went back to the courier

	 ________________________________________ 
	/ Well, everything looks good... I'm not \
	| sure what 'Hello Co' means, but I'll   |
	\ pass it on.                            /
	 ---------------------------------------- 

	And I think that does it!
