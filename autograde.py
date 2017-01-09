import random
from random import randint, choice 

def autograder():
	random_var = (random.choice([1,2,3,4,5,6,7,8,9,10]))
	if random_var == 1:
		return randint(10,59)
	elif random_var > 1 and random_var < 5:
		return randint(60, 69)
	elif random_var >= 5 and random_var < 8:
		return randint(70, 79)
	elif random_var >= 8 and random_var <= 9:
		return randint(80, 89)
	elif random_var > 9 and random_var <= 10:
		return randint(90,100)

def run_autograder(trials):
	avg = {"A" : None, "B" : None, "C" : None, "D" : None, "R" : None}
	new_var = []
	new_var1 = []
	less_sixty = 0
	for i in range(0, trials):
		new_var.append(autograder()) 
	for k in range(0, len(new_var)):
		new_var1.append(new_var[k] // 10)
	for j in range(0, 5):
		less_sixty += new_var1.count(j) / len(new_var1)
	avg['R'] = less_sixty
	for l in range(6, 10):
		total = new_var1.count(l) / len(new_var1)
		if l == 6:
			avg['D'] = total
		elif l == 7:
			avg['C'] = total
		elif l == 8:
			avg['B'] = total
		elif l >= 9  and j <= 10:
			avg['A'] = total
	return avg

def test_autograder(num_experiments, tolerance):
	grade_frequencies = run_autograder(num_experiments)
	if abs(grade_frequencies['A'] - .1) > tolerance:
		return False
	elif abs(grade_frequencies['B'] - .2) > tolerance:
		return False
	elif abs(grade_frequencies['C'] - .3) > tolerance:
		return False
	elif abs(grade_frequencies['D'] - .3) > tolerance:
		return False
	elif abs(grade_frequencies['R'] - .1) > tolerance:
		return False
	return True


def assign_grades(names):
	grades = {}
	for i in range(0, len(names)):
		grades[names[i]] = autograder()
	return grades

def show_grades(grades) :
    print("Name", " " * (19 - len("Name")), "Grade")
    for (k, v) in grades.items() :
        print(k, " " * (20 - len(k)), v)