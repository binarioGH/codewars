#-*-coding: utf-8-*-
def adjacentElementsProduct(arr):
	products = []
	cnt = 0
	for n in arr:
		candidates = []
		if cnt != 0:
			candidates.append(n*arr[cnt-1])
		try:
			candidates.append(n*arr[cnt+1])
		except:
			pass
		products.append(max(candidates))
		cnt += 1
	return max(products)
