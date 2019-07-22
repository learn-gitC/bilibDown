#!/bin/bash
for line in `cat url_list_un`
do
	echo $line
	you-get $line
done
