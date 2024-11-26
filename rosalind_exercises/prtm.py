#!/usr/bin/env python

#  Problem PRTM - Calculating Protein Mass

# Description: 
# Given: A protein string P of length at most 1000 aa.
# Return: The total weight of P. Consult the monoisotopic mass table.

# Instructions:
# 1. read the data
# 2. define the dictionary (key: amino acid one letter code, value: mass in Da)
# 3. (actual solution):
#   - define a counter variable, total_weight, and set it to 0
#   - loop over the input,
#   - for the current amino acid, take the value from the dictionary, and add it to total_weight
#   
#   print total_weight

# Code Answer:
p= "SKADYEK" #protein string
total_weight= 0

amino_acid_masses = {
    "A": 71.03711,
    "C": 103.00919,
    "D": 115.02694,
    "E": 129.04259,
    "F": 147.06841,
    "G": 57.02146,
    "H": 137.05891,
    "I": 113.08406,
    "K": 128.09496,
    "L": 113.08406,
    "M": 131.04049,
    "N": 114.04293,
    "P": 97.05276,
    "Q": 128.05858,
    "R": 156.10111,
    "S": 87.03203,
    "T": 101.04768,
    "V": 99.06841,
    "W": 186.07931,
    "Y": 163.06333
}

for amino_acid in p:
    if amino_acid in amino_acid_masses:
        total_weight += amino_acid_masses[amino_acid]

print(total_weight)

