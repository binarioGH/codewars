#-*-coding: utf-8-*-
def positive_sum(arr):
	total = 0
	for num in arr:
		if num <= 0:
			continue
		else:
			total += num
	return total