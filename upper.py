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

def title(text):
	text = text.split()
	
	windex = 0
	for word in text:
		word = list(word)
		index = -1
		alpha = True
		for letter in word:
			index += 1
			if not letter.isalpha():
				continue
			else:			
				if alpha:
					alpha = False
					word[index] = upper(letter)
				else:
					word[index] = lower(letter)
				
		word = "".join(word)
		text[windex] = word
		windex += 1
	return " ".join(text)