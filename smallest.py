#-*-coding: utf-8-*-
def find_the_smallest_int(nums):
	mn = nums[0];
	for num in nums:
		if num <= mn:
			mn = num;
	return mn;