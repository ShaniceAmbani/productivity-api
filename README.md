# Productivity API

## Project Description

Productivity API is a secure RESTful Flask backend that allows users to create and manage personal notes. The application uses JWT (JSON Web Token) authentication to ensure that only authenticated users can access protected endpoints. Each user can only create, view, update, and delete their own notes.

The API supports:

- User registration
- User login
- Authentication using JWT
- Viewing the logged-in user's profile
- Full CRUD operations for notes
- Pagination for listing notes
- Database seeding with sample data

---

## Technologies Used

- Python
- Flask
- Flask-RESTful
- Flask-SQLAlchemy
- Flask-Migrate
- Flask-Bcrypt
- Flask-JWT-Extended
- SQLite
- Faker

---

## Installation

### 1. Clone the repository

```bash
git clone git@github.com:ShaniceAmbani/productivity-api.git
```

### 2. Navigate into the project

```bash
cd productivity-api
```

### 3. Install dependencies

```bash
pipenv install
```

### 4. Activate the virtual environment

```bash
pipenv shell
```

---

## Database Setup

Initialize migrations (only the first time):

```bash
export FLASK_APP=app.py
flask db init
```

Create a migration:

```bash
flask db migrate -m "Initial migration"
```

Apply the migration:

```bash
flask db upgrade
```

---

## Seed the Database

Run:

```bash
python seed.py
```

This creates sample users and notes.

---

## Running the Application

Start the Flask server:

```bash
python app.py
```

The API will run on:

```
http://127.0.0.1:5000
```

---

# API Endpoints

## Authentication

### POST `/signup`

Creates a new user.

### POST `/login`

Authenticates a user and returns a JWT access token.

### GET `/me`

Returns the currently authenticated user's information.

Requires a valid JWT token.

---

## Notes

### GET `/notes`

Returns the authenticated user's notes with pagination.

Query Parameters:

- `page`
- `per_page`

---

### POST `/notes`

Creates a new note for the authenticated user.

---

### PATCH `/notes/<id>`

Updates one of the authenticated user's notes.

---

### DELETE `/notes/<id>`

Deletes one of the authenticated user's notes.

---

## Authentication

Protected routes require a JWT token in the request header.

Example:

```text
Authorization: Bearer YOUR_ACCESS_TOKEN
```

---

## Project Structure

```
productivity-api/
│
├── app.py
├── config.py
├── seed.py
├── README.md
├── models/
│   ├── dbconfig.py
│   ├── user.py
│   └── note.py
├── resources/
│   ├── auth.py
│   └── notes.py
├── schemas/
├── instance/
├── migrations/
├── Pipfile
└── Pipfile.lock
```

---

## Author

**Shanice Ambani**
