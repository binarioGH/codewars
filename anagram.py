#-*-coding: utf-8-*-

def anagrams(word, words):
	anagramlist = [];
	ordenatedWord = sorted(word)
	for w in words:
		if(sorted(w) == ordenatedWord):
			anagramlist.append(w);
	return anagramlist;