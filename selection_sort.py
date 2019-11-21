

def selection_sort(unsorted):
	for i in range(len(unsorted)):
		min_val = i
		for j in range(1 + i, len(unsorted)):
			if unsorted[min_val] > unsorted[j]:
				hold_1 = unsorted[j]
				unsorted[j] = unsorted[min_val]
				unsorted[min_val] = hold_1
	return unsorted



