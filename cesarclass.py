#-*-coding: utf-8-*-

class CaesarCipher:
	def __init__(self, key):
		self.key = int(key);
		self.abc ="ABCDEFGHIJKLMNOPQRSTUVWXYZ";
	def encode(self, txt):
		return self.translate(txt, "e");
	def decode(self, txt):
		return self.translate(txt, "d");
	def translate(self, txt, m):
		translated = "";
		txt = txt.upper();
		for char in txt:
			if(char not in self.abc):
				translated += char;
			else:
				indx = self.abc.find(char);
				if(m == "d"):
					indx -= self.key;
				else:
					indx += self.key;
				if(indx >= len(self.abc)):
					indx %= len(self.abc);
				if(indx < 0):
					indx += len(self.abc);
				translated += self.abc[indx];
		return translated;