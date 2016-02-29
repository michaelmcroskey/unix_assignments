# **awk.md** 

**1.** Printing specific fields.

- Prints the second field in dogs.txt
	
		awk '{ print $2 }' dogs.txt

- Print the second field, then the first field in dogs.txt
	
		awk '{ print $2, $1; }' dogs.txt


**2.** Modifying FS to control input field separator.

To delimit the fields by a certain character, use the **FS** variable.

- Print out the third field, delimiting by a comma

		awk 'BEGIN { FS = ","}; { print $3 }' dogs.txt

- Find all of the second fields that are empty.  Here it is searching for ""
	
		awk -F: '$2 == ""' /etc/passwd

- Search through file delimited by tabs ("[ \t]+") and print the second field

		awk 'BEGIN { FS = "[ \t]+" } ; { print $2 }' dogs.txt
	

**3.** Using BEGIN and END.

BEGIN and END are search parameters that match before and after the document has been processed

- The BEGIN keyword is like echo

		awk 'BEGIN { print "My dog is Hobbes"; }'
	
- Search the file for all third fields and print that they have been found
	
		awk 'BEGIN { print $3; }
		> END { print "All third fields successfully printed!\n-----"; }' dogs.txt

- To print out the number of times a word (Beagle) occurs in a file, one can use the BEGIN and END keywords/

		awk '
		> BEGIN { print "Appearance of \"Beagle\"" }
		> /Beagle/ { ++n }
		> END   { print "\"Beagle\" appears " n " times." }' dogs.txt

**4.** Using pattern matching.

- Print the second field of every first field that is "Hobbes" (my dog)

		awk '$1 == "Hobbes" { print $2 }' dogs.txt
	
- Print all records that do not contain the string "Hobbes"

		awk '! /Hobbes/' dogs.txt

**5.** Using special variables such as NF and NR.

- NF - total number of fields per record

		awk '{print NR,"->",NF}' dogs.txt

- NR - total number of records in a file

		awk '{print "Processing Record - ",NR;}END {print NR, "Records processed";}' dogs.txt

**6.** Using associative arrays.

Syntax:

	arrayName[string]=value
		
- Looping through an associative array:

		awk '{
		> data[$3]++;
		> }
		> END{
		> for (var in data)
		> print var, "is associated with", data[var]"
		> }
		> ' data.txt

- Remove duplicate and clean up:

		awk '!($0 in array) { array[$0]; print }' dogs.txt