#!/usr/bin/env python

# Strategy:
# 1) Generate the reverse complement strand of the DNA sequence.
# 2) Search for reverse palindromes with lengths between 4 and 12.
# 3) Return the position and length of each palindrome found.

from util import read_fasta
# Read the DNA sequence from a fasta file
DNA = read_fasta('../rosalind-data/revp-data.txt')
#print(DNA)

# 1) Reverse complement strand

# A function to return the complementary base for a given nucleotide
def complement (x):
    if x=="A":
       return "T"
    elif x== "C":
       return "G"
    elif x== "G":
       return "C"
    elif x== "T":
       return "A"

# A function to generate the reverse complement of a given substring
def reverse_complement(substring):
    complement_bases = "" # create an empty string to store the complementary bases
    for base in substring[::-1]: # go over each base in the reversed substring
        complement_bases += complement(base) # append the complementary base to the complement_bases string
    return complement_bases # return the reverse complement DNA sequence


# 2) Search for reverse palindromes

def find_reverse_palindromes(dna):
    results=[]
    for i in range(len(dna)): # go over every start position in the DNA sequence
        for length in range(4, 13): # search for substrings of length between 4 and 12
            if i + length > len(dna): # if the substring is within the bounds of the DNA sequence
                continue
            substring = dna[i:i+length] 
            if substring == reverse_complement(substring): # check if the substring is equal to its reverse complement
                results.append((i + 1, length)) # +1 to get 1 based positions
    return results

# find all reverse palindromes in the DNA sequence
palindromes = find_reverse_palindromes(DNA)

# 3) Print the position and length of each palindrome
for position, length in palindromes:
    print(position, length)


