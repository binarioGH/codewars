#-*-coding: utf-8-*-
def getOnlyLetters(word):
	word = word.lower();
	letters = [];
	for letter in word:
		if(letter == " "):
			continue;
		if(not letter in letters):
			letters.append(letter);
	letters = sorted(letters);
	letters = "".join(letters);
	return letters;
def find_uniq(words):
	short = {}
	for word in words:
		shortWord = getOnlyLetters(word);
		if(not shortWord in short):
			short[shortWord] = [1, word];
		else:
			short[shortWord][0] += 1;
	for s in short:
		if(short[s][0] == 1):
			nonMatching = short[s][1];
	return nonMatching