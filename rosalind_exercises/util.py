# a library of utility functions for Rosalind exercises

def read_input(filepath):
    with open(filepath, 'r') as infile:
        lines = infile.readlines()
        stripped = []
        for line in lines:
            stripped.append(line.strip())
    return stripped



# This function reads a FASTA file and extracts the sequences, combining multi-line sequences into single strings.
# Each complete sequence is stored as an individual element in a list. 

def read_fasta2(filepath):
    with open(filepath, 'r') as infile:
        lines = infile.readlines()
        seq = []  
        current_sequence = ""  
        for line in lines:
            line = line.strip()  
            if line.startswith('>'):  
                if current_sequence:  
                    seq.append(current_sequence)
                current_sequence = ""  
            else:
                current_sequence += line  
        if current_sequence:  
            seq.append(current_sequence)
    return seq  