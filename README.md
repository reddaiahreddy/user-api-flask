# Flask User API (Week 1)

## Overview
This is a simple REST API built using Flask. It demonstrates basic backend concepts such as routing, HTTP methods, and JSON handling.

## Features
- GET /users → Fetch all users
- POST /users → Add a new user
- In-memory data storage

## Tech Stack
- Python
- Flask
- REST API

## How to Run

```bash
pip install flask
python app.py


# Future Improvements (Week 2 planned)
- Add database (SQLite/PostgreSQL)
- Add input validation
- Improve project structure
- Add error handling

Week 2
# Week 2 Improvements

## Database Integration
- SQLite database added
- SQLAlchemy ORM configured
- Persistent data storage

## Data Modeling
- User model created
- Database schema initialized

## API Quality
- Input validation
- Error handling
- Proper HTTP status codes

---

# Current Architecture

```text
Client
 ↓
Flask API
 ↓
SQLAlchemy ORM
 ↓
SQLite Database
```

---

# Tech Stack

- Python
- Flask
- SQLite
- SQLAlchemy
- Git
- GitHub

---

# How to Run

```bash
pip install -r requirements.txt
python app.py
```

---

# Week 3 Planned Improvements

- Update user API (PUT)
- Delete user API (DELETE)
- Project folder restructuring
- Service layer
- Cleaner architecture

# Week 3 Improvements

## CRUD Completion
- PUT /users/<id>
- DELETE /users/<id>

## Architecture Improvements
- Flask Blueprints
- Modular route structure
- Service layer introduced
- Separation of concerns
