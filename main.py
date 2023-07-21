from question_model import Question
from data import question_data
from quiz_brain import  quiz

question_bank = []
for question in question_data:
    question_text = question["text"]
    question_answer = question["answer"]
    new_question = Question(question_text,question_answer)
    question_bank.append(new_question)


quiz1 = quiz(question_bank)

while quiz1.still_has_question() :
    quiz1.next_question()
    
print("you have complete the quiz")
print(f"you final score {quiz1.question_number}")