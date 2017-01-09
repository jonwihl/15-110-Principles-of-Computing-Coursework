#Checks if root is a leaf of a Huffman tree and return True. Returns False otherwise
def is_leaf(root):
	if type(root) == str: #Check if root is type string
		return True
	else:
		return False

#Checks if root has 2 children and returns True. Returns False if it does not
def is_binary_node(root):
	if len(root) == 2: #checks if root has two children 
		return True
	else:
		return False 

#Checks if root is a valid tree
def is_prefix_tree(root):
	if len(root) != 1: #base case- root is a valid tree
		if len(root) == 2 and len(root[0]) != 1:
			return True
		if is_binary_node(root) == True or is_leaf(root) == True: #checks if root is a leaf or binary node
			return is_prefix_tree(root[1]) 
	return False 

#Function decodes root
def decode_char(root, code_str):
	if is_leaf(root) == True: #base case if root is a leaf
		return (root, code_str)
	else:
		if code_str[0] == "0":
			return decode_char(root[0], code_str[1:]) 
		else:
			return decode_char(root[1], code_str[1:])

#creates code using decode_char. Uses char_str to match letters
def decode(root, code_str):
	output = ""
	while len(code_str) > 0:
		(decoded_char, code_str) = decode_char(root, code_str)
		output += decoded_char
	return output

def find_codewords(root, code_table, partial_codeword):
	if is_leaf(root):
		code_table[root] = partial_codeword
		return code_table
	else:
		left = find_codewords(root[0], code_table, partial_codeword + "0")
		return find_codewords(root[1], left, partial_codeword + "1")

def build_code_table(root):
	code_dict = {}
	partial_codeword = ""
	return find_codewords(root, code_dict, partial_codeword)

def encode(code_table, msg):
	new_msg = ""
	for i in msg:
		if i in code_table:
			new_msg += code_table[i]
		else:
			print("Error, not encodable")
	return new_msg

'''
Ran out of time before I could finish commenting 

'''
