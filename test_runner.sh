#!/bin/bash

failcount=0
if [ $# -eq 0 ]
then
	for filename in *_datatest.py; do
		echo "~~~~~~~~~~~~~~~~~~~~~~~~~~~~"
		echo "$filename"
		echo "~~~~~~~~~~~~~~~~~~~~~~~~~~~~"
		
		if ! /usr/bin/env python2 "$filename"
		then
			let failcount++
		fi
	done
else
	for arg in "$@"
	do
		echo "~~~~~~~~~~~~~~~~~~~~~~~~~~~~"
		echo "$arg"
		echo "~~~~~~~~~~~~~~~~~~~~~~~~~~~~"

		if ! /usr/bin/env python2 "$arg"
		then
			let failcount++
		fi
	done
fi

exit $failcount
