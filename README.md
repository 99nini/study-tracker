# Study Tracker

A command-line study tracker built with Python and SQLite.

## Features

- Add study sessions
- Automatically record the date
- View saved sessions
- Edit existing sessions
- Delete sessions
- Calculate total study time
- Store data locally with SQLite
- Validate user input
- Preserve data between program restarts

## Requirements

- Python 3.11 or newer

SQLite is included with Python, so no additional packages are required.

## Run the Application

Open a terminal in the project folder and run:

```bash
python study_tracker.py
```

## Data Storage

Study sessions are stored locally in:

```text
study_tracker.db
```

The database file is ignored by Git, so personal study data is not uploaded to GitHub.

The application automatically creates the database and its `sessions` table when it starts.

## Database Operations

The application supports the four main database operations, also known as CRUD:

- **Create** — add a study session
- **Read** — view saved sessions
- **Update** — edit an existing session
- **Delete** — remove a session

## Technologies

- Python
- SQLite
- SQL
- Git
- GitHub

## Project Status

- [x] Stage 1 — Command-line application with JSON storage
- [x] Stage 2 — SQLite database and CRUD operations
- [ ] Stage 3 — Flask web application
- [ ] Stage 4 — Dashboard styling
- [ ] Stage 5 — Deployment
