def bubble_sort(list_in):
	sort = True
	while sort:
		sort = False
		for i in range(len(list_in) - 1):
			if list_in[i] > list_in[i + 1]:
				sort = True
				list_in[i], list_in[i + 1] = list_in[i + 1], list_in[i]
	return list_in
