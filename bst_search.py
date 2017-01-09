def right_index(i):
	return i + (i + 2)

def left_index(i):
	return 2 * i + 1

def bst_search(tree, key):
	for i in range(0, len(tree)):
		if tree[i] == key:
			return True
		else:
			if tree[i] != None and key > tree[i]:
				i = right_index(0)
			elif tree[i] != None:
				i = left_index(0)
	return False
