#!/usr/bin/env python

# Strategy:
# Create a dictionary where the FASTA ID is the key and the sequence is the value.
# Then compare each pair of sequences to check for overlaps.

from util import fasta_pair

fasta_dict = fasta_pair('../rosalind-data/grph-data.txt')
#print(fasta_dict)

k = 3  # k is the length of the overlap, defined as 3 in this case

# compare each pair of sequences to check for overlaps.
for name1, seq1 in fasta_dict.items():  # for each name and sequence in the fasta_dict
    for name2, seq2 in fasta_dict.items():  # for every other name and sequence
        if name1 != name2:  # ensure the current name and the next name are not the same
            if seq1[-k:] == seq2[:k]:  # check if the last k bases of seq1 match the first k bases of seq2
                print(name1, name2)  # if they match, print the two names