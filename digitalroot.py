#-*-coding: utf-8-*-

def digital_root(num):
	num = str(num)
	while len(num) != 1:
		num = str(sum(int(x) for x in num))
	return int(num)