#-*-coding: utf-8-*-
WORD = ["hello", "world"] #esta lista es más grande en la kata.

def break_caesar(message):
	abc = "abcdefghijklmnopqrstuvwxyz"
	print("Encoded message:\n{}".format(message))
	for key in range(0, len(abc)):
		decoded = decipher(message, key, abc)
		if isEnglish(decoded):
			print("decoded message:\n{}".format(decoded))
			return key
	return -1
def decipher(message, key, abc):
	decoded = ""
	for symbol in message:
		if symbol.isalpha():
			index = abc.find(symbol.lower()) - key
			if index > len(abc):
				index -= len(abc)
			if symbol.isupper():
				decoded += abc[index].upper()
			else:
				decoded += abc[index]
		else:
			decoded += symbol
	return decoded


def isEnglish(phrase):
	phrase = removeNonletters(phrase)
	phrase = phrase.lower()
	word_counter = 0
	match_counter = 0
	for word in phrase.split():
		if word in WORDS:
			match_counter += 1
		word_counter += 1
	return match_counter >= int(word_counter / 2)


def removeNonletters(text):
	only_letters = ""
	for symbol in text:
		if symbol.isalpha() or symbol == " ":
			only_letters += symbol
	return only_letters
