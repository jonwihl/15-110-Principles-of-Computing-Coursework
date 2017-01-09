import csv
import pdb

def friends_with_files(friends_file_name, fof_file_name):
	with open(friends_file_name, mode='r') as infile:
		infile.readline()
		reader = csv.reader(infile)
		mydict = {}
		for row in reader:
			mydict[row[0]] = row[1:]
		fof_dict = friends_of_friends(mydict)
	with open(fof_file_name, mode='w') as outfile:
		writer = csv.writer(outfile)
		writer.writerow(["person", "friend of friends"])
		for name in fof_dict:
			writer.writerow([name, fof_dict[name]])

def friends_of_friends(d):
	fof_dict = {key: [] for key in d}
	for person in d:
		for friends in d[person]:
			fof_dict[person] +=	d[friends]
	
	for person in fof_dict:					#removes person from their friend of friends
		for friend in fof_dict[person]:
			if person in fof_dict[person]:
				fof_dict[person].remove(person)

	for i in range(len(fof_dict)):
		for friend in fof_dict:  			 #removes original friends from friend of friends
			for name in fof_dict[friend]:
				if name in d[friend]:
					fof_dict[friend].remove(name)

	for friend in fof_dict:					#removes duplicates in persons friend of friends 
		for name in fof_dict[friend]:
			while fof_dict[friend].count(name) > 1:
				fof_dict[friend].remove(name)

	return fof_dict	

def test_friends_of_friends():
	friends_with_files("office.csv", "office_fof.csv")
	friends_with_files("republicans.csv", "republicans._fof.csv")
	friends_with_files("college.csv", "college_fof.csv")

