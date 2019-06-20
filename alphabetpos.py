#-*-coding: utf-8-*-
def alphabet_position(text):
	text = text.lower()
	numstring = []
	abc = "abcdefghijklmnopqrstuvwxyz"
	for char in text:
		index = abc.find(char)
		if index == -1:
			continue
		numstring.append(str(index + 1))
	return " ".join(numstring)