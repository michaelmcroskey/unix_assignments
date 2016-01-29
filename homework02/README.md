Homework 02
===========

Exercise 01: Transferring Files *(6 Points)*
--------------------------------------------

1) What commands did you run to create your /tmp/${USER}-workspace workspace and the data files? Provide a comment # Comment above each set of commands to describe what you did. For example:

	# Create workspace on source machine
		$ cd /tmp; mkdir mmcrosk1-workspace

	# Generate 10MB file full of random data
		$ dd if=/dev/urandom of=sample1.txt bs=10M count=1

	# Create 10 hard links to 10MB file
		$ ln sample1.txt data0
		$ ln sample1.txt data1
		$ ln sample1.txt data2
		$ ln sample1.txt data3
		$ ln sample1.txt data4
		$ ln sample1.txt data5
		$ ln sample1.txt data6
		$ ln sample1.txt data7
		$ ln sample1.txt data8
		$ ln sample1.txt data9
		

	# Create workspace on target machine
		$ ssh mmcrosk1@helios.nd.edu
		$ cd /tmp; mkdir mmcrosk1-workspace
		
2) Run the du command in the /tmp/${USER}-workspace folder of the source machine. What is the total disk usage? Is this number surprising? Why or why not?

	The total disk usage in the source was 11M. I thought this was a little surprising since I expected the file I created to account for 10M and thought the links would be sized in the bytes range or KB range, not enough I would expect to account for an entire MB (unless the computer rounds)
	
3) After you have performed the file transfers, run the du command in the /tmp/${USER}-workspace folder of the target machine. What is the total disk usage? Is this number different from the one above? Why or why not?

	The total disk usage in the target was 101M! Holy fudge! This is because each hard link is referencing the original file does it ten times (10x10M=~100). Basically, in the source directory, hard links are pretty small because they are referencing a local file.
	
4)  # Transfer data files using scp
		$ scp data* mmcrosk1@remote101.helios.nd.edu:/tmp/mmcrosk1-workspace/ 

	# Transfer data files using sftp
		$ sftp mmcrosk1@remote101.helios.nd.edu < sftp.txt
		
	# Creating SFTP text file in source directory
		$ nano sftp.txt
		cd /tmp/mmcrosk1-workspace
		mput data*

	# Transfer data files using rsync
		$ rsync data* --stats mmcrosk1@remote101.helios.nd.edu:/tmp/mmcrosk1-workspace/

5) When using scp and sftp multiple times, how often is each data file transferred? When using rsync multiple times, how often is each data file transferred? How is this feature of rsync useful?

	The scp and sftp commands will transfer the files each time (overwriting if necessary). However, rsync will only make transfers if there have been changes made to the files. This is useful when tracking changes in files and for version control.

6) Of the three commands, which one do you prefer and why?
	
	I prefer sftp because I've used sftp in web development and it seems like a universal protocol. Plus, I can modify the sftp.txt file later and run the same commands to make it do different things.
	

Exercise 02: Transferring Files *(9 Points)*
--------------------------------------------

1) Scan `xavier.h4x0r.space` for HTTP port:

	$ nmap -Pn xavier.h4x0r.space
    Output
	Starting Nmap 5.51 ( http://nmap.org ) at 2016-01-29 00:09 EST
	Nmap scan report for xavier.h4x0r.space (129.74.161.24)
	Host is up (0.00047s latency).
	Not shown: 946 filtered ports, 50 closed ports
	PORT     STATE SERVICE
	22/tcp   open  ssh
	8888/tcp open  sun-answerbook
	9111/tcp open  DragonIDSConsole
	9876/tcp open  sd
	
	
		

    As you can see here, there is are X ports in the 9000 - 10000 range.
    To check if the port was a HTTP server, I next used the X command...

2) Access HTTP server:

	First tried:
	$ curl xavier.h4x0r.space:9111
	Then tried:
	$ curl xavier.h4x0r.space:9876
	
	Output
	| If you seek the ORACLE, you must query  |
	| the DOORMAN at /{netid}/{passcode}!     |
	|                                         |
	| To retrieve your passcode you must      |
	| decode the file at                      |
	| ~pbui/pub/oracle/${USER}/code using the |
	| BASE64 command. 						   |
	
