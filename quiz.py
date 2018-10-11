def show_menu():
    print("Quiz Game")
    print("----------")
    print()
    print("1. Run Quiz")
    print("2. Enter A Question")
    print("3. Exit")
    print()
    
    option = input("Enter option: ")
    return option


while True:
    option = show_menu()
    
    if option == "3":
        break
