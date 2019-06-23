#-*-coding: utf-8-*-*

def countSubsequences(needle, haystack):
	nindex = 0
	counter = 0
	needle = "".join(needle.split())
	haystack = "".join(haystack.split())
	for char in haystack:
		if char == needle[nindex - 1] and needle[nindex] != needle[nindex -1]:
			continue
		elif needle[nindex] == char:
			nindex += 1
		else:
			nindex = 0
		if len(needle) -1 == nindex:
			nindex = 0
			counter += 1
	return counter

def main():
	a = input(">")
	b = input(">")
	print(countSubsequences(a,b))

if __name__ == '__main__':
	main()