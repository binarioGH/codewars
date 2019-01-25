#-*-coding: utf-8-*-

def rot13(message):
	abc = "abcdefghijklmnopqrstuvwxyz"
	encoded = ""
	for symbol in message:
		if symbol.isupper():
			encoded += "{}".format(abc[abc.find(symbol.lower()) - 13]).upper()
		elif symbol.islower():
			encoded += abc[abc.find(symbol) - 13]
		else:
			encoded += symbol
	return encoded
