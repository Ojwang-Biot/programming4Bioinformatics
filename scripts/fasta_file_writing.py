#!/usr/bin/env python3

#program to create a FASTA file for three sequences


#sequence headers
h1 = "ABC123"
h2 = "DEF456"
h3 = "HIJ789"

#DNA sequences corresponding to the sequence headers
s1 = "ATCGTACGATCGATCGATCGCTAGACGTATCG"
s2 = "actgatcgacgatcgatcgatcacgact".upper()
s3 = "ACTGAC-ACTGT--ACTGTA----CATGTG".replace('-', '')

#create a file
fasta_file = open("fasta_dummy.txt", "w")

#write the file

fasta_file.write('>' + h1 + '\n' + s1 + '\n')
fasta_file.write('>' + h2 + '\n' + s2 + '\n')
fasta_file.write('>' + h3 + '\n' + s3 + '\n')

fasta_file.close()

print("Succefully created")


