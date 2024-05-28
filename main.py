from Bio.Seq import Seq

file_path = 'sequence.txt'

with open(file_path, 'r') as file:
    dna_sequence = file.read().strip()

sequence = Seq(dna_sequence)

motif = "ACTG"
pozycja = []
pos = -1
idz = True

while idz:
    pos = sequence.find(motif, pos+1)
    if pos == -1:
        idz = False
    else:
        pozycja += [pos]

print(", ".join([str(i) for i in pozycja]))