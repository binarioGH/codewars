#-*-coding: utf-8-*-
class VigenereCipher(object):
    def __init__(self, key, alphabet):
        self.key = key
        self.abc = alphabet
    def translate(self, text, mode):
    	border = "\n{}".format("-"*80)
    	translated = ""
    	keyindex = 0
    	for symbol in text:
    		if symbol in self.abc:
    			if mode == "e":
    				translatedindex = self.abc.find(symbol) + self.abc.find(self.key[keyindex])
    			else:
    				translatedindex = self.abc.find(symbol) - self.abc.find(self.key[keyindex]) 			
    			if translatedindex > len(self.abc):
    				translatedindex -= len(self.abc)
    			translated += self.abc[translatedindex]
    			print("{}symbol: {}\nindex:{} {}\nkeyindex:{}{}".format(border,symbol,translatedindex, self.abc[translatedindex],keyindex,border))
    		else:
    			translated += symbol
    		keyindex += 1
    		if keyindex == len(self.key):
    			keyindex = 0
    	return translated
    def decode(self, text):
    	return self.translate(text, "d")
    def encode(self, text):
    	return self.translate(text, "e")

