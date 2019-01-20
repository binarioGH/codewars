#-*-coding: utf-8-*-
def solve(arr):
	dup = []
	for index in arr:
		if index in dup:
			arr.remove(index)
		else:
			dup.append(index)
	return arr