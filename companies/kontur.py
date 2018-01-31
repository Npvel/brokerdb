import requests
from urllib3.exceptions import HTTPError
from datetime import datetime, timedelta

KONTUR_API_KEY = '3208d29d15c507395db770d0e65f3711e40374df'

def process_regdate(company_data):
	try:
		reg_date = datetime.strptime(company_data["UL"]["legalName"]["date"], "%Y-%m-%d")
		today = datetime.now()
		date_past = today - timedelta(days = 365*30)
		if reg_date > today:
			print('Некоректаня дата регистрации')
			return False
		elif reg_date < date_past:
			print('Невозможно')
			return False
		else:
			company_data["UL"]["legalName"]["date"] = reg_date
			return company_data
	except(ValueError):
		print ('Некорректный формат даты')
		return False


def is_legal_name_valid(company_data):
	legal_name = company_data["UL"]["legalName"]["short"]
	if len(legal_name) <= 5:
		print('Вероятно название компании некорректно')
		return False

	return True


def is_zip_code_valid(company_data):
	zip_code = company_data["UL"]["legalAddress"]["parsedAddressRF"]["zipCode"]
	if len(zip_code) != 6:
		print("Некорректный почтовый индекс")
		return False

	return True


def get_company_inn(inn):
	try:
		responce = requests.get('https://focus-api.kontur.ru/api3/req?key={}&ogrn=&inn={}'.format(KONTUR_API_KEY, inn))
		try:
			responce.raise_for_status()
			try:
				company_data = responce.json()[0]
				if is_legal_name_valid(company_data) and is_zip_code_valid(company_data):
					company_data = process_regdate(company_data)
					if company_data:
						return company_data
			except(IndexError):
				print('Нет такой компании')
		except(HTTPError):
			print('Ошибка на сервере Контура')
	except(requests.exceptions.RequestException):
		print('Произошла ошибка соединения')

	return False


if __name__=="__main__":
	result = get_company_inn(1657012526)
	if result:
		print(result)
	else:
		print('Что-то пошло не так')
		