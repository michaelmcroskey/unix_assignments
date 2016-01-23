ents
Homework 01
===========

Exercise 01: Paths *(2 Points)*
-------------------------------

1. How would you navigate to the csesoft AFS home directory using an absolute path?
	
	$ cd /afs/nd.edu/user14/csesoft

2. How would you navigate to the csesoft AFS home directory using a relative path?
	
	$ cd ../../user14/csesoft

3. How would you navigate to the csesoft AFS home directory using a path that contains ~?

	$ cd ~/../../user14/csesoft

4. How would you create a shortcut or link in your own $HOME directory called csesoft to the csesoft AFS home directory.

	$ ln -s /afs/nd.edu/user14/csesoft ~/csesoft


Exercise 02: Copying, Moving, Removing *(3 Points)*
---------------------------------------------------

1. How would you copy all the contents of the /usr/share/pixmaps folder to a new images folder in your AFS home directory?

	$ cd ~; mkdir images; cp -a /usr/share/pixmaps/. ~/images

2. Perform the copy operation above and then inspect the symlinks in the new images folder. Are there any broken links? If so, how do you know and why are they broken?

	$ find . -xtype l
	- There are 24 broken links
	- xtype is a test performed on a dereferenced link

3. How would you rename the images folder to pixmaps? Time this operation using the time command.
	
	$ mv ~/images ~/pixmaps
	
4. How would you move the pixmaps to /tmp/$USER-pixmaps (where $USER is your netid)? Time this operation using the time command. Is this operation slower? Why?

	$ time mv ~/pixmaps /tmp/mmcrosk1-pixmaps
	- Yes this operation is slower than simply renaming becuase it requires both renaming and moving the file directoy. Quantitatively, **mv** took 0.001s when used to rename and took 0.049s when used to move and rename in this case

5. How would you remove the /tmp/$USER-pixmaps folder? Time this operation using the time command. How does this compare to the previous move command?

	$ time rmdir --ignore-fail-on-non-empty /tmp/mmcrosk1-pixmaps
	- This operation is much slower than the previous two becuase they are removing each file inside the directory as well as the directory itself


Exercise 03: Files and Directories *(5 Points)*
-----------------------------------------------

1. How would you list the contents of the software directory such that you get a long listing with file sizes in human readable format (ie. K, M, G, etc.)?

	$ ls -l -h

2. How would you list the contents of the software directory such that you get a long listing of objects from newest to oldest (ie. the most recently modified file or directory is listed at the top)?

	$ 

3. The Cooperative Computing Lab develops a set of distributed and scientific computing applications collectively called the CCTools and provides the latest version of the software at the following path:

	/afs/nd.edu/user37/ccl/software/cctools/x86_64
	How many total files (excluding directories) are in the directory above? What command(s) did you use to determine the total?

4. Does the directory above contain an executable named weaver? If so, that is the program written by the instructor for his dissertation. What command(s) did you use to determine if the folder contained weaver?

5. Which of the three folders in the /afs/nd.edu/user37/ccl/software/cctools/x86_64 directory is the largest and how large is it (in terms of megabytes)? What command(s) did you use to determine the largest directory and its size?

6. How many files are in the largest folder found above? What command(s) did you use to determine the number of files in the largest folder?

7. What is the largest file in the /afs/nd.edu/user37/ccl/software/cctools/x86_64 directory? What command(s) did you use to determine the largest file?

8. How many files in the /afs/nd.edu/user37/ccl/software/cctools/x86_64 directory have not been modified in more than 30 days? What command(s) did you use to determine this?


Exercise 04: Unix Permissions *(2 Points)*
------------------------------------------

1. Identify who can read from that file, write to that file, and execute that file.

2. What command would you execute to change data.txt such that:

	a. Only you can read and write to the file.

	b. Only you and members of your group can read, write, and execute the file.

	c. Anyone can read the file.

	d. There are no permissions on the file.

3. If there are no permissions on the file, who can delete the file?


Exercise 05: AFS Permissions *(2 Points)*
-----------------------------------------

1. Use the fs listacl command to view the ACLs on your home directory, your Private directory, and your Public directory. What are the differences in the ACLs for those three folders and what do those differences mean?

2. What are the Unix permissions for the folder /afs/nd.edu/commons? Use touch create a file /afs/nd.edu/commons/$USER.txt (where $USER is your netid). What happened? Explain.

3. How would you use the fs setacl command to give the instructor (but no one else but yourself) access to a folder in your home directory?


Exercise 06: Masks *(1 Point)*
------------------------------

1. Type umask 000 and then use touch to create a file called world1.txt.
2. Type umask 022 and then use touch to create a file called world2.txt.
3. Type umask 044 and then use touch to create a file called world3.txt.
What are the permissions of each of the three files you created? Are they the same? Why or why not? Explain the effect umask has on file creation and how this can be useful.





