Homework 07
===========

## dd.py

**1. How you handled parsing the command line options.**

I used a for loop to go through each of the arguments, testing in each case if the current value was equal to a flag and if so, grabbing the following value and incrementing the counter. I had already set some variables for default values. 

**2. How you opened the input and output files (in particular, what modes did you use).**

I created an open_fd function with exception handling that uses os.open(path, mode) where the mode was os.O_RDONLY for open. The target file had to include os.O_CREAT|os.O_WRONLY in case we had to create a file.

**3. How you utilized the seek and skip arguments.**

I again created functions for these, lseek_fd(file, skip*bs, os.SEEK_SET), where the byte size (bs) was 512 and it relied on os.lseek. The file is different in each case, as it is source in skip and target in seek. Also, seeking does the seek*bs.

**4. How you utilized count and bs to read data from if and write to of.**

I set count equal to sys.maxint, then checked if my iterator reached count to stop the while loop. Then I invoked the write_fd function which utilizes os.write(path, mode) to copy the data over, reading from the source each time. The counter is important to stop it once it's copied everything.


## find.py

**1. How you handled parsing the command line options.**

I used a very similar implementation to my ./dd.py script, only this one used a while loop and took into account that not all flags carry a value with them (I didn't need to use split command). In pretty much every case, triggering the if condition meant switching the boolean value of a variable to 1 from the default 0. I used os, stat, re, and fnmatch calls. 

**2. How you walked the directory tree.**

I walked the directory tree using a couple of for loops. I looked for help online for this because I wasn't sure how to use the os.walk listings. It simply required three iterators, two of which I concatenated. I called the include() function on the different elements in files + dirs based on the root, which recusively steps through the tree.

**3. How you determined whether or not to print a filesystem objects path.**

I determined to print a filesystem object's path in my include() function, which checked for each of the flags. If no conditions are met, it actually returns true. False means don't print the path while true means do. This print is located in the innermost for loop, so it recursively works to call paths.

**4. Use strace to compare the number of calls to the stat system call your find.py does compared to the traditional find command on /etc. Do you notice anything strange with find's implementation? Investigate and explain how find is getting file information.**

Using "strace -c ./find.py /etc" I found that my code was incredibly inefficient. I attempted to call os.stat once but ended up calling stat a lot more times (41639 times). I couldn't figure out the correct syntax to have to only call it once, which would have drastically decreased the amount of calls I think. I'm not sure if having the recursive for loop is also part of the problem, but "strace -c find /etc" produced just 24 stat calls.