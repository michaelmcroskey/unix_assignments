Homework 05
===========

CAESAR
------

1) How you constructed the source set (ie. SET1).

	I created an lowercase set using {a..z} and uppercase set using {A..Z} followed by a pipe to sed to clean it up. I assigned variables to each of these.

2) How you constructed the target set (ie. SET2).

	I found the spot 13 places (or $1 places) to the right of the first letter of the alphabet and cut the alphabet and appended it to the end to essentially shift it. This meant making cuts at 13 spaces and then 26-13 spaces, which took a while to figure out how much to add or subtract believe it or not. I did this for both upper and lowercase.

3) How you used both of these sets to perform the encryption.

	Finally, I used the tr command to map the letters of the standard alphabet to my new set. It was important that my sets were the smae size. This was essentially tr $SET1 $SET2 for both upper and lowercase.

REDDIT
------

1) How you filtered the URLs and extracted only the relevant portion of the data.

	I started with a search function for each of the flags which was mostly given but added pipes to find "url", then the 4th field in that line (the url itself), and limited the results to http or https using another grep.

2) How you managed the different ordering (ie. sort, shuffle, as-is) operations.

	I made a simple elseif statement using the search and then sorting or shuffling based on my flag case structure above.

3) How the command line options affected your operations above.

	My flag case statement handles inputed flags by assigning the $var variables numbers, initializing at 0 for none. If the n flag is present, it jumps out of the default and sets n. -r comes next and then -s for shuffle and sort respectively. The case runs so that the last flag entered will run (it's impossible to shuffle and sort!)
	
BROIFY
------

1) How you removed comments.

	I made the delimeter variable DELIM=$OPTARG which means DELIM -d takes an optional argument and in this case looks for the delimeter. I used the sed -r "s|$DELIM.*||g" command which searches the input for lines that begin with the delimeter and then globally applies the replacement.

2) How you removed empty lines.

	I removed empty lines with the sed -r '/^\s*$/d' command which takes anything between ^ and $ to remove (-r) that part. In this case \s* was in between because that represents an empty line.

3) How the command line options affected your operations above.

	Again, I had to break this into a case statement with my own $var variable. Essentially, a default case without any flags would mean var=0. In the -W case, it runs a limited version of the default command to keep blank lines and remove tabs.
	
