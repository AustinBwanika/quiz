class QuizBrain:
    # TODO Asking questions
    # TODO Checking if the answer was correct
    # TODO checking if we're at the end of the quiz
    def __init__(self, list):
        self.question_number = 0
        self.question_list = list
        self.score = 0

    def next_question(self,):
        current_question = self.question_list[self.question_number]
        self.question_number += 1
        prompt = input(f"Q:{self.question_number} {current_question.text} (True or False?)")
        self.check_answer(prompt, current_question.answer)

    def still_has_questions(self):
        if self.question_number == len(self.question_list) :
            return False
        else:
            return True

    def check_answer(self, user_answer, correct):
        if user_answer.lower() == correct.lower():
            print("You got it correct")
            self.score += 1

        else:
            print("That's wrong")
        print(f"The correct answer was: {correct}")
        print(f"Your current score is {self.score}/{self.question_number}\n")

