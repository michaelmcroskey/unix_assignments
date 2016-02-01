Reading 01
==========

**Questions:**
--------------

1. Create a file *Private* that is only readable to you.

	$ chmod 600 Private.md 

2. Create a link to /afs/nd.edu/coursesp.16/cse/cse20189.01 in your home directory.

	$ ln -s /afs/nd.edu/coursesp.16/cse/cse20189.01

3. Determine the size of a file named *BigFile*

	$ du -hs BigFile.md

4. Determine the size of a directory named *MyFolder*.

	$ du -hs MyFolder

5. Given the following output of *ps ux;* terminate the *ssh student00* process.

	$ kill 25263

6. Given the output of *ps ux* above, how would you terminate all of the *urxvt* processes in one command?

	$ kill -9 25129 25913

7. Determine how long a program named simulation takes to run.

	$ time simulation

8. Persistently set the default your shell's *EDITOR* to your weapon of choice.

	$ setenv EDITOR nano
