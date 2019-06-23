"""Homework 2"""
#task 1
def list_pow(list_first):
	new_list = []
	for pow_do in range(0,len(list_first)):
		new_list.append(list_first[pow_do]**2)
	return new_list
print("#task 1:",list_pow([2,4,5,6,89,100]))

#task 2
def string_symmetry(first_string):
	if len(first_string) <= 1:
		return True
	else:
		return (first_string[0] == first_string[-1] and string_symmetry(first_string[1:-1]))
print("#task 2:",string_symmetry('assa'))

#task 3
def five_division(list_number):
	dictionary_out = {}
	for num in list_number:
		dictionary_out[num] = (num % 5 == 0 if True else False)
	return dictionary_out
print("#task 3:",five_division([2,5,7,9,10,9,99,100,125,1000,45675]))

#tast 4
def parity_filter(list_number):
	new_list = []
	if len(list_number)%2 == 0:
		for parity in range(0,len(list_number)):
			if list_number[parity]%2==0:
				new_list.append(list_number[parity])
			else:
				continue
	else:
		for parity in range(0,len(list_number)):
			if list_number[parity]%2!=0:
				new_list.append(list_number[parity])
			else:
				continue
	return new_list
print("#task 4:",parity_filter([1,2,3,4,5,6,7,8,9]))
print("#task 4:",parity_filter([1,2,3,4,5,6,7,8,9,10]))

#tast 5
def list_parity_unparity(list_number):
	new_list = sorted(list_number)
	new_list_parity = []
	new_list_unparity = []
	for go_list in range(0,len(new_list)):
		if new_list[go_list]%2==0:
			new_list_parity.append(new_list[go_list])
		elif new_list[go_list]%2!=0:
			new_list_unparity.append(new_list[go_list])
	new_list_parity.reverse()
	new_list = new_list_unparity + new_list_parity
	return new_list
print("#task 5:",list_parity_unparity([1,2,3,4,5,6,7,8,3,4,5,6,7,567,345,234,659,19026]))