#-*-coding: utf-8-*-
def encrypt_this(text):
	cypher_text = []
	for word in text.split():
		if len(word) == 1:
			cypher_text.append(str(ord(word)))
		encoded_word = list(word)
		encoded_word[0] = str(ord(word[0]))
		encoded_word[1:2] = word[len(word) - 1]
		encoded_word[len(word) - 1] = word[1:2]
		cypher_text.append("".join(encoded_word))
	return " ".join(cypher_text)