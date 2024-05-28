#!/usr/bin/env python3
#program to complement DNA sequence

dna_seq = "ACTGATCGATTACGTATAGTATTTGCTATCATACATATATATCGATGCGTTCAT"

#complementing the DNA sequence using replace method

#replace A
replaceA = dna_seq.replace('A', 't')

#replace T
replaceT = replaceA.replace('T', 'a')

#replace C
replaceC = replaceT.replace('C', 'g')

#replace G 
replaceG = replaceC.replace('G', 'c')


#printing the complemantary DNA sequence

print(replaceG.upper())

