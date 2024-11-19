# Computing GC Content

## Problem: 
Given: At most 10 DNA strings in FASTA format (of length at most 1 kbp each).
Return: The ID of the string having the highest GC-content, followed by the GC-content of that string.

### Code Answer:
```python
# reads the file and give back a line by line string
def read_input(filepath):
    with open(filepath, 'r') as infile:
        lines = infile.readlines()
        stripped = []
        for line in lines:
            stripped.append(line.strip())
    return stripped

# or
from util import read_input 


# function that makes a dictionary out of the fasta data (ID as a key and sequence as a value)
def fasta (fasta_data):
    sequences={} # empty dictionary
    id="" # empty variable for the ID

    for line in fasta_data: # for every line in fasta_data 
        if line[0] == ">": #if the line starts with > it is an ID
            id= line [1:] # save the ID but without the >
            sequences[id] = "" #empty sequence
        else: #if its not an ID line
            sequences[id] += line.strip() #put the sequence to the ID

    return sequences

# calculate the GC content

def calculate_gc_content(sequence):
    gc_count = sequence.count("C") + sequence.count("G")  # .count counts how often "C" und G" is in the sequence
    return (gc_count / len(sequence)) * 100 #calculate it in percent



# find the highest GC content: return the highest GC content and the ID of the sequence with the highest GC content 
def find_highest_gc_content(filepath):
    
    fasta_lines = read_input(filepath)  
    sequences = fasta(fasta_lines) 
    
    highest_gc_id = None #the id of the sequence with the highest GC content is set to None, which means no varaible yet
    highest_gc_content = 0 # initial value is 0
    
    for seq_id, sequence in sequences.items():
        gc_content = calculate_gc_content(sequence)  # calculate the GC content with the function calculate_gc_content
        if gc_content > highest_gc_content:  # if the current GC content is bigger than the current highest GC content
            highest_gc_id = seq_id #then the highest GC content is set to the current sequence ID
            highest_gc_content = gc_content #and the highest_gc_content is set to current biggest GC content
    
    return highest_gc_id, highest_gc_content

#print the answer
file_path = "./rosalind-data/gc-test.txt"
result_id, result_gc = find_highest_gc_content(file_path)
print(result_id)
print(result_gc)  

```

