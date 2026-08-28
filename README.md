# 🎬 Movie Listing API

A backend API built with **FastAPI** as my capstone project for the AltSchool Africa Backend Engineering program.

The project demonstrates REST API development, user authentication, relational database modelling, validation, and automated testing.

## 🚀 Features

- User registration
- Password hashing with bcrypt
- JWT-based authentication
- Authenticated movie creation
- Comments on movies
- PostgreSQL database integration
- SQLAlchemy ORM
- Pydantic data validation
- Database migrations with Alembic
- Automated testing with Pytest

## 🛠 Tech Stack

**Backend:** Python, FastAPI  
**Database:** PostgreSQL  
**ORM:** SQLAlchemy  
**Validation:** Pydantic  
**Authentication:** JWT, Passlib/bcrypt  
**Database Migrations:** Alembic  
**Testing:** Pytest

## 📁 Project Structure

    movie_api/
    ├── app/
    │   ├── routers/
    │   │   ├── user.py
    │   │   ├── movie.py
    │   │   └── comment.py
    │   ├── config.py
    │   ├── database.py
    │   ├── dependencies.py
    │   ├── models.py
    │   ├── schemas.py
    │   ├── services.py
    │   ├── utils.py
    │   └── main.py
    ├── migrations/
    ├── tests/
    │   ├── test_users.py
    │   ├── test_movies.py
    │   └── test_comments.py
    ├── alembic.ini
    ├── requirements.txt
    └── README.md

## ⚙️ Setup

1. Clone the repository:

       git clone https://github.com/AgunloyeOS/movie_api.git
       cd movie_api

2. Create and activate a virtual environment.

3. Install dependencies:

       pip install -r requirements.txt

4. Create a PostgreSQL database.

5. Configure the required environment variables:

       DATABASE_URL=your_database_url
       SECRET_KEY=your_secret_key

6. Start the API:

       uvicorn app.main:app --reload

## 🧪 Testing

Run the test suite with:

    pytest

## 📚 API Documentation

Once the application is running, FastAPI provides interactive API documentation at:

    /docs

and alternative ReDoc documentation at:

    /redoc

## 🎓 Project Context

This project was developed as my capstone project during the AltSchool Africa Backend Engineering program.