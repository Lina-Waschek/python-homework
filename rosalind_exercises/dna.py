DNA = "AGCTTTTCATTCTGACTGCAACGGGCAATATGTCTCTGTGTGGATTAAAAAAAGAGTGTCTGATAGCAGC"
nucleotide_count = {'A': 0, 'C': 0, 'G': 0, 'T': 0} #set the initial counts for each nucleotide (A, C, G, T) to 0

for nucleotide in DNA: #for every nucleotide in the DNA
    if nucleotide in nucleotide_count: #if the nucleotide is in the nucleotide_count (it always will because we predefined it)
        nucleotide_count[nucleotide] += 1 #then increase the count for this nucleotide by 1

print(nucleotide_count['A'], nucleotide_count['C'], nucleotide_count['G'], nucleotide_count['T']) #print the nucleotide count for every nucleotide
