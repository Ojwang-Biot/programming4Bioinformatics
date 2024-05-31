#!/usr/bin/env python3

#program to trim adapter sequences given a file of DNA sequences, and writing the cleaned sequences to a new file. Also print the length of each sequence

#open the file to use the content

dna_file = open("/home/genejuggler/Desktop/programming_bioinfo/programming4Bioinformatics/datasets/python_for_biologists_excer/lists_and_loops/exercises/input.txt")

#create th file to wite on

trimmed_seq = open("trimmed_seq.txt", "w")

#loop through the dna_file and write in the trimmed_seq file

for dna in dna_file:
	
	#trim the sequences to remove adapters
	trimmed_dna = dna[15:-1]
	
	#write the trimmed sequences in a new file
	trimmed_seq.write(trimmed_dna)
	
	#calculate the length of the sequences
	seq_len = len(trimmed_dna)
	
	#print the length to the screen
	print(f'processed sequence with length {seq_len}')
	
#print sequence length on the screen

dna_file.close()
trimmed_seq.close()
	
print("trimming successfully")
