#!/usr/bin/env python3

#this function takes two arguments - a protein sequence and a list of amino acid residue code. if no list is given, it returns the percentage of hydrophobic amino acid residues (A, I, L, M, Y and V)

def amino_acid_residue(protein, aa_list=['A', 'I', 'L', 'F', 'M', 'W', 'Y', 'V']):
	
	#converting the arguments into uppercase
	protein = protein.upper()
	
	#determine protein length
	length_protein = len(protein)
	
	total = 0
	for aa in aa_list:
		aa = aa.upper()
		aa_count = protein.count(aa)
	
		#add number for this residue to the total amount
		total = total + aa_count
		
	#compute the percent protein that the amino acid makes up
	percent_protein = total * 100 / length_protein
		
	#output percent protein
	return percent_protein
	
#testing the function with assertions
assert amino_acid_residue("MSRSLLLRFLLFLLLLPPLP", ["M"]) == 5
assert amino_acid_residue("MSRSLLLRFLLFLLLLPPLP", ['M', 'L']) == 55
assert amino_acid_residue("MSRSLLLRFLLFLLLLPPLP", ['F', 'S', 'L']) == 70
assert amino_acid_residue("MSRSLLLRFLLFLLLLPPLP") == 65


