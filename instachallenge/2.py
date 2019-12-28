#-*-coding: utf-8-*-
from json import loads


def main():
	with open("morse.json", "r") as f:
		morse_data = f.read()
	morsecode = loads(morse_data)
	text = input("Input your text: ")
	text = text.lower()
	new_text = ""
	for char in text:
		if char not in morsecode:
			continue
		else:
			new_text += morsecode[char] + " "
	print("\n\n{}\n\n".format("="*80))
	print("Translated text: {}".format(new_text))


if __name__ == '__main__':
	main()