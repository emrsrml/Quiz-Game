class quiz:
    def __init__(self,q_list):
        self.question_number = 0
        self.qusetion_list = q_list
        self.user_score = 0
    def still_has_question(self):
        return self.question_number < len(self.qusetion_list)

    def next_question(self):
        current_question = self.qusetion_list[self.question_number]
        self.question_number += 1
        user_answer = input(f"Q.{self.question_number}:{current_question} True/False:")
        self.check_answer(user_answer,current_question.answer)
    
    def check_answer(self,user_answer,correct_answer):
        if user_answer == correct_answer.lower():
            print("You got it right!")
            self.user_score += 1
        else:
            print("that's wrong")
        print(f"correct answer was: {correct_answer}")
        print(f"current scoer is {self.user_score}/{self.question_number}")
        print("\n")
            
        
            