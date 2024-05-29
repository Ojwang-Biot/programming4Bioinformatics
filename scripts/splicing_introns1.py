#!/usr/bin/env python3

#program to print the coding regions of DNA suequence after splicing out introns

dna_seq = "ATCGATCGATCGATCGACTGACTAGTCATAGCTATGCATGTAGCTACTCGATCGATCGATCGATCGATCGATCGATCGATCGATCATGCTATCATCGATCGATATCGATGCATCGACTACTAT"

#1st exon runs from start to 63rd base

exon1 = dna_seq[0:63]
        
#2nd exon runs from 90th base to the end of the sequence

exon2 = dna_seq[90:-1]

#concatenate the two exons to make a continous coding region

coding_reg = exon1 + exon2

print(f'The coding regions of the DNA sequence is: {coding_reg}')

#program to calculate what percentage is coding

percent_coding = len(coding_reg) / len(dna_seq) * 100

print(f'DNA sequence coding is: {percent_coding}%')

#program to print the original genomic DNA sequence with coding bases in uppercase and non-coding in lowercase

intron = dna_seq[63:91].lower()

print(exon1 + intron + exon2)


