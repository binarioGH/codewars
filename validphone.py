#-*-coding: utf-8-*-
def valid_phonenumber(number):
	counter = 0
	if len(number) == 14:
		counter += 1
	if number[5] == " " and number[9] == "-":
		counter += 1
	if counter != 2:
		return False
	return True