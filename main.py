from question_model import Question
from data import question_data
from quiz_brain import QuizzBrain


question_bank = []


for key in question_data:
    question = key["question"]  # creating a new variable for each question of the imported data
    answer = key["correct_answer"]  # creating a new variable for each answer of the imported data
    new_question = Question(question, answer)  # creating a new object from Question class having as
    # input the new variables
    question_bank.append(new_question)  # adding the data to a list using the append method.

manager = QuizzBrain(question_bank)  # Creating new object from the QuizzBrain Class


while manager.still_has_questions():
    manager.next_question()

print("You've completed the quiz")
print(f"Your final score is: {manager.user_score}/{manager.question_number}")

# The still_has_questions method checks if there are questions in the questions_list and displays the
# next one until there is nothing left. It takes hold of the next_question() method as well as the
# question_number and question_list attributes.




#  print(question_bank[0].question, question_bank[0].answer) NOTICE how you have used the objet attribute
# after writing the list index!

