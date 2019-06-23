"""Homework 3"""
"""Для запуска програмы нужно указать правильное размещение текстового файла в функции print_all в строках 90 и 95""" 
#task 1
def counting_letters(string,list_leters = ['a','e','i','o','u']):#функция посчета определенных букв
	counted_leters = 0
	for check in range(0,len(str(string))):
		if string[check] in list_leters:
			counted_leters += 1
	return counted_leters
def count_text(file_name,list_leters = ['a','e','i','o','u']):#функция посчета определенных букв в тексте и максимальное каличество этих букв в слове
	second_out_text = text_line = list_text =   ""
	max_leters = 0
	prev_max_leters = 1
	with open(file_name) as file:
		for line in file:
			list_text = line.split()
	for string in range(0,len(list_text)):
		max_leters = counting_letters(list_text[string])
		second_out_text += list_text[string] + "(" + str(max_leters) + ") "
		if max_leters > prev_max_leters:
			prev_max_leters = max_leters
			text_line = list_text[string]
	second_out_text += '\n' + 'Max leters in string: ' + str(text_line) + '= ' + str(prev_max_leters) + '.'
	return second_out_text
#print("task 1:")
#print(count_text("D:/py/text.txt"))

#task 2
def the_long_word(first_string):
	for line in first_string:
		string = first_string.split()
	max_word = len(string[0])
	new_list_equal = []
	for line in range(0,len(string)):
		string[line] = string[line].replace(".","")
		if max_word < len(string[line]):
			max_word = len(string[line])
	for line in range(0,len(string)):
		if max_word == len(string[line]):
			new_list_equal.append(string[line])
	return max_word,new_list_equal
#print("task 2:")
#print(the_long_word("""Proin eget tortor risus. Cras ultricies ligula sed magna dictum porta. Proin eget tortor risus. Curabitur non
#nulla sit amet nisl tempus convallis quis ac lectus. Donec rutrum congue leo eget malesuada."""))

#task 3
import random
def open_files(file_name):#фукция для открытия файла
	with open(file_name) as file:
		list_text = file.read()
	return str(list_text)
def get_string(list_li):#функция для преобразования из списка в строку
	new_string = ""
	for text in list_li:#уровень предложений
		for string in text:#уровень строк
			for literal in string:#уровень букв
				new_string += str(literal)
			if string != []:
				new_string += " "
		new_string = new_string[0:-1]#удаление лишнего пробела в конце предложении что бы точка ишла сразу после буквы
		if text != []:
			new_string += ". "
	return new_string
def revers_literals(list_literals):#функция для рандомного размещения букв в слове
	return random.sample(list(list_literals),len(list(list_literals)))
def revers_string(string_list):#функция для рандомного размещения слов в одном предложении
	new_list = []
	string = []
	for line in string_list:
		string = string_list.split(' ')
	for line in range(0,len(string)):
		new_list.append(revers_literals(string[line]))
	return random.sample(new_list,len(new_list))
def revers_text(file_name):#функция для рандомного размещения предложений в тексте
	new_list = []
	first_string = open_files(file_name)
	for line in first_string:
		string = first_string.split('. ')
	for line in range(0,len(string)):
		new_list.append(revers_string(string[line]))
	new_list = random.sample(new_list,len(new_list))
	new_string = get_string(new_list)
	return new_string
#print("task 3:")
#print(revers_text("D:/py/text.txt"))


def print_all():
	print("task 1:")
	print(count_text("D:/py/text.txt"))
	print("task 2:")
	print(the_long_word("""Proin eget tortor risus. Cras ultricies ligula sed magna dictum porta. Proin eget tortor risus. Curabitur non
	nulla sit amet nisl tempus convallis quis ac lectus. Donec rutrum congue leo eget malesuada."""))
	print("task 3:")
	print(revers_text("D:/py/text.txt"))
print_all()
