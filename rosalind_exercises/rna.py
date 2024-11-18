DNA="GATGGAACTTGACTACGTAAATT"
RNA =""
for nucleotide in DNA: #for every nucleotide in DNA
    if nucleotide == "T": #if the nucleotide is a "T"
        RNA+="U" #then replace it with a "U" in the RNA string
    else: #if the nucleotide is not a T
       RNA+=nucleotide #keep the nucleotide unchanged in the RNA string

print(RNA)