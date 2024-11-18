# a function to return the complementary base for a given nucleotide
def complement (x):
    if x=="A":
        return "T"
    elif x== "C":
        return "G"
    elif x== "G":
        return "C"
    elif x== "T":
        return "A"

DNA="AAAACCCGGT"
com_DNA="" #define an empty string for the complementary DNA

# Create the complementary DNA string
for nucleotide in DNA: #for every nucleotide in DNA
    com_DNA+= complement(nucleotide) #append the complementary nucleotide to com_DNA

# Reverse the complementary DNA string to get the reverse complement
rev_DNA= com_DNA[::-1]

print(rev_DNA)



