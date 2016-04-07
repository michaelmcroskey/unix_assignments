Homework 08
===========

### Part 1

**1. What the role of the parent and child processes were and how each accomplished their tasks using system calls.**

The parent process ensures that the child process completes within 10 seconds (or how long is specified). Meanwhile, the child takes in the user's command and executes it via os.execlp.

**2. How the timeout mechanism worked and what system calls were used.**

The signal.alarm and signal.signal were important for the timeout mechanism, which essentially self-reports when the process doesn't complete when it should. So basically the child starts and then the parent waits, but specifically for a successful execution. If not, it terminates with SIGTERM.

**3. How the test script verifies the correctness of your program.**

I just used word count on a few commands to determine if the output was zero or not. If at any point down the line, one of the commands did not produce an output, the program fails in that section. Further, I could grab the exit status with echo $? and compare that to 0.

**4. What happens when you set SECONDS and the argument to sleep to the same duration.  Do you always get the same result (ie. does the script exit with success or failure each time)? Explain how you experimented with this and whether or not it is reasonable to expect consistent results.**

I think I broke my terminal...Haha no but really I forgot to allow me to quit the application I made so it just kept printing 1s no matter what value I entered. I created a while loop to continuously run the command with seconds=2 until n=300. At least in my tests, it just always printed 1. I guess it was consistent for me.

### Part 2

**1. How you scanned the filesystem to ensure you checked the files in the specified directories. **

The check_directory() accomplishes this using os.walk(directory) and for loops that reference each file and call check_file() on each.

**2. How you loaded the rules and used them to check the files.**

First I installed yaml on my local machine, then used yaml.load(stream) to load a simple file I created based on the example rules online. Then I used a dictionary to cycle through and see which patterns match.

**3. What data structure did you use to help detect changes to files and the logic you used determine if a file was new or modified.**

Dictionary - it painlessly (haha) allowed me to reference date changes I found via stat or even its existence. Differences between files meant using execute_action().

**4. How you executed each action.**
 
First I saw if the action was the path or name and made appropriate adjustments to my list. Next I forked and tried to execute the action specified, unless the pid wasn't 0 in which case I could wait to eventually terminate the child.

**5. The current design to rorschach.py suffers from two problems related to the following concepts: busy waiting and cache invalidation. Explain what these problems mean in the context of rorschach.py and under which scenarios would these issues cause performance or efficiency challenges. What are some ways these challenges can be alleviated? (You don't have to implement them, just suggest a few ways we can prevent or mitigate busy waiting and how to implement cache invalidation) **

Busy waiting simply means that rorschach.py has to repeatedly check if changes have occurred in such a large recursive structure. I would fix this by storing when a folder has changed so that it doesn't always need to check sub-folders. Cache invalidation is when uneccessary entries are deleted from a dictionary. Caching can always mean more data than necessary, so it's a good idea to keep the working dictionary fresh and then store the other values in a more static archive.