3) Decoding

	$ base64 ~pbui/pub/oracle/mmcrosk1/code
	
	Output
	T1dFNVptWTBPRGN3T1dVelkyUTFZemxqWm1VM01UQXhZemc0TUdOaFpUYz0K
	
4) Access the DOORMAN

	$ curl xavier.h4x0r.space:9876/mmcrosk1/T1dFNVptWTBPRGN3T1dVelkyUTFZemxqWm1VM01UQXhZemc0TUdOaFpUYz0K
	
	Output
	| What kinda of passcode is               |
	| T1dFNVptWTBPRGN3T1dVelkyUTFZemxqWm1VM01 |
	| UQXhZemc0TUdOaFpUYz0K? Nice try, but no |
	\ dice!                                   /
	
	2nd try for code
	$ base64 --decode ~pbui/pub/oracle/mmcrosk1/code 
	
	Output
	9a9ff48709e3cd5c9cfe7101c880cae7
	
	2nd try for DOORMAN
	$ curl xavier.h4x0r.space:9876/mmcrosk1/9a9ff48709e3cd5c9cfe7101c880cae7
	
	Output
	|                                         |
	| The ORACLE looks forward to talking to  |
	| you, but you must first retrieve a      |
	| secret message from the SLEEPER.        |
	|                                         |
	| He can be found in plain sight at       |
	| ~pbui/pub/oracle/SLEEPER... You will    |
	| need to wake him up and then signal him |
	| to HANGUP his connection. If he         |
	| recognizes you, he will give you the    |
	| message in coded form.                  |
	|                                         |
	| Once you have the message, proceed to   |
	| port 9111 and deliver the message to    |
	| the ORACLE.                             |
	|                                         |
	
5) Signal the SLEEPER

	First try
	$ pkill ~pbui/pub/oracle/SLEEPER
	
	Second try
	$ ~pbui/pub/oracle/SLEEPER
	
	Run sleeper in background
	$ ~pbui/pub/oracle/SLEEPER &
	Kill sleeper
	$ pkill -1 SLEEPER
	
	Output message
	enpwZWJmeDE9MTQ1NDA0Njg3NA==
	
6) Talk to the ORACLE

	$ telnet xavier.h4x0r.space 9111
	
	Trying 129.74.161.24...
	Connected to xavier.h4x0r.space (129.74.161.24).
	Escape character is '^]'.
	 ________________________ 
	< Hello, who may you be? >
	 ------------------------ 
	       \   ,__,
	        \  (oo)____
	           (__)    )\
	              ||--|| *
	NAME? mmcrosk1
	 ___________________________________ 
	/ Hmm... mmcrosk1?                  \
	|                                   |
	| That name sounds familiar... what |
	\ message do you have for me?       /
	 ----------------------------------- 
	       \   ,__,
	        \  (oo)____
	           (__)    )\
	              ||--|| *
	MESSAGE? enpwZWJmeDE9MTQ1NDA0Njg3NA==
	 ______________________________________ 
	/ Ah yes... mmcrosk1!                  \
	|                                      |
	| You're smarter than I thought. I can |
	| see why the instructor likes you.    |
	|                                      |
	| You met the SLEEPER about 3 minutes  |
	\ ago... What took you so long?        /
	 -------------------------------------- 
	       \   ,__,
	        \  (oo)____
	           (__)    )\
	              ||--|| *
	REASON? I had to go to the bathroom
	 ______________________________________ 
	/ Hmm... Sorry, kid. You got the gift, \
	| but it looks like you're waiting for |
	| something.                           |
	|                                      |
	| Your next life, maybe. Who knows?    |
	\ That's the way these things go.      /
	 -------------------------------------- 
	       \   ,__,
	        \  (oo)____
	           (__)    )\
	              ||--|| *

	Congratulations mmcrosk1! You have reached the end of this journey.
	
	
	
