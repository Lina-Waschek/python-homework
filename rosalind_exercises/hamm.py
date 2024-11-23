#!/usr/bin/env python

# Problem HAMM - Counting Point Mutations

# Description:
# Given: Two DNA strings s and t of equal length (not exceeding 1 kbp).
# Return: The Hamming distance dH(s,t).

# Code answer:

s = "GAGCCTACTAACGGGAT"
t = "CATCGTAATGACGGCCT"
#make an initial distance counter starting with 0
distance = 0

# Iterate over the positions in the strings
for nucleotide in range(len(s)): #for every nucleotide in the range of the DNA string (s and t have the same length)
    if s[nucleotide] != t[nucleotide]: #if the nucleotide in s is not the same as the one in t
        distance += 1  #then the distance is increased by one

print(distance) #print the Hamming distance