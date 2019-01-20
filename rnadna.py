#-*-coding: utf-8-*-
def DNAtoRNA(dna):
	dna = list(dna)
	for symbol in range(len(dna)):
		if dna[symbol] == "T":
			dna[symbol] = "U"
	return "".join(dna)