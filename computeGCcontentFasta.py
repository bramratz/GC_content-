#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Given a file in Fasta format, computes GC content as a 
percentage for each sequence in the file.
ID with GC percentage are printed out to the terminal

Created on Mon Jun  8 15:57:14 2020

@author: bram
"""

# Import modules
import sys, re
from collections import defaultdict

# Determine the total number of lines in the file 
lineCount = 0 # initialize line count 
with open(sys.argv[1], 'r') as f:
    for line in f:
        lineCount += 1 # For each l;ine increase count by 1

# Regex to capture sequence ID
ID = re.compile(r'^>Rosalind_\d{4}')

# Dictionary to hold GC content associated with each ID
GCcontentDict = defaultdict(list)

# Starting variables 
currentID = None    # Current ID
numC = 0            # Number of C's in a line
numG = 0            # Number of G's in a line 
stringLen = 0       # Number of characters in a line 
numLines = 0        # Current number of lines 

with open(sys.argv[1]) as file:
    for line in file.readlines(): # Read each file line by line
        # Capture first ID in file 
        if currentID == None and ID.search(line):
            currentID = line.split('>')[1] # Set ID as currentID
            numLines += 1 
        # If ID is in the line but its not the first ID compute GC 
        # content then capture the next ID
        elif ID.search(line):
            GCcontent = ((numC + numG) / stringLen) * 100 # GC content
            GCcontentDict[currentID] = GCcontent # Save to dict
            
            # Reset Variables 
            numC = 0
            numG = 0
            stringLen = 0
            
            # Capture the new ID
            currentID = line.split('>')[1]
            numLines += 1 
        # Compute GC calculation for the last ID if last line of file
        # reached 
        elif numLines == (lineCount - 1):
            # Calculate the number of G's and C's
            numC += str(line).count("C")
            numG += str(line).count("G")
            for i in line: # Calculate the total number of characters 
                if i == "\n":
                    continue # Skip new line characters
                else:
                    stringLen += 1
            
            GCcontent = ((numC + numG) / stringLen) * 100 #GC content
            GCcontentDict[currentID] = GCcontent # Save to dict
        # Find the number of G's, C's, and total number of characters in 
        # a line
        else:
            # Calculate the number of G's and C's
            numC += str(line).count("C")
            numG += str(line).count("G")
            for i in line: # Calculate the total number of characters
                if i == "\n":
                    continue # Skip new line characters
                else:
                    stringLen += 1
            numLines += 1

for k, v in GCcontentDict.items():
    print(k, v)