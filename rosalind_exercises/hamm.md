# Counting Point Mutations
## Problem:
Given two strings s and t of equal length, the Hamming distance between s and t, denoted dH(s,t), is the number of corresponding symbols that differ in s and t. See Figure 2.

Given: Two DNA strings s and t of equal length (not exceeding 1 kbp).
Return: The Hamming distance dH(s,t).

# Code answer:
Goal: Compare the sequences and find the differences, then calculate the number of positions where the two sequences differ. 
Plan: Because both sequences are of the same length, we can directly compare the corresponding positions. Go over every nucleotide of the sequences to get the difference using a for loop. Each time a difference between the characters at the same position in the two sequences is found, we increase a counter by 1. The finished counter is the Hamming distance.


```python
s = "GAGCCT"
t = "CATCGT"
#make an initial distance counter starting with 0
distance = 0

# Iterate over the positions in the strings
for nucleotide in range(len(s)): #for every nucleotide in the range of the DNA string (s and t have the same length)
    if s[nucleotide] != t[nucleotide]: #if the nucleotide in s is not the same as the one in t
        distance += 1  #then the distance is increased by one

print(distance) #print the Hamming distance
```
