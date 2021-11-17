from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = []

for ques_dictionary in question_data:
    New_question = Question(ques_dictionary['text'], ques_dictionary['answer'])
    question_bank.append(New_question)


quiz = QuizBrain(question_bank)

while quiz.still_has_question():
    quiz.next_question()


print("you have completed the quiz")
print(f"your final score was: {quiz.score}/{len(question_bank)} ")


