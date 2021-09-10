class Quiz_brain:
    def __init__(self, que_list):
        self.que_list=que_list
        self.que_no=0
        self.score=0
    def nextquestion(self):
        current_que=self.que_list[self.que_no]
        ans=input(f"Q.{self.que_no+1} {current_que.text} (True/False):")
        self.que_no=self.que_no+1
        self.check(current_que, ans)
    def stillhasques(self):
        if(self.que_no<len(self.que_list)):
            return True
        else:
            return False
    def check(self,current_que,ans):
        if(current_que.answer.lower()==ans):
            self.score=self.score+1
            print("You are right!!")
            
        else:
            print("You are wrong")
            print(f"The right answer was: {current_que.answer}")
        print(f"Your score is:{self.score}/{self.que_no}")
    