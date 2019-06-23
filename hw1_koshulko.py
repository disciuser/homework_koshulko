"""Homework 1"""
#task 1
from functools import reduce
def is_polindrom(string,number_of_method):#функция разварота строки
	if number_of_method == 0:#разварот строки через срез
		return string[::-1]
	elif number_of_method == 1:#разварот строки через функцию
		return "".join(reversed(string))
	elif number_of_method == 2:#разварот строки в цикле
		chars = list(string)
		for simbol in range(len(string)//2):
			temp = chars[simbol]
			chars[simbol] = chars[len(string)-simbol-1]
			chars[len(string)-simbol-1] = temp
		return "".join(chars)
	elif number_of_method == 3:#разварот строки с помощю рекурсии
		if len(string) == 1:
			return string
		return string[-1]+is_polindrom(string[:-1],3)
	elif number_of_method == 4:#разварот строки с помощю лямбда функции
		return reduce(lambda x,y : y+x, string)
print("task 1: string 'Reverse my!'")
print("	Method 1, list slice:",is_polindrom("Reverse my!",0))
print("	Method 2, function:",is_polindrom("Reverse my!",1))
print("	Method 3, cicle:",is_polindrom("Reverse my!",2))
print("	Method 4, recursion:",is_polindrom("Reverse my!",3))
print("	Method 5, lambda:",is_polindrom("Reverse my!",4))


#task 2
def counting_letters(string,list_leters):#функция посчета определенных букв
	counted_leters = 0
	for check in range(0,len(string)):
		if string[check] in list_leters:
			counted_leters += 1
	return counted_leters
print("task 2:",counting_letters("Hello this is my homework. I learn Python!",['a','e','i','o','u']))


#task 3
def counting_substring(string,list_leters):#функция посчета построк
	new_list_leters = list_leters.lower()
	new_string = string.lower()
	return new_string.count(new_list_leters)
print("task 3:",counting_substring("Hello this is my homework. I learn Python! This is very good! Is, iS, IS, is","IS"))


#task 4
'''def longest_alphabetical_substring(text, rank=lambda char: char):
    if not text: # empty
        return text
    longest = substr = []
    prev = text[0]
    for char in text[1:]:
        substr.append(prev)
        if rank(prev) > rank(char): # end of alphabetical substring
            if len(longest) < len(substr):
                longest = substr
            substr = []
        prev = char
    substr.append(prev)
    return type(prev)().join(substr if len(longest) < len(substr) else longest)
print("task 4:",longest_alphabetical_substring("slirhgoqin4rogqi"))'''


#task 5
def GetType(object):
	if type(object) == list:
		return "Type list:"+str(object)

	elif type(object) == tuple:
		return "Type tuple:"+str(object)

	elif type(object) == dict:
		return "Type dict:"+str(object)

	elif type(object) == int:
		return "Type int:"+str(object)

	elif type(object) == float:
		return "Type float:"+str(object)

	elif type(object) == str:
		return "Type string:"+"'"+str(object)+"'"

	else:
		return "".join("Type of object not found! " + object)
print("task 5:",GetType({"asd":23,45.56:True}))


#task 6
def GetMessageType(object_A,object_B):
	
	if type(object_A) == str or type(object_B) == str :
		return "String received(Получена строка)."
	elif type(object_A) == int and type(object_B) == int:
		if object_A > object_B:
			return "More(Больше)."
		elif object_A == object_B:
			return "Are equal(Равны)."
		elif object_A < object_B:
			return "less(Меньше)."
print("task 6:")
print("	",GetMessageType("qwerty",24))
print("	",GetMessageType(48,23))
print("	",GetMessageType(55,55))
print("	",GetMessageType(37,78))


#task 7
import random
def Unique(list_somthing,rand_sort = False):
	new_unique_list = []
	for check in range(0,len(list_somthing)):
		if list_somthing[check] not in new_unique_list:
			new_unique_list.append(list_somthing[check])
	if rand_sort == True:
		new_unique_list = random.sample(new_unique_list,len(new_unique_list))
	return new_unique_list
print("task 7:",Unique(["a", 5, 2, 5, (1, "a"), "a"],True))


#task 8
def every_third(list_somthing,method):
	new_third_list = []
	if method == 0:
		for check in range(2,len(list_somthing),3):
			new_third_list.append(list_somthing[check])
	else:
		new_third_list = list_somthing[2::3]
	return tuple(new_third_list)
print("task 8:")
print("	Method 1",every_third(["a", 5, 2, 6, 1, "b", "c"],0))
print("	Method 2",every_third(["a", 5, 2, 6, 1, "b", "c"],1))


#task 9
'''def Min_Max(x,y,z):
	return max(max(x,y,z),max(x,y),)
print("task 9:")
print("	test 1: X", Min_Max(5,2,1))
print("	test 2: X", Min_Max(5,2,3))
print("	test 3: Z", Min_Max(1,3,2))
print("	test 4: Y", Min_Max(1,2,5))'''