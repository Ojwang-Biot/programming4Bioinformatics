#!/usr/bin/env python3

#program to create multiple fasta files

#creating variables to store headers

h1 = "ABC123"
h2 = "DEF456"
h3 = "HIJ789"

#creating variable to store the sequences

seq1 = "ATCGTACGATCGATCGATCGCTAGACGTATCG"
seq2 = "actgatcgacgatcgatcgatcacgact"
seq3 = "ACTGAC-ACTGT--ACTGTA----CATGTG"

#writing the first sequence

file1 = open(h1 + ".fasta", "w")
file1.write('>' + h1 + '\n' + seq1)

#writing second sequence
file2 = open(h2 + ".fasta", "w")
file2.write('>' + h2 + '\n' + seq2.upper())

#writing the third sequence
file3 = open(h3 + ".fasta", "w")
file3.write('>' + h3 + '\n' + seq3.replace("-", ""))

#closing the files
file1.close()
file2.close()
file3.close()

#let's see if it has created the files successfully

print("files successfully created")
