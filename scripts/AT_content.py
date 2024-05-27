#program to print AT content of a given sequence

dna_seq = "ACTGATCGATTACGTATAGTATTTGCTATCATACATATATATCGATGCGTTCAT"

#count A and T content
a_content = dna_seq.count('A')
t_content = dna_seq.count('T')

#calculating AT content
at_content = (a_content + t_content)/len(dna_seq) * 100

#print AT content
print(f"AT Content of the DNA sequence is {at_content}% ")
