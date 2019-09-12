import random
import time
import sys


start = time.time()
unsorted = random.sample(range(1, 100000000), 1000)
#unsorted = [3, 9, 6, 2, 10]


# Using Recursion, Python has a default limit of 1000, needs to be raised
def selection_sort(list_in):
	sys.setrecursionlimit(10000)
	if len(list_in) > 1:
		least_num = list_in.pop()
		for num in list_in:
			if least_num > num:
				list_in.append(least_num)
				least_num = num
				list_in.remove(least_num)
		return [least_num] + selection_sort(list_in)
	else:
		return list_in


# Without Recursion
def selection_sort_loop(list_in):
	for i in range(0, len(list_in) - 1):
		min_val = i
		for j in range(i + 1, len(list_in)):
			if list_in[min_val] > list_in[j]:
				min_val = j
		if min_val != i:
			list_in[min_val], list_in[i] = list_in[i], list_in[min_val]
	return list_in


print(selection_sort_loop(unsorted))
#print(selection_sort(unsorted))
end = time.time()
print(end - start)
