def sum(numbers):
	total = 0
	for x in range(0, len(numbers)):
		total = total + numbers[x]
	return total

def dot_product(A, B):
	dot = []
	if len(A) == len(B):
		for x in range(0, len(A)):
			num = A[x] * B[x]
			dot.append(num)
	else:
		return None
	return sum(dot)