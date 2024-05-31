#!/usr/bin/env python3

#given a file with genomic dna and a file with a list of start/stop positions of exons on separate lines

#this program will extract the exon segments, concatenate them, and write them to a new file

#open genomic DNA file
genomic_dna = open("/home/genejuggler/Desktop/programming_bioinfo/programming4Bioinformatics/datasets/python_for_biologists_excer/lists_and_loops/exercises/genomic_dna.txt").read()

#open exon file
exons_file = open("/home/genejuggler/Desktop/programming_bioinfo/programming4Bioinformatics/datasets/python_for_biologists_excer/lists_and_loops/exercises/exons.txt")

#open the filr to write into
file = open("exons_from_genomic_DNA.txt", "w")

#creating variable to store the coding sequence once extracted
coding_seq = ""

#iterating over the exon file
for line in exons_file:
	
	#split line using comma delimiter
	exon_position = line.split(',')
	
	#extract start and stop positions
	start = int(exon_position[0])
	stop = int(exon_position[1])
	
	#extract the exon from genomic DNA
	exon = genomic_dna[start:stop]
	
	#add the exon to the end of the current coding sequence
	coding_seq = coding_seq + exon
	
	#writing the exons to a new file
	file.write(coding_seq)
	
file.close()


print("extraction successful")
		
