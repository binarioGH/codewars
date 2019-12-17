#-*-coding: utf-8-*-


abc = "abcdefghijklmnñopqrstuvwxyz"
ABC = "ABCDEFGHIJKLMNÑOPQRSTUVWXYZ"

def upper(text):
	text = list(text)
	new_text = ""
	for char in text:
		if char in abc:
			char = ord(char) - 32
			char = string(chr(char))
		new_text += char
	return new_text
