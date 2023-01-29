class QuizzBrain:

    def __init__(self, q_list):
        self.question_number = 0
        self.question_list = q_list
        self.user_score = 0

    def still_has_questions(self):
        return self.question_number < len(self.question_list)

    def next_question(self):
        current_question = self.question_list[self.question_number]
        self.question_number += 1
        users_answer = input(f"Q.{self.question_number}: {current_question.question} (True/False): ")
        self.check_answers(users_answer, current_question.answer)  # Here you are creating a connexion between the
        # next_question() method and the check_answers() method, otherwise the check_answers() method
        # cannot use the attributes set in the next_question() method when it is created.

    def check_answers(self, users_answer, correct_answer):  # correct_answer parameter is based in current_question
        if users_answer.lower() == correct_answer.lower():
            print("You got it!")
            self.user_score += 1
        else:
            print("Sorry, that is wrong...")
        print(f"the correct answer is {correct_answer}")
        print(f"Your current score is: {self.user_score}/{self.question_number}")
        print("\n")



# Remember that everything in OOP work based on connection between the different
# elements of the program. In the next_question method created in the QuizzBrain class you created a new
# variable called current_question to get hold of the current question that the user works with. In it, you're
# apparently just going to work with data from the QuizzBrain class, but when you import the class to
# the main.py you'll be working with the question_bank, which is composed by objects created from the Question
# class. The objects from the Question class have as attributes ".question" and ".answer", that is why, in the input()
# from the next_question method you see that the current_question variable has ".question" as attribute.
