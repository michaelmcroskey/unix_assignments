#!/bin/sh

curl -s ${1:-'http://catalog.cse.nd.edu:9097/query.text'} | awk '
	/^cpus/ { count=count + $2 };
	END{ print "Total CPUs: " count }'

curl -s ${1:-'http://catalog.cse.nd.edu:9097/query.text'} | awk '
	/^name/ { print $2 }' | uniq | awk '{ print "Total Machines: " NR }' | tail -1 
	
curl -s ${1:-'http://catalog.cse.nd.edu:9097/query.text'} | awk '
	/^type/ { arrayOfTypes[$2]++ };
	END{ for (i in arrayOfTypes) print arrayOfTypes[i], i }' | sort -nr | head -1 | awk '{ print "Most Prolific Type: " $2 }' 