#-*-coding: utf-8-*-

def print_p(num):
	if type(num) != type(1):
		print("wrong!")
		return 0
	print("*"*num)
	print("*{}*\n".format(" "*(num-2)) * (num-2), end="")
	print("*"*num)
	for line in range(0, num):
		print("*")
	return 1


def main():
	number = int(input("Introduce a number: "))
	print_p(number)

if __name__ == '__main__':
	main()
