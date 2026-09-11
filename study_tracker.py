# initial menu
print('🌸 Welcome to Study Tracker!')

while True:
    print('\nWhat would you like to do?')
    print("1. Add a study session")
    print("2. View study sessions")
    print("3. View total study time")
    print("4. Exit")

    choice = input('\nEnter your choice (1-4):')
    #print(f"You selected option {choice}.")

    #menu responses
    if choice == "1":
        print("Let's add a study session~! 📖")
    elif choice == "2":
        print('Here are your study sessions~ 📚')
    elif choice == "3":
        print("Let's calculate your total study time~ ⌛")
    elif choice == "4":
        print("Goodbye! Keep learning~ 💗")
        break
    else:
        print("❌ Ops! Invalid choice. Please enter a number from 1 to 4~ ❌")