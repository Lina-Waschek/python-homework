#!/usr/bin/env python

# Problem ORF - Open Reading Frames

# Description:
# Given: A DNA string s of length at most 1 kbp in FASTA format.
# Return: Every distinct candidate protein string that can be translated from ORFs of s. Strings can be returned in any order.

# Steps:
# read in DNA sequence
# translate to RNA (forward strand)
# reverse complement to RNA (backward strand)
# write a function that finds all ORFs in an RNA sequence
# apply it to the forward strand to find all forward ORFs
# apply it to the backward strand to find all backward ORFs
# combine the list of forward and backward ORFs
# write (or copy) a function that translates an mRNA to a peptide
# go over all ORFs and translate them to peptides


# Code answer:
# 1) translate to RNA and to reverse complement RNA (like in revc exercise)
DNA= "AGCCATGTAGCTAACTCAGGTTACATGGGGATGACCCCGCGACTTGGATTAGAGTCTCTTTTGGAATAAGCCTGAATGATCCGAGTAGCATCTCAG"
complementary_DNA = "" #empty complementary DNA string

def complement(nucleotide): # Map each nucleotide to its complement
    if nucleotide == "A":
        return "T"
    elif nucleotide == "C":
        return "G"
    elif nucleotide == "G":
        return "C"
    elif nucleotide == "T":
        return "A"


for nucleotide in DNA:  # For each nucleotide in DNA
    complementary_DNA += complement(nucleotide)  # Append the complementary nucleotide

# reverse the complementary DNA string
reverse_complementary_DNA = complementary_DNA[::-1]

# get the RNA string
RNA= DNA.replace("T", "U")

# to get the reverse complementary RNA string replace the T with U in the reverse complementary DNA string
reverse_complementary_RNA = reverse_complementary_DNA.replace("T", "U")

codon_table = {
    "UUU": "F",      "CUU": "L",      "AUU": "I",      "GUU": "V",
    "UUC": "F",      "CUC": "L",      "AUC": "I",      "GUC": "V",
    "UUA": "L",      "CUA": "L",      "AUA": "I",      "GUA": "V",
    "UUG": "L",      "CUG": "L",      "AUG": "M",      "GUG": "V",
    "UCU": "S",      "CCU": "P",      "ACU": "T",      "GCU": "A",
    "UCC": "S",      "CCC": "P",      "ACC": "T",      "GCC": "A",
    "UCA": "S",      "CCA": "P",      "ACA": "T",      "GCA": "A",
    "UCG": "S",      "CCG": "P",      "ACG": "T",      "GCG": "A",
    "UAU": "Y",      "CAU": "H",      "AAU": "N",      "GAU": "D",
    "UAC": "Y",      "CAC": "H",      "AAC": "N",      "GAC": "D",
    "UAA": "Stop",   "CAA": "Q",      "AAA": "K",      "GAA": "E",
    "UAG": "Stop",   "CAG": "Q",      "AAG": "K",      "GAG": "E",
    "UGU": "C",      "CGU": "R",      "AGU": "S",      "GGU": "G",
    "UGC": "C",      "CGC": "R",      "AGC": "S",      "GGC": "G",
    "UGA": "Stop",   "CGA": "R",      "AGA": "R",      "GGA": "G",
    "UGG": "W",      "CGG": "R",      "AGG": "R",      "GGG": "G"
}
# find all the ORFs in a RNA sequence
def find_orf(RNA):
    orfs = []
    for i in range(len(RNA)):
        if RNA[i:i+3] == "AUG": #if its the start codon
            for j in range(i, len(RNA), 3): # start from the start codon and move in steps of 3 (one codon at a time)
                codon = RNA[j:j+3] 
                if codon in ["UAA", "UAG", "UGA"]: #if it´s a stop codon
                    orfs.append(RNA[i:j+3]) #append the ORF from the start codon to the stop codon
                    break #stops the loop after the stop codon
    return orfs

# find all the ORFs in the forward and the reverse RNA strand
orf_forward = find_orf(RNA)
orf_reverse = find_orf(reverse_complementary_RNA) 

# translate the mRNA to a protein string
def translate(rna_sequence):
    protein_string = ""
    for i in range(0, len(rna_sequence), 3): #go over the RNA sequence in steps of 3 (each codon)
        codon = rna_sequence[i:i+3] 
        amino_acid = codon_table[codon] #get the corresponding amino acid from the codon table
        if amino_acid == "Stop": # if it´s a stop codon
            return protein_string # the translation ends here and returns the protein string
        protein_string += amino_acid # if its not a stop codon the protein sequence goes on
    return protein_string 
        
# Combine the forward and reverse ORFs, translate them, and add the resulting peptides to a list 
peptides = []
for orf in orf_forward + orf_reverse:
    peptides.append(translate(orf))

peptides = list(set(peptides)) #get rid of duplicate peptides

#print each peptide on a new line
for peptide in peptides:
    print(peptide)



