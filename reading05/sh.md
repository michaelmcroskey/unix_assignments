EXAMPLES
========

1) variables
------------

	echo "USER is 	 "	$USER
	# prints the USER variable

2) capturing STDOUT
-------------------

	myecho=$(echo hello)
	$myecho

	# saves "hello" into $myecho

3) if statement
---------------

	if [ "$(uname)" = 'Linux' ]
		then
			echo Tux
	fi

4) case statement
-----------------

	CAR="honda"

	case "$CAR" in
	   "honda") echo "Car is Honda" 
	   ;;
	   "ford") echo "Car is Ford" 
	   ;;
	   "toyota") echo "Car is Toyota"  
	   ;;
	esac

5) for loop
-----------

	for i in "$@"
	do
	  echo Hello, $i!
	done

6) while loop
-------------

	y=1
	while [ $y -le 5 ]
	do
	  echo "Hello $y times"
	  y=$(( $y + 1 ))
	done

7) function
-----------

	lines () {
		cat $1 | wc -l
	}
	numLines=$( lines $1 )
	echo "The file $1 has $numLines lines in it."
	

8) trap
-------

	function finish {
	  rm -rf mktemp -d -t tmp
	}
	trap finish EXIT
	
	