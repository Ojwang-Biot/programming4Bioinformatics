#!/usr/bin/env python3

#example of reading and writing a file
# program to split genomic DNA into coding and non-coding parts, and writing the sequences to two separate files

# open the file
file = open("/home/genejuggler/Desktop/programming_bioinfo/programming4Bioinformatics/datasets/python_for_biologists_excer/reading_files/exercises/genomic_dna.txt", "r")

#read the file content
sequence = file.read().rstrip()

#spliting the sequences
#getting the coding strand
exons_file = sequence[0:63] + sequence[90:-1]

#getting non-coding
introns_file = sequence[63:91]

#writing DNA coding region
coding_file = open("exons.txt", "w")

coding_file.write(exons_file)


#writing DNA non-coding region
noncoding_file = open("introns.txt", "w")

noncoding_file.write(introns_file)

file.close()

print("successful")

