#!/bin/bash

# This generates xsd from txt if the txt is newer...

input='testcases.txt'
output='TestingCheck4.xsd'

for file in *$input
do
 xsdfile=$(echo $file | sed "s/$input/$output/")
 if [ $file -nt $xsdfile ]; then
   echo "creating $xsdfile from $file...";
   ./txt2xsd.sh $file > $xsdfile;
   /usr/bin/xmllint --noout --schema ./XMLSchema.xsd $xsdfile;
 fi
done
