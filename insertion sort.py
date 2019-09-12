import time
import random

start = time.time()

unsorted = random.sample(range(1, 100000000), 1000)


def insertion_sort(list_in):
	for i in range(1, len(list_in)):
		sorted_list_in = list_in[i]
		while list_in[i - 1] > sorted_list_in and i > 0:
			list_in[i], list_in[i - 1] = list_in[i - 1], list_in[i]
			i = i - 1
	return list_in


print(insertion_sort(unsorted))
end = time.time()
print(end - start)
