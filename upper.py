#-*-coding: utf-8-*-





upper = lambda t: transform(t, "abcdefghijklmnñopqrstuvwxyz", -32)
lower = lambda t: transform(t, "ABCDEFGHIJKLMNÑOPQRSTUVWXYZ", 32 )

def transform(text, alphabet, add):
	text = list(text)
	new_text = ""
	for char in text:
		if char in alphabet:
			char = ord(char) + add
			char = str(chr(char))
		new_text += char
	return new_text
