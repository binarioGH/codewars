#-*-coding: utf-8-*-
def calcType(a, b, res):
	if a + b == res:
		return "addition"
	elif a - b == res or b - a == res:
		return "subtraction"
	elif a * b == res:
		return "multiplication"
	elif a / b == res or b / a == res:
		return "division"