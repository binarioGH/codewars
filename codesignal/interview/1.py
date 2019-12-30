#-*-coding: utf-8-*-
def firstDuplicate(lst):
	seen = []
	for number in lst:
		if number in seen:
			return number
		return number
	return -1