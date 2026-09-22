# ToDo App

A small Flask application for creating, updating, and deleting tasks. It uses a local SQLite database.

## Run Locally

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python app.py
```

Open `http://127.0.0.1:5000` in a browser. The application creates its local `todo.db` database when it starts; the database is intentionally ignored by Git.
