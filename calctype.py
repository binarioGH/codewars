#-*-coding: utf-8-*-
def calcType(a, b, res):
	ans = {"addition": a+b,"subtraction":a-b,"multiplication":a*b,"division":a/b}
	for op in ans:
		if ans[op] == res:
			return op