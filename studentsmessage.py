#-*-coding: utf-8-*-
#https://www.youtube.com/watch?v=JcPDyQWq6QA&pbjreload=10
from math import sqrt
def decipher_message(message):
	key = int(sqrt(len(message)))
	plaintext = [""] * key
	current_row = 0
	for symbol in message:
		plaintext[current_row] += symbol
		current_row += 1
		if current_row > key - 1:
			current_row = 0
	return "".join(plaintext)
