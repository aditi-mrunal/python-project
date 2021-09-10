from question_model import Question
from data import question_data
from quiz_brain import Quiz_brain 
question_bank=[]


for que in question_data:
    que_text=que["text"]
    que_ans=que["answer"]
    question_bank.append(Question(que_text, que_ans))
    
quiz=Quiz_brain(question_bank)
while quiz.stillhasques():
    quiz.nextquestion()
print(f"Your final score is: {quiz.score}/{quiz.que_no}")    
    