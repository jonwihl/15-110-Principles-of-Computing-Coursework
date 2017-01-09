import math

def num_perfect_square(numbers):
	prime_numbers = []
	for x in range(0, len(numbers)):
		if numbers[x] >= 0:
			if math.sqrt(numbers[x]).is_integer() == True:
				prime_numbers.append(numbers[x])
			elif x == len(numbers) and math.sqrt(numbers[x]).is_integer() == False:
				not_in_list = -1
				return not_in_list
		else:
			x += 1
	return (len(prime_numbers))