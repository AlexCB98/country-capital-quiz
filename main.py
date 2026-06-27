from country_model import CountryQuestion
from quiz_brain import QuizBrain
from data import clean_country_data
from random import choice, shuffle
from ui import QuizInterface

question_bank = []

true_false = (True, False)

shuffle(clean_country_data)

for item in clean_country_data:
    country = item['country']
    capital = item['capital']

    rnd_choice = choice(true_false)

    if rnd_choice:
        capital = item['capital']
        answer = 'True'
    else:
        wrong_item = choice(clean_country_data)

        while wrong_item['country'] == country:
            wrong_item = choice(clean_country_data)

        capital = wrong_item['capital']
        answer = 'False'

    new_question = CountryQuestion(country, capital, answer)
    question_bank.append(new_question)

quiz = QuizBrain(question_bank)
quiz_ui = QuizInterface(quiz)