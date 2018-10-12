def show_menu():
    print("----------")
    print("Quiz Game")
    print("----------")
    print()
    print("1. Run Quiz")
    print("2. Enter A Question")
    print("3. Exit")
    print()
    
    option = input("Enter option: ")
    return option


def ask_questions():
    with open("questions.txt") as f:
        questions = f.read().split("\n")[:-1]
        
    score = 0
    
    for q in questions:
        question, answer = q.split("|")
        guess = input (question)
        
        
        if guess.casefold() == answer.casefold():
            score += 1
            
    print("You scored {0}".format(score) + " out of " + str(len(questions)))
        
    

def add_a_question():
     question = input("Enter a question: ")
     answer = input("Answer: ")
     
     with open ("questions.txt", "a") as f:
         line = question + "|" + answer + "\n"
         f.write(line)


while True:
    option = show_menu()
    
    if option == "1":
        ask_questions()
        
    if option == "2":
       add_a_question()
    
    if option == "3":
        break
