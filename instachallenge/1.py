#-*-coding: utf-8-*-

def find_missing(array):
	abc = "abcdefghijklmnopqrstuvwxyz"
	first = abc.find(array[0])
	last = abc.find(array[-1]) + 1
	string = abc[first:last]
	if len(array) == len(string):
		return -1
	else:
		for index in range(len(string)):
			if string[index] != array[index]:
				return string[index]


def main():	
	found = find_missing(["m", "o"])
	if found == -1:
		print("The secuence is correct.")
	else:
		print("The missing letter is {}".format(found))

if __name__ == '__main__':
	main()