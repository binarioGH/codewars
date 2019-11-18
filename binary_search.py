#-*-coding: utf-8-*-
from random import randint

def generate_list(mxlen=10, mnn=1, mxn=100):
	lst = [randint(mnn,mxn)]
	number = lst[0]
	first = number
	for i in range(mxlen):
		number += randint(mnn, mxn)
		lst.append(number)
	return lst

def main():
	print(generate_list())



if __name__ == '__main__':
	main()