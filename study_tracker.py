# initial menu
print("🌸 Welcome to Study Tracker!")

study_sessions = []

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
        subject = input("📖 What subject did you study?")
        minutes = int(input("How many minutes did you study?"))
        
        session = {
            "subject": subject,
            "minutes": minutes
        }
        
        study_sessions.append(session)
        print(f"Added {minutes} minutes of {subject}~")
    elif choice == "2":
        if not study_sessions:
            print("❌ Ops! You have not added any study sessions yet")
        else:
            print("\nYour study sessions:")
            
            for number, session in enumerate(study_sessions, start=1):
                subject = session["subject"]
                minutes = session["minutes"]
                
                print(f"{number}. {subject} — {minutes} minutes")
    elif choice == "3":
        print("Let's calculate your total study time~ ⌛")
    elif choice == "4":
        print("Goodbye! Keep learning~ 💗")
        break
    else:
        print("❌ Ops! Invalid choice. Please enter a number from 1 to 4~")