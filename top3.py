#-*-coding: utf-8-*-
def getLongerWord(dic):
	longer = ""; 
	MaxCounter = 0;
	for word in dic:
		if(dic[word] >= MaxCounter):
			longer = word;
			MaxCounter = dic[word];
	return longer;

def deleteNonLetters(word):
	newWord = "";
	abc = "abcdefghijklmnopqrstuvwxyz'";
	basura = True;
	for char in word:
		if(char in abc):
			newWord += char;
			if(char != "'"):
				basura = False;
	if(basura):
		return "";
	return newWord;

def top_3_words(text):
	top3 = [];
	words = {};
	for word in text.split(" "):
		word = word.lower();
		word = deleteNonLetters(word);
		if(word == "" or word == " "):
			continue
		if(word in words):
			words[word] += 1;
		else:
			words[word] = 1;
	while len(top3) < 3:
		if(len(words) <= 0):
			break;
		mostUsed = getLongerWord(words);
		if(mostUsed == "" or mostUsed == " "):
			continue;
		del words[mostUsed];
		top3.append(mostUsed);
	return top3;