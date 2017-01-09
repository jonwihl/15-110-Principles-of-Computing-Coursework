def digit(num, pos):
	new = num // 10 ** (pos - 1)
	return new % 10


def reverse_num(num, num_digits):
	#initialize variables 
	i = 1
	reverse = 0
	while (i < num_digits + 1):
		value = digit(num, i) * (10 ** (num_digits - i)) 
		reverse = reverse + value
		i += 1
	return (reverse)
		
def pal_num(num, num_digits):
	if reverse_num(num, num_digits) == num:
		return True
	else:
		return False

def get_first(num):
	while(num / 10 > 1):
		new = num // 10
		num = new
	return (num)

def num_digits(num):
	return len(str(num))

def rotate_num(num, rotate, left):
	if left == True and rotate != 1:
		new1 = num // 10 ** (rotate)
		new2 = num - new1 * 10 ** (rotate)
		new3 = new2 * 10 ** (rotate)
		final = new3 + new1
		return (final)
	elif left == True and rotate == 1:
		digits = num_digits(num)
		new1 = num // 10 ** (digits - rotate)
		new2 = num - new1 * 10 ** (rotate)
		new3 = new2 * 10 ** (rotate)
		final = new3 + new1
		return (final)
	elif left == False and rotate != 1:
		new_1 = num % 10 ** (rotate)
		new_2 = num - new_1
		new_3 = new_2 // 10 ** (rotate)
		new_4 = new_1 * 10 ** (rotate)
		final_1 = new_3 + new_4
		return (final_1)
	elif left == False and rotate == 1:
		new_1 = num % 10 ** (rotate)
		new_2 = num - new_1
		new_3 = new_2 // 10 ** (rotate)
		new_4 = num_digits(num)
		new_5 = new_1 * 10 ** (new_4 - 1)
		final = new_3 + new_5
		return (final)
			
def test_rotate_num():
    # We can rotate numbers either left or right
    # Right
    assert rotate_num(1234, 1, False) == 4123
    # Left
    assert rotate_num(1234, 2, True) == 3412

    # Rotating single digit numbers always results in the same number
    assert rotate_num(0, 1, True) == 0
    assert rotate_num(1, 1, False) == 1
    assert rotate_num(2, 2, True) == 2

    # We can rotate a number back to its original value.
    assert rotate_num(1234, 4, True) == 1234
    assert rotate_num(1234, 4, False) == 1234
    
    # Rotation of 0 digits has no effect.
    assert rotate_num(1234, 0, True) == 1234
    assert rotate_num(1234, 0, False) == 1234
    assert rotate_num(1000, 0, True) == 1000

    # We can correctly rotate numbers with trailing zeros.
    assert rotate_num(1000, 1, True) == 1
    assert rotate_num(1000, 1, False) == 100
    assert rotate_num(1000, 4, True) == 1000
    assert rotate_num(1000, 4, False) == 1000 		
	

