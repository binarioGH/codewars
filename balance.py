#-*-coding: utf-8-*-
def onlyLetters(text):
	letters = "abcdefghijklmnopqrstuvwxyz"
	letters += letters.upper()
	letters += "1234567890."
	newstring =""
	for char in text:
		if letters.find(char) == -1:
			continue
		newstring += char
	return newstring

def balance(book):
	lines = book.split("\n")
	newbook = []
	balance = float(onlyLetters(lines[0]))
	newbook.append("Original Balance: {0:.2f}".format(balance))
	for line in lines[1:]:
		try:
			splitedline = line.split(" ")
			id = splitedline[0]
			item = onlyLetters(splitedline[1])
			value = float(onlyLetters(splitedline[2]))
		except:
			continue
		else:
			balance -= value
			newbook.append("{} {} {0:.2f} Balance {0:.2f}".format(id, item, value, balance))
	return "\r".join(newbook)