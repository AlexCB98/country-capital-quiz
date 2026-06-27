class QuizBrain:

    def __init__(self, question_bank):
        self.question_number = 0
        self.score = 0
        self.question_list = question_bank
        self.current_question = None

    def still_has_questions(self):
        return self.question_number < len(self.question_list)

    def next_question(self):
        self.current_question = self.question_list[self.question_number]
        self.question_number +=1
        return (f'Q.{self.question_number}: Is {self.current_question.capital}'
                f' the capital of {self.current_question.country}?')

    def check_answer(self, user_answer):
        current_answer = self.current_question.answer

        if current_answer.lower() == user_answer.lower():
            self.score += 1
            return True
        else:
            return False