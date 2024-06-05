# program to print accession names that satisfy certain criteria


#loading regular expressions module
import re

#function to store accessions
def accessions():
	accs = ['xkn59438', 'yhdck2', 'eihd39d9', 'chdsye847', 'hedle3455', 'xjhd53e', '45da', 'de37dp']
	
	return accs
	

#accessions with the number 5

for match in accessions():
	if re.search(r"5", match):
		print(match)
		
print()

#printing accessions containing letter d or e

print("The following accessions contain d or e\n")

for match in accessions():
	if re.search(r"(d|e)", match):
		print(match)
	
		
#contain the letters d and e in that order
print("\nAccessions containing d and e in that order\n")
for match in accessions():
	if re.search(r"d.*e", match):
		print(match)
		
		
#contain the letters d and e in that order with a single letter between them
#in this case we use dot(.) delimiter

print("\nAccessions containing letters d and e in that order with a single letter between them\n")
for acc in accessions():
	if re.search(r"(d.e)", acc):
		print(acc)
		

#contain both the letters d and e in any order
print("\nAccessions containing both the letters d and e in any order")
for acc in accessions():
	if re.search(r"(d.*e|e.*d)", acc):
		print(acc)


#start with x or y
print("\nAccessions starting with x or y")
for acc in accessions():
	if re.search(r"^x", acc) or re.search(r"^y", acc):
		print(acc)


#start with x or y and end with e
print("\nAccessions starting with x or y and end with e")
for acc in accessions():
	if (re.search(r"^x", acc) or re.search(r"^y", acc)) and re.search(r"e$", acc):
		print(acc)
		


#contain three or more numbers in a row
#to match 3 or more numbers in a row, a more specific quantifier is used with a curly bracket

print("\nAccessions containing three or more numbers in a row")
for acc in accessions():
	if re.search(r"[0123456789]{3,100}", acc):
		print(f'\t {acc}') 


#end with d followed by either a, r or p
print("\nAccessions ending with d followed by either a, r or p")
for acc in accessions():
	if re.search(r"d[arp]$", acc):
		print(f'\t{acc}')











