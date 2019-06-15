#-*-coding: utf-8-*-
def solution(string):
	if not string % 2 == 0:
		string += "_"
	s = []
	cs = ""
	for char in string:
		cs += char
		if len(cs) == 2:
			s.append(cs)
			cs = ""
	return s