#!/usr/bin/env python

# Strategy:
# 1) Cut out the intron substrings from the main DNA string 
# 2) Convert the resulting DNA string to RNA (see rna.py), then read in codons and translate to amino acids (like prot.py)

from util import fasta_pair
# Function to extract the main DNA sequence and introns from the FASTA file
def get_main_dna_and_introns(filepath):
    sequences = fasta_pair(filepath)
# separate the main DNA sequence and the introns
    headers = list(sequences.keys())
    main_dna = sequences[headers[0]]  # first label is the main DNA
    introns = [sequences[header] for header in headers[1:]]  # remaining are introns
    return main_dna, introns

main_dna, introns = get_main_dna_and_introns('../rosalind-data/splc-data.txt')

#print(main_dna)
#print(introns)

# Function to remove introns from the main DNA sequence    
def remove_introns(dna, introns):
    for intron in introns: # loop through each intron
        dna = dna.replace(intron, "") # remove the intron from the DNA string
    return dna # return the DNA sequence without introns
        
# Function to transcribe the DNA to RNA
def transcribe_to_rna(dna):
    RNA = ""  # Initialize RNA variable
    for nucleotide in dna:  # for every nucleotide in DNA
        if nucleotide == "T":  # if the nucleotide is a "T"
            RNA += "U"  # replace it with "U" in the RNA string
        else:  # if the nucleotide is not a T
            RNA += nucleotide  # keep the nucleotide unchanged in the RNA string
    return RNA  # Return RNA after loop

# Codon table for translation from RNA to protein   
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

# Function to translate RNA sequence to a protein sequence
def translate_rna_to_protein(rna, codon_table):
    protein = "" # empty string for the protein
    for i in range(0, len(rna), 3): # process RNA in triplets (codons)
        codon = rna[i:i+3] # extract the current codon
        amino_acid = codon_table.get(codon, "") # get the corresponding amino acid from the codon table
        if amino_acid == "Stop": # if codon is a stop codon, end the translation
            break
        protein += amino_acid # add the amino acid to the protein sequence
    return protein

exons_only = remove_introns(main_dna, introns)
RNA = transcribe_to_rna(exons_only)
protein_string = translate_rna_to_protein(RNA, codon_table)

print(protein_string)