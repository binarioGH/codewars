#-*-coding: utf-8-*-

def isCryptSolution(crypt, solution):
	eq = []
	solution = dict(solution)
	for word in crypt:
		futint = ""
		for letter in word:
			futint += solution[letter]
		if futint[0] == "0":
			return False
		futint = int(futint)
		eq.append(futint)
	return eq[0] + eq[1] == eq[2]

