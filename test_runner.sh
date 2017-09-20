#!/bin/bash
if [ $# -eq 0 ]
then
	for filename in *_datatest.py; do
		echo "~~~~~~~~~~~~~~~~~~~~~~~~~~~~"
		echo "$filename"
		echo "~~~~~~~~~~~~~~~~~~~~~~~~~~~~"
		/usr/bin/env python2 "$filename"
	done
else
	for arg in "$@"
	do
		echo "~~~~~~~~~~~~~~~~~~~~~~~~~~~~"
		echo "$arg"
		echo "~~~~~~~~~~~~~~~~~~~~~~~~~~~~"
		/usr/bin/env python2 "$arg"
	done
fi
