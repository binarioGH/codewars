#-*-coding: utf-8-*-
from random import randint
from random import choice as randchoice

def generate_list(mxlen=10, mnn=1, mxn=100):
	lst = [randint(mnn,mxn)]
	number = lst[0]
	first = number
	for i in range(mxlen - 1):
		number += randint(mnn, mxn)
		lst.append(number)
	return lst

def find(lst, num):
	mn = 0
	mx = len(lst) - 1
	index = randint(mn, mx)
	counter = 0
	while lst[index] != num and counter < len(lst):
		if lst[index] > num:
			mx = index
		elif lst[index] < num:
			mn = index
		counter += 1
		index = randint(mn, mx)
	print("min: {}\nmax: {}".format(mn,mx))
	return index

	

def main():
	lst = generate_list()
	num = randchoice(lst)
	print("Lista: {}\nNum: {}".format(lst, num))
	index = find(lst, num)
	print("Index: {}".format(index))
	if lst[index] == num:
		print("Funciona :3")
	else:
		print("No funciona") 
	


if __name__ == '__main__':
	main()