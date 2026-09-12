import json
import sqlite3
from datetime import date
DATA_FILE = "sessions.json"
DATABASE_FILE = "study_tracker.db"

# menu
def show_menu():
    print("\nWhat would you like to do?")
    print("1. Add a study session")
    print("2. View study sessions")
    print("3. View total study time")
    print("4. Delete a study session")
    print("5. Exit")

#function for creating db
def create_database():
    with sqlite3.connect(DATABASE_FILE) as connection:
        cursor = connection.cursor()
        
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS sessions (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                subject TEXT NOT NULL,
                minutes INTEGER NOT NULL,
                study_date TEXT NOT NULL
            )
        """)
        
        connection.commit()

def save_session_to_database(subject, minutes, study_date):
    with sqlite3.connect(DATABASE_FILE) as connection:
        cursor = connection.cursor()
        
        cursor.execute(
            """
            INSERT INTO sessions (subject, minutes, study_date)
            VALUES (?, ?, ?)
            """,
            (subject, minutes, study_date)
        )
        
        connection.commit()

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
    save_session_to_database(subject, minutes, today)
    
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

#function for deleting an existing study session
def delete_session(sessions):
    if not sessions:
        print("You have not added any study sessions yet")
        return
    
    view_sessions(sessions)
    
    session_number_text = input(
        "\nEnter the number of the session to delete: "
    ).strip()
    
    if not session_number_text.isdigit():
        print("Please enter a valid session number")
        return
    
    session_number = int(session_number_text)
    session_index = session_number - 1
    
    if session_index < 0 or session_index >= len(sessions):
        print("This session number does not exist")
        return
    
    removed_session = sessions.pop(session_index)
    save_sessions(sessions)
    
    subject = removed_session["subject"]
    minutes = removed_session["minutes"]
    
    print(f"Deleted {minutes} minutes of {subject}.")

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
        
    hour_word = "hour" if hours == 1 else "hours"
    minute_word = "minute" if remaining_minutes == 1 else "minutes"

    print(
        f"⌛ You have studied for {hours} {hour_word} "
        f"and {remaining_minutes} {minute_word}~"
)

#function for saving sessions to json
def save_sessions(sessions):
    with open(DATA_FILE, "w", encoding="utf-8") as file:
        json.dump(sessions, file, indent=4, ensure_ascii=False)
        
def main():
    create_database()
    print("🌸 Welcome to Study Tracker!")
    
    study_sessions = load_sessions()
    
    while True:
        show_menu()

        choice = input('\nEnter your choice (1-5):')
        #print(f"You selected option {choice}.")

        #menu responses
        if choice == "1":
            add_session(study_sessions)
        elif choice == "2":
            view_sessions(study_sessions)
        elif choice == "3":
            show_total_time(study_sessions)
        elif choice == "4":
            delete_session(study_sessions)
        elif choice == "5":
            print("Goodbye! Keep learning~ 💗")
            break
        else:
            print("❌ Ops! Invalid choice. Please enter a number from 1 to 5~")

if __name__ == "__main__":
    main()