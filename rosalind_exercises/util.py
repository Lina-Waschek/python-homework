# a library of utility functions for Rosalind exercises

def read_input(filepath):
    with open(filepath, 'r') as infile:
        lines = infile.readlines()
        stripped = []
        for line in lines:
            stripped.append(line.strip())
    return stripped


# This function reads a FASTA file from a given filepath and returns
# the concatenated DNA sequence as a single string, ignoring the header lines.

def read_fasta(filepath):
    with open(filepath, 'r') as infile:
        lines = infile.readlines()
    
    dna_sequence = ""
    for line in lines:
        if line.startswith(">"):  # If the line starts with a ">", it's a header line, so we skip it
            continue  
        # For other lines (which contain the DNA sequence), remove any leading/trailing spaces or newlines
        # and append the result to the dna_sequence string
        dna_sequence += line.strip()  
    return dna_sequence



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


# make a dictionary with ID (as the key) and sequence (as the value) pairs
def fasta_pair(filepath):
    sequences = {}  # empty dictionary
    current_id = ""

    # read the file line by line
    with open(filepath, 'r') as file:
        for line in file:
            line = line.strip()  # remove unnecessary whitespace and line breaks
            if line.startswith(">"):
                # this line is a header
                header = line
                current_id = header[1:]  # remove the ">" to get the ID
                sequences[current_id] = ""  # initialize an empty sequence for this ID
            else:
                # this is a sequence
                sequence = line
                sequences[current_id] += sequence  # append the sequence to the current ID
    
    return sequences

