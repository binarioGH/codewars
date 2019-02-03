#-*-coding: utf-8-*-
def detectnum(word):
	count = 0
	n = ""
	for char in word:
		if char.isaplha():
			count += 1
			n += char
		else:
			return (int(n), count)
def decipher_this(text):
	decipher_text = []
	for word in text.slpit():
		num, border = detectnum(word)
