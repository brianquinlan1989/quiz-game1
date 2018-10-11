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


def add_a_question():
     question = input("Enter a question: ")
     answer = input("Answer: ")
     
     with open ("questions.txt", "a") as f:
         line = question + "|" + answer + "\n"
         f.write(line)


while True:
    option = show_menu()
    
    if option == "1":
        print("you picked run quiz")
        
    if option == "2":
       add_a_question()
    
    if option == "3":
        break
