Homework 01 - Grading
=====================

**Score**: 13.25 / 15

Deductions
----------
Exercise 2(#2): -0.25 --
But the question asks *why* they are broken. The answer is because these links have relative paths. Those paths are now broken because they were based off of its previous file location.

Exercise 3(#2): -0.25 --
It asks for a *long listing* (ie. use the -l flag as well).

Exercise 3(#3): -0.50 --
There are actually many more! Dont forget to check inside of the subdirectories. Try using **find**. 

Exercise 3(#7): -0.25 --
You found the correct largest file, but the command is not a valid solution to this problem. Try using **sort** to get the findings into size order and then use **head** to filter out just the largest files.

Exercise 3(#8): -0.25 --
Dont forget to pipe that command into **wc** so that you can count the number. It looks like this works, but a simpler approach can be found by using the -mtime flag that **find** provides.

Exercise 5(#2): -0.25 --
This question asked for the **Unix** permissions (ie. ugo rwx), not the AFS permissions.

Comments
--------
