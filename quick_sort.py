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

