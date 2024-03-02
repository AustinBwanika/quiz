# Imports
from question_model import Question
from data import question_data
from quiz_brain import QuizBrain


# Variables
question_bank = []

for i in question_data:
    text = i["text"]
    answer = i["answer"]
    question_data = Question(q_text=text, q_answer=answer)
    question_bank.append(question_data)

# print(question_bank)

quiz = QuizBrain(question_bank)


while quiz.still_has_questions():
    quiz.next_question()

print("You have completed the quiz!")
print(f"Your final score was: {quiz.score}/{quiz.question_number}")