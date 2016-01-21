Homework 01
===========

Exercise 01: Paths *(2 Points)*
-------------------------------

1. How would you navigate to the csesoft AFS home directory using an absolute path?

2. How would you navigate to the csesoft AFS home directory using a relative path?

3. How would you navigate to the csesoft AFS home directory using a path that contains ~?

4. How would you create a shortcut or link in your own $HOME directory called csesoft to the csesoft AFS home directory.


Exercise 02: Copying, Moving, Removing *(3 Points)*
---------------------------------------------------

1. How would you copy all the contents of the /usr/share/pixmaps folder to a new images folder in your AFS home directory?

2. Perform the copy operation above and then inspect the symlinks in the new images folder. Are there any broken links? If so, how do you know and why are they broken?

3. How would you rename the images folder to pixmaps? Time this operation using the time command.

4. How would you move the pixmaps to /tmp/$USER-pixmaps (where $USER is your netid)? Time this operation using the time command. Is this operation slower? Why?

5. How would you remove the /tmp/$USER-pixmaps folder? Time this operation using the time command. How does this compare to the previous move command?


Exercise 03: Files and Directories *(5 Points)*
-----------------------------------------------

1. How would you list the contents of the software directory such that you get a long listing with file sizes in human readable format (ie. K, M, G, etc.)?

2. How would you list the contents of the software directory such that you get a long listing of objects from newest to oldest (ie. the most recently modified file or directory is listed at the top)?

3. The Cooperative Computing Lab develops a set of distributed and scientific computing applications collectively called the CCTools and provides the latest version of the software at the following path:

/afs/nd.edu/user37/ccl/software/cctools/x86_64
How many total files (excluding directories) are in the directory above? What command(s) did you use to determine the total?

4. Does the directory above contain an executable named weaver? If so, that is the program written by the instructor for his dissertation. What command(s) did you use to determine if the folder contained weaver?

5. Which of the three folders in the /afs/nd.edu/user37/ccl/software/cctools/x86_64 directory is the largest and how large is it (in terms of megabytes)? What command(s) did you use to determine the largest directory and its size?

6. How many files are in the largest folder found above? What command(s) did you use to determine the number of files in the largest folder?

7. What is the largest file in the /afs/nd.edu/user37/ccl/software/cctools/x86_64 directory? What command(s) did you use to determine the largest file?

8. How many files in the /afs/nd.edu/user37/ccl/software/cctools/x86_64 directory have not been modified in more than 30 days? What command(s) did you use to determine this?