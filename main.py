from country_model import CountryQuestion
from quiz_brain import QuizBrain
from data import clean_country_data
from random import choice, shuffle

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

while quiz.still_has_questions():

    question_text = quiz.next_question()
    user_answer = input(f'{question_text} -> True/False: ')
    is_right = quiz.check_answer(user_answer)

    if is_right:
        print('Correct')
    else:
        print('Wrong')

    print(f'Score: {quiz.score}/{quiz.question_number}')