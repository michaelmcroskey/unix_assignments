Homework 04
===========

Describe how you implemented the bake.sh script. In particular, briefly discuss:

a. How you handled setting variables and the default values.
------------------------------------------------------------

> I used the ${VARIABLE:="command"} syntax to define CC, CFLAGS, SUFFIXES, and VERBOSE. The := is an assignment operator in this case and sets a default value that can be overwritten using the $env command at runtime

b. How you iterated over all the files that match the SUFFIXES.
--------------------------------------------------------------

> Because SUFFIXES was already defined to ".c", I simply made a for loop cycling through the files (iterator named "i") in *$SUFFIXES, meaning any file that ends in the suffix mentioned (.c in this case).

c. How you handled the VERBOSE variable.
-------------------------------------------

> I set the default value to zero so that pretty much any other value for the environmental variable VERBOSE would trigger the if statement. I just made it so that it echoed the entire command it was doing inside the while loop (for each file) and added the -v flag for verbose warnings.

d. How you terminated the program early if the compilation command failed.
--------------------------------------------------------------------------

> I used short circuit evaluation in the compilation statement through the logical || or symbols and had an exit 1 (non-zero exit status) as the argument

Compare using bake.sh to make. What are the advantages and disadvantages of both automated building techniques? What will you use in the future (bake.sh, make, or something else)?
-------------------------------------------------

> I think I would prefer make becuase it follows almost the same template each time. Bake is great for compiling multiple files and to that extent it would take more lines of code to compile many files in a certain directory using a makefile. I like the simplicity and organization of makefiles.


