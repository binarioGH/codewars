#-*-coding: utf-8-*-
def first_non_repeating_letter(string):
	banned = []
	letters = []
	for char in string:
		if char.lower() in letters:
			letters.remove(char.lower())
		elif char.upper() in letters:
			letters.remove(char.upper())
		else:
			if not char in banned:
				letters.append(char)
			banned.append(char)
	print(letters)
	if len(letters) == 0:
		return ""
	indexes = []
	for l in letters:
		indexes.append(string.find(l))
	nonrep = string[min(indexes)]
	return nonrep