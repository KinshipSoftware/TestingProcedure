#!/usr/bin/python
# Author: Peter Withers
# Date: 2014/09/20

import sys
import time
import os

testCasesFile = 'KinOathtestcases.txt'

outputFileName = time.strftime("KinOath-Testing-Worksheet-%Y-%m-%d.md")

outputFile = open(os.path.join("reports", outputFileName), 'w')
with open(testCasesFile) as testPlan:
    for line in testPlan.readlines():
        #print line;
        if line.startswith('#'):
            outputFile.write(line[1:]);
            outputFile.write("\n");
        elif line.startswith('  '):
            #outputFile.write(line);
            parts = line[2:].split(" ", 1);
            outputFile.write("##" + parts[0]);
            outputFile.write("\n");
            outputFile.write(parts[1]);
            #outputFile.write("\n");
            outputFile.write("* Works");
            outputFile.write("\n");
            outputFile.write("* Kind of works");
            outputFile.write("\n");
            outputFile.write("* Doesn't work");
            outputFile.write("\n");
            outputFile.write("\n");
        else:
            outputFile.write("#" + line);
            outputFile.write("\n");
exit(0)
