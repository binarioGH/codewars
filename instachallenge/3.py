#-*-coding: utf-8-*-
from math import sqrt
def isPrime(number):
	for n in range(2, int(sqrt(number) + 1)):
		if number % n == 0:
			return False
	return True


def main():
	number = int(input("Input a number: "))
	counter = 0
	ni = 1
	while counter < number:
		if isPrime(ni):
			counter += 1
		ni += 1

	print("the {}th prime number is {}".format(number, ni))




if __name__ == '__main__':
	main()