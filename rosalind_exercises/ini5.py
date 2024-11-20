#!/usr/bin/env python

from util import read_input 

#first read the file
    
filepath = "../rosalind-data/ini5-data.txt"
with open(filepath, 'r') as infile:
    lines = infile.readlines()
    for line in lines:
        print(line.strip())

#print only even-numbered lines

for line in lines[1::2]:
    print(line.strip())

