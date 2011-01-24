#!/bin/bash
#
# Bash script to generate a Arbil test XSD (XML) file from a plain text testcases file
# ignores comments and whitespace in the testcases file
#
# plain text file format:
#
# NodeSearchTest
#
#   OpenSearchWindow "From the local corpus tree right click and select search; a search window should be shown."
#   LocalSearch      "From the local corpus tree right click and select search; enter [...]"
#
# -Nodes are one word per line
# -Tests are [space] (at least one), plus one word, plus an expression in "quotation marks"
#
# Version 1.1 / Vlado Plaga 2010-11-25

testcasesfile=$1;

doctype='<?xml version="1.0" encoding="utf-8"?>';

fileheader='
<xs:schema elementFormDefault="qualified" xmlns:xs="http://www.w3.org/2001/XMLSchema" xmlns:ann="http://www.clarin.eu">

    <xs:element name="BugCheck">

        <xs:complexType>

            <xs:sequence>

                <xs:element name="DateTime" type="xs:string" maxOccurs="1" minOccurs="1" ann:documentation="The date time the test was started" ann:displaypriority="1"/>

                <xs:element name="ProgramVersion" type="xs:string" maxOccurs="1" minOccurs="1" ann:documentation="The version of the application being tested" />

                <xs:element name="OSVersion" type="xs:string" maxOccurs="1" minOccurs="1" ann:documentation="The operating system type and version being tested on" />

';

testfooter='                            <xs:element name="ErrorDescription" maxOccurs="unbounded" minOccurs="1" type="xs:string" ann:documentation="Description of errors in this test node. Can exist multiple times." />

                        </xs:sequence>

                    </xs:complexType>

                </xs:element>
';

testresults='    <xs:simpleType name="TestResult">

        <xs:restriction base="xs:string">

            <xs:enumeration value="Works" />

            <xs:enumeration value="Mostly" />
            
            <xs:enumeration value="Strange" />
            
            <xs:enumeration value="Fails" />

        </xs:restriction>

    </xs:simpleType>
';


testheader='                    <xs:complexType>

                        <xs:sequence>
';


sequencefooter='            </xs:sequence>

        </xs:complexType>

    </xs:element>
';

# boolean variable to make sure tags are closed with $testfooter
insidetest=false;

echo "$doctype";
echo;
echo "<!-- This file is generated from $testcasesfile! Modifications will be lost when regenerated! -->";

echo "$fileheader";

while read line; do
  # ignore empty and comment lines
  if [[ $line != "" && ! $(echo $line | grep " *#" ) ]]; then 
    if [[ $line == *\ * ]]; then # Subtest lines start with at least one space
      insidetest=0; # "0" is "true" for bash
      element="$(echo $line | sed s/\ .*//)";
      annotation="$(echo $line | sed -e s/$element// -e s/\ *//)";
      echo "                            <xs:element name=\"$element\" maxOccurs=\"1\" minOccurs=\"1\" ann:documentation=$annotation type=\"TestResult\" />";
      echo;
    else
      if [ "$insidetest" == "0" ]; then
        echo "$testfooter";
      fi;
      insidetest=false;
      echo "                <xs:element name=\"$line\" minOccurs=\"1\" maxOccurs=\"unbounded\">";
      echo;
      echo "$testheader";
    fi
  fi
done < $testcasesfile

echo "$testfooter";

echo "$sequencefooter";

echo "$testresults";

echo "</xs:schema>";
