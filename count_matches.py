def count_matches(some_list, value):
	count = 0
	if len(some_list) == 0:
		return 0
	if some_list[0] == value:
		count += 1
		return  count + count_matches(some_list[1:], value)
	else:
		return count_matches(some_list[1:], value)