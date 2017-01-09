def left_index(i):
	left_node = i + (i + 1)
	return left_node

def right_index(i):
	right_node = i + (i + 2)
	return right_node

def parent_index(i):
	if i % 2 == 0:
		parent_node = i // 2 - 1 
	else:
		parent_node = i // 2
	return parent_node

def is_leaf(tree, i):
	left = left_index(i)
	right = right_index(i)
	if left > len(tree) or right > len(tree):
		return True
	else:
		return False

def missing_child(tree, i):
	if is_leaf(tree, i):
		return []
	elif tree[right_index(i)] == None:
		return [tree[i]] + missing_child(tree, left_index(i))
	elif tree[left_index(i)] == None:
		return [tree[i]] + missing_child(tree, right_index(i))
	else:
		return missing_child(tree, left_index(i)) + missing_child(tree, right_index(i))