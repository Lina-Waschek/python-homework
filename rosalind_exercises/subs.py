# Problem SUBS - Finding a Motif in DNA

# Description:
# Given: Two DNA strings s and t (each of length at most 1 kbp).
# Return: All locations of t as a substring of s.

# Strategy: 
# 1) Check s for t at every possible starting position using a loop.
# 2) Test if the substring of s matches t by slicing.

# Code answer:

s= "GATATATGCATATACTT" # DNA string
t= "ATAT" # substring to find in s

locations= "" # create an empty string to store the locations 
for start in range(0, len(s)): # go over every position of s
    if s[start:start + len(t)] == t: #if the substring of s matches t
        locations += str(start+1) + " " # convert the starting number to a string and add the starting position (+1 for 1-based numbering) with a space to the locations string

print(locations.strip())