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
	return " 	".join(text)

def length(text):
	counter = 0
	for char in text:
		counter += 1
	return counter

def find(text,char):
	counter = 0
	for c in text:
		if c == char:
			return counter
		counter += 1 
	return -1

def isalpha(text):
	text = text.lower()
	abc = "abcdefghijklmnñopqrstuvwxyz"
	for char in text:
		if char not in abc:
			return False
	return True

def isdigit(number):
	number = str(number)
	for digit in number:
		try:
			digit = int(digit)
		except:
			return False
	return True

def isSpecialChar(char):
	if not isdigit(char) and not isalpha(char):
		return True
	return False