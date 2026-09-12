import sqlite3
from datetime import date
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

#functon for saving session to db
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
        return cursor.lastrowid

#function for loading sessions from db
def load_sessions_from_database():
    with sqlite3.connect(DATABASE_FILE) as connection:
        cursor = connection.cursor()
        
        cursor.execute(
            """
            SELECT id, subject, minutes, study_date
            FROM sessions
            ORDER BY id
            """
        )
    
        rows = cursor.fetchall()
    
    sessions = []
    
    for row in rows:
        session = {
            "id": row[0],
            "subject": row[1],
            "minutes": row[2],
            "date": row[3]
        }
            
        sessions.append(session)
        
    return sessions

#function for deleting session from db
def delete_session_from_database(session_id):
    with sqlite3.connect(DATABASE_FILE) as connection:
        cursor = connection.cursor()
        
        cursor.execute(
            "DELETE FROM sessions where id = ?",
            (session_id,),
        )
        
        connection.commit

#function for calculating total time with sql
def get_total_minutes_from_database():
    with sqlite3.connect(DATABASE_FILE) as connection:
        cursor = connection.cursor()
        
        cursor.execute(
            "SELECT COALESCE(SUM(minutes), 0) from sessions"
        )
        
        result = cursor.fetchone()
        
    return result[0]

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
    
    session_id = save_session_to_database(
        subject,
        minutes,
        today
    )
    
    session = {
        "id": session_id,
        "subject": subject,
        "minutes": minutes,
        "date": today
    }
    
    sessions.append(session)
    
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
        print("There are no study sessions to delete.")
        return

    print("\nStudy sessions:")

    for number, session in enumerate(sessions, start=1):
        print(
            f"{number}. {session['subject']} - "
            f"{session['minutes']} minutes - "
            f"{session['date']}"
        )

    choice = input(
        "Enter the number of the session to delete: "
    ).strip()

    if not choice.isdigit():
        print("❌ Please enter a valid number.")
        return

    session_index = int(choice) - 1

    if session_index < 0 or session_index >= len(sessions):
        print("❌ That session does not exist.")
        return

    session = sessions[session_index]
    session_id = session["id"]

    delete_session_from_database(session_id)
    sessions.pop(session_index)

    print(
        f"Deleted {session['minutes']} minutes "
        f"of {session['subject']}."
    )

#function for viewing total study time
def show_total_time():
    total_minutes = get_total_minutes_from_database()
    
    
    hours = total_minutes // 60
    remaining_minutes = total_minutes % 60
        
    hour_word = "hour" if hours == 1 else "hours"
    minute_word = "minute" if remaining_minutes == 1 else "minutes"

    print(
        f"⌛ You have studied for {hours} {hour_word} "
        f"and {remaining_minutes} {minute_word}~"
)

def main():
    create_database()
    print("🌸 Welcome to Study Tracker!")
    
    sessions = load_sessions_from_database()
    
    while True:
        show_menu()

        choice = input('\nEnter your choice (1-5):')
        #print(f"You selected option {choice}.")

        #menu responses
        if choice == "1":
            add_session(sessions)
        elif choice == "2":
            view_sessions(sessions)
        elif choice == "3":
            show_total_time()
        elif choice == "4":
            delete_session(sessions)
        elif choice == "5":
            print("Goodbye! Keep learning~ 💗")
            break
        else:
            print("❌ Ops! Invalid choice. Please enter a number from 1 to 5~")

if __name__ == "__main__":
    main()