#!/usr/bin/env python3

#in this example I used data.csv file from python for biology book. In the file, each line contains species name, sequence, gene name, expression level

# program to print out the gene names for all genes belonging to Drosophila melanogaster or Drosophila simulans

#open the file containing the data 

file = open("/home/genejuggler/Desktop/programming_bioinfo/programming4Bioinformatics/datasets/python_for_biologists_excer/conditional_tests/exercises/data.csv")

#iterate through the file line by line
for line in file:

	#split the variables column-wise to make a list for easy manipulation
	variable = line.rstrip().split(',')
	
	#let's name the different columns
	
	species = variable[0]
	sequence = variable[1]
	gene_name = variable[2]
	expression_level = variable[3]
	
	#print the gene names based on the stated condition
	if species == 'Drosophila melanogaster' or species == 'Drosophila simulans':
		print(f'{species}: {gene_name}')
	
file.close()

#part2: print out the gene names of all genes between 90 and 110 bases long

#open file

print() # prints a new line

print("printing out the gene names of all genes between 90 and 110 bases long")

print()

data = open("/home/genejuggler/Desktop/programming_bioinfo/programming4Bioinformatics/datasets/python_for_biologists_excer/conditional_tests/exercises/data.csv")

#iterate through the data
for line in data:
	
	#make a list of the variable
	variable = line.rstrip().split(',')
	
	#name the columns
	species = variable[0]
	sequence = variable[1]
	gene_name = variable[2]
	expression = variable[3]
	
	#determine length of the sequence
	seq_len = len(sequence)
	
	#condition
	if seq_len > 90 and seq_len < 110:
		print(f'sequence length is {seq_len}: gene name: {gene_name}')
		
file.close()

print()

#Part3
print("Print out the gene names for all genes whose AT content is less than 0.5 and whose expression level is greater than 200")

print()

data = open("/home/genejuggler/Desktop/programming_bioinfo/programming4Bioinformatics/datasets/python_for_biologists_excer/conditional_tests/exercises/data.csv")

for line in data:
	
	#make a list of the variable
	variable = line.rstrip().split(',')
	
	#name the columns
	species = variable[0]
	sequence = variable[1]
	gene_name = variable[2]
	expression = variable[3]
	
	#determine length of the sequence
	seq_len = len(sequence)
	
	#at_content
	a_count = sequence.upper().count('A')
	t_count = sequence.upper().count('T')
	
	at_content = (a_count + t_count)/seq_len
	
	#condition
	if at_content < 0.5 and int(expression) > 200:
		print(f'gene name: {gene_name} AT content: {at_content} expression level: {expression}')
	
file.close()
	
	


















