import json
from datetime import date
DATA_FILE = "sessions.json"

# menu
def show_menu():
    print("\nWhat would you like to do?")
    print("1. Add a study session")
    print("2. View study sessions")
    print("3. View total study time")
    print("4. Exit")

#function for loading saved sessions
def load_sessions():
    try:
        with open(DATA_FILE, "r", encoding="utf-8") as file:
            return json.load(file)
        
    except FileNotFoundError:
        return []
    
    except json.JSONDecodeError:
        print("Warning: The sessions file contains invalid JSON")
        return []

#start message    
print("🌸 Welcome to Study Tracker!")

study_sessions = load_sessions()

#function for adding new session
def add_session(sessions):
    subject = input("📖 What subject did you study? ").strip()
    
    if not subject:
        print("❌ The subject can not be empty")
        return
    
    minutes_text = input("⌛ How many minutes did you study? ").strip()
    
    if not minutes_text.isdigit():
        print("❌ Please enter the minutes as a number value")
        return
    
    minutes = int(minutes_text)
    
    if minutes <= 0:
        print("❌ Study time must be greater than zero")
        return
    
    today = date.today().isoformat()
    
    session = {
        "subject": subject,
        "minutes": minutes,
        "date": today
    }
    
    sessions.append(session)
    save_sessions(sessions)
    print(f"Added {minutes} minutes of {subject}~")

#function for viewing sessions    
def view_sessions(sessions):
    if not sessions:
        print("❌ Ops! You have not added any study sessions yet")
        return

    print("\nYour study sessions:")
    
    for number, session in enumerate(sessions, start=1):
        subject = session["subject"]
        minutes = session["minutes"]
        session_date = session.get("date", "Unknown date")
    
        print(f"{number}. {session_date} — {subject}: {minutes} minutes")
        
#function for viewing total study time
def show_total_time(sessions):
    if not sessions:
        print("❌ Ops! You have not added any study sessions yet")
        return
    
    total_minutes = 0
        
    for session in sessions:
        total_minutes += session["minutes"]
            
    hours = total_minutes // 60
    remaining_minutes = total_minutes % 60
        
    print(f"⌛ You have studied for {hours} hours and {remaining_minutes} minutes~")
    
#function for saving sessions to json
def save_sessions(sessions):
    with open(DATA_FILE, "w", encoding="utf-8") as file:
        json.dump(sessions, file, indent=4, ensure_ascii=False)
        

while True:
    show_menu()

    choice = input('\nEnter your choice (1-4):')
    #print(f"You selected option {choice}.")

    #menu responses
    if choice == "1":
        add_session(study_sessions)
    elif choice == "2":
        view_sessions(study_sessions)
    elif choice == "3":
        show_total_time(study_sessions)
    elif choice == "4":
        print("Goodbye! Keep learning~ 💗")
        break
    else:
        print("❌ Ops! Invalid choice. Please enter a number from 1 to 4~")