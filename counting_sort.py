def counting_sort(keys, max_key):
	result = []
	count = [0] * (max_key + 1)
	for x in keys:
		count[x] += 1
	for i in range(0, max_key + 1):
		for k in range(0, count[i]):
			result.append(i)
	return result

def find_largest(values):
	largest = values[0]
	for x in range(1, len(values)):
		if values[x] > largest:
			largest = values[x]
	return largest

def time_sort(n):
	my_list = list(range(n))
	from time import time
	max_key = find_largest(my_list)
	start = time()
	counting_sort(my_list, max_key)
	return time() - start