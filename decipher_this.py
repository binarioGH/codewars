#-*-coding: utf-8-*-
def getFirstLetter(m):
	letter = ""
	index = 0
	for c in m:
		if not c.isalpha():
			letter += c
			index += 1
			continue
		break
	return (chr(int(letter)), index)
def decipher_this(msj):
	decrypted = []
	for word in msj.split():
	    fl, i = getFirstLetter(word) #fl = first letter, i = index
	    newword = word[i:]
	    newword = newword[::-1]
	    decrypted.append("{}{}".format(fl,newword))
	return " ".join(decrypted)