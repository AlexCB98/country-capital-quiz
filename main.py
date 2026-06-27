from country_model import CountryQuestion
from data import clean_country_data

question_bank = []

for item in clean_country_data:
    country = item['country']
    capital = item['capital']
    answer = 'True'

    question_model = CountryQuestion(country,capital,answer)
    question_bank.append(question_model)

for question in question_bank[:3]:
    print(question)
    print('---')