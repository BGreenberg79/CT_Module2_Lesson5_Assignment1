# Task 1 develop a list of questions and answers

question_1 = "Who is the first NBA MVP? \na) Bob Cousy \nb) Tom Heinsohn \nc) Oscar Robertson \nd) Bob Pettit: "
question_2 = "Who was the last emperor of China? \na) Puyi \nb) Qin Shi Huang \nc) Emperor Min \nd) Emperor Taizu: "
question_3 = "Who directed the Dekalog? \na) Jacques Demy \nb) Akira Kurosawa \nc) Krzysztof Kieslowski \nd) Luis Bunuel: "
question_4 = "What year did Walt Disney World open? \na) 1955 \nb) 1971 \nc) 1964 \nd) 1982: "
q1_correct = "d"
q1_wrong = ["a", "b", "c"]
q2_correct = "a"
q2_wrong = ["b", "c", "d"]
q3_correct = "c"
q3_wrong = ["a", "b", "d"]
q4_correct = "b"
q4_wrong = ["a", "c", "d"]

'''
I combined the questions and answers into the same variables and used the \n syntax to 
separate the answers within the same variable to facilitate the coding of the input 
functions that will be used to actually administer the quiz. I then defined variables for the right
and wrong answer's creating an answer key that will work off of if/else statements and for statements.
'''

# Task 2 Write a function that quizzes the user and takes their answers

def quiz_user():
    print("You are about to be quizzed! Please enter any answers as a single lower case letter")
    global correct_answers
    global incorrect_answers
    correct_answers = []
    incorrect_answers = []
    while True:
        ask_q1 = input(question_1)
        if ask_q1 == q1_correct:
            print("Congratulations you are correct!")
            correct_answers.append(ask_q1)
            break
        elif ask_q1 in q1_wrong:
            print("Sorry that is an incorrect answer")
            incorrect_answers.append(ask_q1)
            break
        else:
            print("Incorrect answer format")
            continue
    while True:
        ask_q2 = input(question_2)
        if ask_q2 == q2_correct:
            print("Congratulations you are correct!")
            correct_answers.append(ask_q2)
            break
        elif ask_q2 in q2_wrong:
            print("Sorry that is an incorrect answer")
            incorrect_answers.append(ask_q2)
            break
        else:
            print("Incorrect answer format")
            continue
    while True:
        ask_q3 = input(question_3)
        if ask_q3 == q3_correct:
            print("Congratulations you are correct!")
            correct_answers.append(ask_q3)
            break
        elif ask_q3 in q3_wrong:
            print("Sorry that is an incorrect answer")
            incorrect_answers.append(ask_q3)
            break
        else:
            print("Incorrect answer format")
            continue
    while True:
        ask_q4 = input(question_4)
        if ask_q4 == q4_correct:
            print("Congratulations you are correct!")
            correct_answers.append(ask_q4)
            break
        elif ask_q4 in q4_wrong:
            print("Sorry that is an incorrect answer")
            incorrect_answers.append(ask_q4)
            break
        else:
            print("Incorrect answer format")
            continue

quiz_user()
'''
This function gives a multiple choice quiz for all 4 earlier defined questions and then 
appends correct answes to one global list, that can later be graded, and appends to a 
different global list of incorrect answers while also giving immediate feedback. I used an 
if/elif/else chain for correct/incorrect/invalid entry and made each question a while loop
where break statements alow the user to proceed to the next question if right or wrong and 
continue statements to allow a second guess for typos/ineligible answer formats.
'''

# Task 3 Score the Quiz and give the user feedback on their performance

total_correct = len(correct_answers)
total_wrong = len(incorrect_answers)
quiz_length = 4
try:
    number_grade = (total_correct / quiz_length) * 100
except:
    number_grade = 100
print(f"You answered {total_correct} questions correctly and {total_wrong} questions incorrectly, resulting in a {number_grade}% on the quiz.")
