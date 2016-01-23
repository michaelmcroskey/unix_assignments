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

	$ ls -t

3. The Cooperative Computing Lab develops a set of distributed and scientific computing applications collectively called the CCTools and provides the latest version of the software at the following path:

	/afs/nd.edu/user37/ccl/software/cctools/x86_64
	How many total files (excluding directories) are in the directory above? What command(s) did you use to determine the total?
	
	- There are three files in this directory
	$ ls | wc -l

4. Does the directory above contain an executable named weaver? If so, that is the program written by the instructor for his dissertation. What command(s) did you use to determine if the folder contained weaver?

	- Yes, it returned:
		- ./redhat6/lib/python2.6/site-packages/weaver
		- ./redhat6/bin/weaver
		- ./osx-10.9/lib/python2.7/site-packages/weaver
		- ./osx-10.9/bin/weaver
	$ cd /afs/nd.edu/user37/ccl/software/cctools/x86_64
	$ find . -name "weaver" -print

5. Which of the three folders in the /afs/nd.edu/user37/ccl/software/cctools/x86_64 directory is the largest and how large is it (in terms of megabytes)? What command(s) did you use to determine the largest directory and its size?
	
	- I used the commands:
	
	$ du -sh osx-10.9
	$ du -sh redhat5
	$ du -sh redhat6
			
	- And saw that the largest directory was redhat5 at 77 Megabytes

6. How many files are in the largest folder found above? What command(s) did you use to determine the number of files in the largest folder?

	- There are 6 folders in the largest folder
	
	$ cd redhat5; ls | wc -l
	
	- There are 798 files in the largest folder
	
	$ cd redhat5; find .//. ! -name . -print | grep -c //

7. What is the largest file in the /afs/nd.edu/user37/ccl/software/cctools/x86_64 directory? What command(s) did you use to determine the largest file?

	- The largest file is parrot_run
	
	$ find . -type f -size +17M

8. How many files in the /afs/nd.edu/user37/ccl/software/cctools/x86_64 directory have not been modified in more than 30 days? What command(s) did you use to determine this?

	$ find . -type f -newermt 20151222 \! -newermt 20160122

	- There are 2025 total files (using find .//. ! -name . -print | grep -c //) and 22 have been modified in the last 30 days via the command above meaning 2003 files have not been modified in the last 30 days


Exercise 04: Unix Permissions *(2 Points)*
------------------------------------------

$ rwxr-x--x

1. Identify who can read from that file, write to that file, and execute that file.

	- The file owner can read, write, and execute
	- The group that file is associated with can read and execute
	- Everyone else can execute
	

2. What command would you execute to change data.txt such that:

	a. Only you can read and write to the file.
		
		$ chmod go-rwx data.txt; chmod u-x data.txt

	b. Only you and members of your group can read, write, and execute the file.
	
		$ chmod g+w data.txt

	c. Anyone can read the file.
	
		$ chmod o+r data.txt

	d. There are no permissions on the file.
	
		$ chmod a-rwx data.txt

3. If there are no permissions on the file, who can delete the file?

	- The owner can delete the file with no permissions


Exercise 05: AFS Permissions *(2 Points)*
-----------------------------------------

1. Use the fs listacl command to view the ACLs on your home directory, your Private directory, and your Public directory. What are the differences in the ACLs for those three folders and what do those differences mean?
	
	In each of these directories, rlidwka is the system administrator (can read, lookup, insert, delete, write, lock). All of nd_campus can lookup. In my home directory, I'm the only authorized user besides rlidwka which means I have read and lookup permissions. In my Private directory it seems I have administrator rights and in my Public it shows that members of the group nd_campus can read, lookup, and lock.
	

	Access list for . is
	Normal rights:
	  nd_campus l
	  system:administrators rlidwka
	  system:authuser l
	  mmcrosk1 rlidwka

	Access list for Private is
	Normal rights:
	  system:administrators rlidwka
	  mmcrosk1 rlidwka
	
	Access list for Public is
	Normal rights:
	  nd_campus rlk
	  system:administrators rlidwka
	  system:authuser rlk
	  mmcrosk1 rlidwka

2. What are the Unix permissions for the folder /afs/nd.edu/commons? Use touch create a file /afs/nd.edu/commons/$USER.txt (where $USER is your netid). What happened? Explain.

	- Going to /afs/nd.edu/commons produced an error message: /afs/nd.edu/commons/: No such file or directory.
	- However, I did find /afs/nd.edu/common
	
	Normal rights:
	  nd_campus rl
	  system:administrators rlidwka
	  system:authuser rl
	
	- nd_campus members can read and lookup
	- Touch produced an error message: touch: cannot touch `mmcrosk1.txt': Read-only file system
	- This is a read only file system so it is not possible to create new files in the common folder

3. How would you use the fs setacl command to give the instructor (but no one else but yourself) access to a folder in your home directory?

	$ fs setacl -dir instructorFile -acl pbui r


Exercise 06: Masks *(1 Point)*
------------------------------

1. Type umask 000 and then use touch to create a file called world1.txt.
2. Type umask 022 and then use touch to create a file called world2.txt.
3. Type umask 044 and then use touch to create a file called world3.txt.
What are the permissions of each of the three files you created? Are they the same? Why or why not? Explain the effect umask has on file creation and how this can be useful.

	- world1.txt Owner, Group, and others can read and write
	- world2.txt Owner, Group, and others can read, Owner can write
	- world3.txt Group and others can read
	- These have different permissions because umask has predefined permissions depending on the number. Umask can set default file permissions quickly using custom numbers



