#-*-coding: utf-8-*-
def encode(text):
	plain_text = ["", ""]
	index = 0
	for symbol in text:
		plain_text[index] += symbol
		if index == 0:
			index += 1
		else:
			index -= 1
	return "".join(plain_text)