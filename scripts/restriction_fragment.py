#!/usr/bin/env python3

#simple program to calculate the size of two fragments that are produced when DNA sequence is digested with EcoRI

#recognition site for EcoRI is GAATTC

dna_seq = "ACTGATCGATTACGTATAGTAGAATTCTATCATACATATATATCGATGCGTTCAT"

#find method will locate the start of EcoRI motif
#one is added to account for indexing in python

length_frag1 = dna_seq.find("GAATTC") + 1

#This applies since we only have one EcoRI motif in the DNA sequence

length_frag2 = len(dna_seq) - length_frag1

#printing the lengths of the fragments
print(f'The length of first fragment is: {length_frag1}')
print(f'The length of second fragment is: {length_frag2}')
