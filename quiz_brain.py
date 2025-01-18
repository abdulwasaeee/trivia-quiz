class Quiz:
   
    def __init__(self,list):
      self.list=list
      self.score=0
      
    def ask(self):
      for i in self.list:
        user_answer=input(f"Q{i.number}. {i.text}\n")
        self.check(user_answer,i.answer)
        print(f"Current score is {self.score}/{len(self.list)}")
        
    def check(self,user,correct):
      if user==correct.lower():
        print("Correct!")
        self.score+=1
      else:
        print(f"Wrong. Answer is {correct} ")
