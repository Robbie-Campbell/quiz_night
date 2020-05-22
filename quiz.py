answer = open("answers.txt", "a")
level = 0
question = 0

while level < 8:
    question = 0
    level += 1
    print("Round " + str(level))
    answer.write("Round: " + str(level) + "\n")
    while question < 5:
        question += 1
        question_answer = input("Input your answer for question " + str(question) + ": ")
        answer.write(str(question) + ": " + question_answer + "\n")

answer.close()
