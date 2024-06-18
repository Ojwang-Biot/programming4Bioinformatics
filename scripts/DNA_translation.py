# python program to translate a DNA sequence into protein. 


#creating a dictionary of DNA codes and their translation

gencode = {'ATA':'I', 'ATC':'I', 'ATT':'I', 'ATG':'M', 'ACA':'T', 'ACC':'T','ACG':'T', 
'ACT':'T', 'AAC':'N', 'AAT':'N', 'AAA':'K', 'AAG':'K', 'AGC':'S', 'AGT':'S', 'AGA':'R', 'AGG':'R', 'CTA':'L', 'CTC':'L', 'CTG':'L', 'CTT':'L', 'CCA':'P','CCC':'P', 'CCG':'P', 'CCT':'P', 'CAC':'H', 'CAT':'H', 'CAA':'Q', 'CAG':'Q', 'CGA':'R', 'CGC':'R', 'CGG':'R', 'CGT':'R', 'GTA':'V', 'GTC':'V', 'GTG':'V', 'GTT':'V', 'GCA':'A', 'GCC':'A', 'GCG':'A', 'GCT':'A', 'GAC':'D', 'GAT':'D', 'GAA':'E', 'GAG':'E', 'GGA':'G', 'GGC':'G', 'GGG':'G', 'GGT':'G', 'TCA':'S', 'TCC':'S', 'TCG':'S', 'TCT':'S', 'TTC':'F', 'TTT':'F', 'TTA':'L', 
'TTG':'L', 'TAC':'Y', 'TAT':'Y', 'TAA':'_', 'TAG':'_', 'TGC':'C', 'TGT':'C', 'TGA':'_', 'TGG':'W'}
	
def dna_to_protein(sequence):
	
	#convert to uppercase
	sequence = sequence.upper()
	
	#calculate the start position for the final codon
	last_codon_start = len(sequence) -2
	
	#defining variable to hold protein sequence
	protein = ""
	
	#processing the DNA sequence in three base codes
	
	#the first position is 0, the last position is (len() of sequence -2), steps 3 		
	#since codons are written in 3's
	for start in range(0,last_codon_start,3):
		
		#extracting the three base codon
		codon = sequence[start:start+3]
		
		#translate dna to amino acid, the X option in get method is to unknown aa 
		#to be replaced by X
		aa = gencode.get(codon, 'X')
		
		#creating an amino acid chain
		protein = protein + aa
		
	return f"Protein sequence is: {protein}"

print(dna_to_protein("ATGTTCGGT"))
print(dna_to_protein("ATCGATCGATCGTTGCTTATCGATCAG"))
print(dna_to_protein("actgatcgtagctagctgacgtatcgtat")) 
print(dna_to_protein("ACGATCGATCGTNACGTACGATCGTACTCG")) 
