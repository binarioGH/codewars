#-*-coding: utf-8-*-
WORDS = ("hello", "world") #En la kata hay una variable precargada con 1000 palabras en inglés
def break_caesar(message):
	abc = "abcdefghijklmnopqrstuvwxyz"
	for key in range(len(abc)):
		decoded_message = decode(message,key,abc)
		if isEnlgish(decoded_message):
			return key
	return -1
def decode(text,key, letters):
	decoded = ""
	for symbol in text:
		if symbol in letters:
			if symbol.isupper():
				decoded_letter_index = letters.find(symbol.lower()) + key
			else:
				decoded_letter_index = letters.find(symbol) + key
		else:
			decoded += symbol
	return decoded
def isEnlgish(message):
	message = message.lower()
	message_without_nonletters = []
	for symbol in message:
		if symbol.isalpha() or symbol == " ":
		    message_without_nonletters.append(symbol)
	word_counter = len(message_without_nonletters)
	message_without_nonletters = "".join(message_without_nonletters)
	match_counter = 0
	for word in message_without_nonletters.split():
		if word in WORDS:
			match_counter += 1
	if match_counter >= int(word_counter) / 2:
		return True
	return False