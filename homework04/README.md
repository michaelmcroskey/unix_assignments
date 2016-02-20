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


Describe how you implemented the disk_usage.sh script. In particular, briefly discuss:

a. How you parsed the command line arguments.
---------------------------------------------

> I parsed the command line arguments using a case statement that chooses a case based on the $OPTION variable passed in from the command line. I made an -n and -a flag as well as a default case * which will run if those two aren't chosen. The cases themselves are simple and just assigns variables.

b. How you handled the case where there are no command line arguments.
-----------------------------------------------------------------------

> The case where there is nothing simply defaults to the du command in the current working without any flags besides -h. This will produce the file size of the current working directory.

c. How you processed each directory argument.
---------------------------------------------

> The -n flag is used to format the output and in this case only prints the first 10 lines. The -a flag is used to set the variable y which is used in the if statement that determines whether to include the -a flag.

d. How you incorporated the command line arguments into the commands you used to compute the top N items in each directory.
---------------------------------------------------------------------------------------------------------------------------

> Piping the results into the head command and setting the -n to 10 prints this information for the top N items using : head -n ${x:=10}. The n flag gives the user the ability to see a variable amount of lines.

Discuss what was the hardest part about this script and why. Additionally, identify what part of the program took up the most amount of code. Is this surprising? Why or why not?
---------------------------------------------------

> The hardest part of this script was getting the syntax right. I was really confused for a while about the use of () vs [] vs {} but figured it out through class exmaples. I think this just takes practice. The most amount of code was the actual du statement at the end, after it had been formatted and properly piped. There are like 11 arguments!


Describe how you implemented the taunt.sh script. In particular, briefly discuss:

a. How you handled different signals.
-------------------------------------

> I used functions extensively, inlcuding chickfila and sirloin, to do a simple task and call on it in my command line arguments. These used cowthink to display text and the pausing (sleeping) variable as well as an exit 1 status. 

b. How you passed long messages to cowsay.
------------------------------------------

> I kept the message in "" and used the cowthink command to take in the string.

c. How you handled the timeout.
-------------------------------

> This was implemented via a for loop which just went for 10 seconds and paused before proceeding. I used the trap commands for signal catching in the foor loop but that wasn't used for sleep.

Compare writing shell scripts to writing C programs. Which one is easier? Which one do you prefer? When would you use one over the other?
------------------------------------

> Well right now, C programs are more intuitive so I prefer it, but once I get over the syntactical hurdles, I imagine myself loving the power of shell commands. I am so intrigued by the power they possess to change computer behavior and access deep-level information. They seem to work similarly enough, I just need more practice. 

