#!/usr/bin/env python3

#this function takes two arguments - a protein sequence and an amino acid residue code and returns the percentage of the protein that the amino acid makes up

def amino_acid_residue(protein, aa):
	
	#converting the arguments into uppercase
	protein = protein.upper()
	aa = aa.upper()
	
	#determine protein length
	length_protein = len(protein)
	
	aa_count = protein.count(aa)
	
	#compute the percent protein that the amino acid makes up
	percent_protein = (aa_count / length_protein) * 100
	
	#output percent protein
	return percent_protein
	
#testing the function

assert amino_acid_residue("MSRSLLLRFLLFLLLLPPLP", "M") == 5
assert amino_acid_residue("MSRSLLLRFLLFLLLLPPLP", "r") == 10
assert amino_acid_residue("MSRSLLLRFLLFLLLLPPLP", "L") == 50
assert amino_acid_residue("MSRSLLLRFLLFLLLLPPLP", "Y") == 0
