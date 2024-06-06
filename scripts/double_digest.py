#given a file containing a DNA sequence, this program will predict the fragment length of digesting the  sequence with two made-up restriction enzymes AbcI whose recognition site is ANT*AAT, and AbcII, recognition site GCRW*TG
# asterisks indicate the position of the cut site
#N represents anybase while W represents A or T and R represents A or G 


#load regular expression module
import re

#open the file and read it 
data = open("/home/genejuggler/Desktop/programming_bioinfo/programming4Bioinformatics/datasets/python_for_biologists_excer/regular_expressions/exercises/dna.txt").read().rstrip("\n")

print("The sequence length is:", len(data), "\n")

#creating a variable to hold the cut positions
#position zero is the start of the sequence
all_cuts = [0]

#cut position for AbcI
for match in re.finditer(r"A[ATCG]TA{2}T", data):
	
	#take the cut position and add it to all_cuts list	
	all_cuts.append(match.start() + 3)


#cut position for AbcII
for match in re.finditer(r"GC[AG][AT]TG", data):
	all_cuts.append(match.start() + 4)
	
#adding the final positio,
all_cuts.append(len(data))

#sort the cut fragments to rearrange them in ascending order
sorted_fragments = sorted(all_cuts)
print(f"Here are the sorted fragments: {sorted_fragments} \n")


#identifying the cut region and printing it out
for i in range(1, len(sorted_fragments)):
	current_cut_position = sorted_fragments[i]
	previous_cut_position = sorted_fragments[i-1]
	frag_size = current_cut_position - previous_cut_position
	print(f"One fragment size is: {frag_size}")	
		
