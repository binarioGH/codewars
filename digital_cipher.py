#-*-coding: utf-8-*-
def encode(message, key):
	abc = "abcdefghijklmnopqrstuvwxyz"
	message = message.lower()
	encoded = []
	keyindex = 0
	key = str(key)
	for symbol in message:
		if not symbol.isalpha():
			continue
		encoded.append(abc.find(symbol) + 1+int(key[keyindex] ))
		keyindex += 1
		if keyindex == len(key):
			keyindex = 0
	return encoded
	
