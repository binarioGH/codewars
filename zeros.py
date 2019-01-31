#-*-coding: utf-8-*-
def zeros(n):
	if n == 0:
		return 0
	nm = 1
	for num in range(1, n+1):
		nm *= num
	n = str(nm)[::-1]
	count = 0
	for num in n:
		if int(num) == 0:
			count += 1
		else:
			return count