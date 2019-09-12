import time
import random

start = time.time()

unsorted = random.sample(range(1, 100000000), 1000)


def quick_sort(list_in):
	if len(list_in) <= 1:
		return list_in
	else:
		pivot_val = list_in.pop()
	less_pivot = []
	great_pivot = []
	for i in range(len(list_in)):
		if pivot_val > list_in[i]:
			less_pivot.append(list_in[i])
		else:
			great_pivot.append(list_in[i])
	return quick_sort(less_pivot) + [pivot_val] + quick_sort(great_pivot)


print(quick_sort(unsorted))
end = time.time()
print(end - start)
