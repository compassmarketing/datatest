#!/bin/bash
for filename in *_datatest.py; do
	echo "~~~~~~~~~~~~~~~~~~~~~~~~~~~~"
	echo "$filename"
	echo "~~~~~~~~~~~~~~~~~~~~~~~~~~~~"
	/usr/bin/env python2 "$filename"
done
