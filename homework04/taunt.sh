#!/bin/bash

export PATH=$PATH:/afs/nd.edu/user15/pbui/pub/bin
sleep="/bin/sleep"

cowNap=0
cowthink "Hello there I'm Moo the cow."

chickfila(){
	cowthink "Eat more chickn!"
	cowNap=1
	exit 1
}

sirloin(){
	cowthink "My grandfather was a knight named Sir Loin"
	cowNap=1
	exit 1
}

for i in {1..10}
	do
	  $sleep 1s
		trap chickfila SIGINT SIGTERM
		trap sirloin SIGHUP
	done
	
if (cowNap=1)
	then
	cowthink "Taking too long, time for a cow nap"
fi



