#!/bin/bash
for line in `cat url_list`
do
	echo $line
	start you-get $line
done
