#!/bin/bash


num=0
input='testcases.txt'
output='TestingCheck4.xsd'

for i in `find -iname "*testcases.txt" `
do
   :
   newArray[$num]=`echo $i | perl -nle 'm/\.\/(.+)testcases\.txt/; print $1'`
   num=$(($num + 1))
done


for i in "${newArray[@]}"
do

        echo $i$input
        echo $i$output
       result=`./txt2xsd.sh $i$input`
	`echo $result > $i$output`
done


