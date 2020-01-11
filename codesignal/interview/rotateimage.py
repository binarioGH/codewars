#-*-coding: utf-8-*-

def rotateImage(a):
	rotated = []
	for i in range(len(a)):
		rotated.append([])
	counter = -1
	backwards = -1
	for i in range(len(a)):
		grid = 0	
		counter = 0
		for number in a[backwards]:
			rotated[grid].append(number)
			grid += 1
			counter += 1
		backwards -= 1
	return rotated	 

def printImage(image):
	for i in image:
		print(i)

def main():
	image = [[1,2,3],[4,5,6],[7,8,9]]
	printImage(image)
	result = rotateImage(image)
	print("\n{}\n".format("-"*80))
	printImage(result)

if __name__ == '__main__':
	main()