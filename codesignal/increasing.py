#-*-coding: utf-8-*-
def almostIncreasingSequence(seq):
	c = 1
	for n in seq:
		if n <= 0:
			seq.remove(n)
		if n != c:
			seq.remove(n)
			if seq == list(range(min(seq), len(seq)+1)):
				return True
			return False
		c += 1
	return True