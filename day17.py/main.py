from data import question_data
from question_model import Question
from quiz_brain import QuestionBrain


question_bank=[]
for question in question_data:
   
    question_text=question["text"]
    question_answer=question["answer"]
    new=Question(text=question_text,answer=question_answer)
    question_bank.append(new)

quiz=QuestionBrain(question_bank)

while quiz.his_next_question:
    quiz.next_question()



print("you have complete the quiz")
print(f"the final score is :{quiz.score} / {quiz.question_number}")