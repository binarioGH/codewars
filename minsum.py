#-*-coding: utf-8-*-

	def sum_two_smallest_numbers(numbers):
		mins = [100000000000000000, 1000000000000000000]
		for index in range(0,2):
			for number in numbers:
				if number <= mins[index]:
					 mins[index] = number
			numbers.remove(mins[index])
		return mins[0] + mins[1]

