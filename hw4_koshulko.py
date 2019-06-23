from datetime import datetime
class Person():
	"""docstring for Person"""
	surname = "Koshulko"
	first_name = "Vladislav"
	nickname = "Riz"
	birth_date = datetime.strptime("1900-01-01","%Y-%m-%d")
	def __init__(self, surname, first_name, nickname, birth_date):
		self.surname = surname
		self.first_name = first_name
		self.nickname = nickname
		self.birth_date = birth_date

	def get_age(self):
		try:
			age = datetime.now() - datetime.strptime(str(self.birth_date),"%Y.%m.%d")
		except Exception:
			raise ValueError("Дата рождения неправильного формата!")
		age = str(int(age.days/365))+" years."
		return age

	def get_fullname(self):
		fullname = self.surname + " " + self.first_name
		return fullname