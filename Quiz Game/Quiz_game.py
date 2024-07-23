questions = ("what is python?: ",
             "what is C?: ",
             "what is Bash?: ")
options = (("A. Script language .", "B. Programming language ."),
           ("A. programming language .", "B.Script language ."),
           ("A. Script language .", "B. Programming language ."))
answers = ("B","A","A")
guesses = []
score = 0
question_num = 0

for question in questions:
    print("===========================")
    print(question)
    for option in options[question_num]:
        print(option)
    guess = input("Enter (A, B): ").upper()
    guesses.append(guess)
    if guess == answers[question_num]:
        score += 1
        print("CORRECT!")
    else:
        print("INCORECT!")
        print(f"{answers[question_num]} is the correct one .")
    question_num += 1

print("===========================")
print("          SCORE            ")
print("===========================")

score =(score / len(questions) * 100)
print(f"YOUR SCORE IS : {score:.0f}%")
print("===========================")