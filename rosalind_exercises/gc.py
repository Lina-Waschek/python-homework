#!/usr/bin/env python

from util import read_input

fasta = read_input('../rosalind-data/gc-data.txt')

#make a dictionary with ID (as the key) and sequence (as the value) pairs
sequences = {}  # empty dictionary
current_id = ""
for line in fasta:
    if line[0] == ">":
        #print("This line is a header:")
        header = line
        #print(header)
        current_id = header[1:]
        sequences[current_id] = ""
    else:
        #print("This is a sequence:")
        sequence = line
        #print("We currently belong to sequence", current_id)
        #print(sequence)
        sequences[current_id] += sequence

#print(sequences)

# calculate the GC content for every sequence
gc_content = {}
for seq_id, dna in sequences.items():
    counts = {'A': 0, 'T': 0, 'C': 0, 'G': 0}
    for base in dna:
        counts[base] += 1
    gc = (counts['G'] + counts['C']) / len(dna) * 100 #the gc content in percent
    gc_content[seq_id] = gc

# find the sequence with the maximum GC content
#first define the placeholders for max value and corresponding id:
max_value = 0
max_id = ""
for seq_id, current_gc_value in gc_content.items():
    if current_gc_value > max_value:
        max_value = current_gc_value
        max_id = seq_id

print(max_id)
print(f"{max_value:.6f}") #print the maximum GC content with 6 decimal places
