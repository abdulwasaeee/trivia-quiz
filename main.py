from data import question_data
from question_model import Question 
from quiz_brain import Quiz
from logo import logo

print(logo)

quizbank=[]
q=1

for i in question_data:
  question=Question(q,i["text"],i["answer"])
  quizbank.append(question)
  q+=1 
  

quiz=Quiz(quizbank)

print("\nAnswer by true or false\n")

quiz.ask()

print(f"\nQuiz finished. Final score is {quiz.score}/{len(quizbank)}")
  
