#-*-coding: utf-8-*-
def correct(string):
	string = list(string)
	plscorrect = {"5":"S", "0":"O", "1":"I"}
	index = 0
	while index < len(string):
		char = string[index]
		if char in plscorrect:
			string[index] = plscorrect[char]
		index += 1
	return "".join(string)