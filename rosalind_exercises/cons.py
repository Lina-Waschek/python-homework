#!/usr/bin/env python

from util import read_fasta2
seq = read_fasta2('../rosalind-data/cons-data.txt')

# Profile matrix: tracks how often each nucleotide appears at each position
# first create an empty profile matrix
profile = {'A': [], 'C': [], 'G': [], 'T': []}

for base in profile:
    profile[base]= [0] * len(seq[0])  #make the profile matrix with zeros for all positions in the sequence

# fill the profile matrix with counts for each base at every position
for s in seq: #go over every sequence
    for position, base in enumerate(s): #go over every base and position
        profile[base][position] +=1 #increase the count for the corresponding base and position 


#print the profile dictionary in a matrix format   
for base in profile: #go over the bases in the profile
    matrix = f"{base}: "
    for count in profile[base]: #go over the numbers of the bases in every position
        matrix += f"{count} "
    print(matrix.strip())  #print the counts as a row for the current nucleotide


# Consensus sequence: the most common nucleotide at each position in the sequence
consensus="" #make an empty variable for the consensus sequence

for i in range(len(seq[0])): #go over each position in the sequences
    max_base= "" #make an empty variable for the most common base
    max_count= -1 #make the maximum count to a value lower than possible counts

    for base in profile: #check each nucleotide in the profile matrix
        if profile[base][i] > max_count: #if this nucleotide's count is higher than the current maximum
            max_base= base #then update the most common nucleotide
            max_count= profile[base][i] #and also update the maximum count

    consensus += max_base #append the most common nucleotide to the consensus sequence

print(consensus)
