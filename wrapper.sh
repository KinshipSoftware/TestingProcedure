#!/bin/bash

input='testcases.txt'
output='TestingCheck4.xsd'

for file in *$input
do
 xsdfile=$(echo $file | sed "s/$input/$output/")
 echo "creating $xsdfile from $file..."
 ./txt2xsd.sh $file > $xsdfile
done
