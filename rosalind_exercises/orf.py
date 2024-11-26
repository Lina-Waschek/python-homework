#!/usr/bin/env python

# Problem ORF - Open Reading Frames

# Description:
# Given: A DNA string s of length at most 1 kbp in FASTA format.
# Return: Every distinct candidate protein string that can be translated from ORFs of s. Strings can be returned in any order.

# Strategy:
# 1) first we need the reverse complement rna string of the dna string before translating it to protein strings (like in revc exercise)
# 2) definde the reading frame by defining start codon and stop codon and then read the codons in between and append them into a protein string 
# 3) for the translation we need the codon table again


# Code idea (not the finished code):
# 1) reverse complement the DNA string and then replace T with U to get the RNA string (like in revc exercise)
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

def translate_rna_to_protein(rna):
    proteins = []  # emty list for proteins
    protein = ""
    
    for start in range(0, len(rna), 3):  # go through all codons in steps of 3
        codon = rna[start:start + 3]
        amino_acid = codon_table[codon]  # get the amino acid for the codon
        
        if codon == "AUG":  # if its the start codon 
            protein = "M"  # begin the protein with M 
        
        elif amino_acid == "Stop" :  # if it is a stop codon
            proteins.append(protein)  # append the protein     
        
        elif protein:  
            protein += amino_acid
    
    return proteins

 
proteins = translate_rna_to_protein(reverse_complementary_RNA)

print(proteins)