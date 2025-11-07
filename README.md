# Quiz Application (Django) – Timed MCQs with Basic Proctoring

A Django-based quiz platform where users can register, attempt multiple-choice quizzes within a time limit, and receive instant results. The app also includes basic browser-based proctoring (fullscreen enforcement and tab-switch detection) to maintain quiz integrity.

---

## 🧠 Distinctiveness and Complexity

This project satisfies the **CS50W distinctiveness and complexity** requirements because:

* Unlike the e-commerce and social network projects from the course, this is a **quiz/assessment system**, designed specifically for online exams and timed evaluations.
* It implements **timed MCQs with auto-submission**, which adds backend logic (quiz timing, submission validation) and frontend interaction (JavaScript countdown, autosubmit on timeout).
* The project integrates **Django models**, forms, authentication, and **JavaScript interactivity** (timer, alerts, and restricted actions during the quiz).
* Each quiz supports **multiple questions and options**, dynamic question loading, and result calculation with real-time validation.
* The system is **mobile-responsive**, built with Django templates and CSS media queries.
* It demonstrates **full-stack functionality**:
  - Django models, views, templates, and URL routing
  - JavaScript timers and user-interaction monitoring on the client side
  - Secure user authentication and data management using Django’s `User` model

In short, this project combines both **backend complexity** (data modeling, authentication, quiz logic) and **frontend logic** (timed submission, input validation) to deliver a fully functional, distinct web application.

---

## ✨ Features

* **User Authentication** – Secure login and registration (using Django’s built-in auth system)
* **Create & Manage Quizzes** – Admins or creators can add quizzes with multiple questions and options  
* **Timed Quizzes** – Each quiz has a defined time limit; auto-submission when time expires  
* **Answer Validation** – Correct answers stored in the database; automatic scoring after submission  
* **Results Page** – Displays total score, correct answers, and percentage achieved  
* **Basic Proctoring** – Detects tab switch or fullscreen exit (via JavaScript warnings)  
* **Mobile-Responsive UI** – Works smoothly across devices  

---

## 🧱 Tech Stack

* **Backend** – Django (Python)
* **Frontend** – HTML, CSS, JavaScript (for timers and proctoring)
* **Database** – SQLite (for development)
* **Auth** – Django’s built-in `User` model and session management

---

## 🗃️ Data Model (from `models.py`)

* `Quiz`: Stores quiz details (title, description, creator, time limit)
* `Question`: Stores questions, options (A–D), and correct answers
* `Answer`: Stores user responses for each question
* `QuizResult`: Stores final score, total marks, and timestamp

---

## 📁 File Overview

```
quiz_app/
├─ manage.py                  # Django management script
├─ requirements.txt           # Dependencies list
├─ core/                      # Project settings and URLs
│   ├─ settings.py
│   ├─ urls.py
│   ├─ wsgi.py
│   └─ asgi.py
├─ quizzes/                   # Main app
│   ├─ models.py              # Quiz, Question, Answer, QuizResult models
│   ├─ views.py               # Logic for creating, attempting, and viewing results
│   ├─ urls.py                # App-specific URL routes
│   ├─ templates/quizzes/     # HTML templates (list, attempt, result, etc.)
│   ├─ static/quizzes/        # JS (timers, proctoring), CSS files
│   └─ forms.py               # Django forms for quiz creation (if applicable)
├─ templates/                 # Base templates
├─ static/                    # Global static files
└─ db.sqlite3                 # SQLite database (auto-created)
```

---

## 🚀 How to Run Locally

### 1. Clone and Setup Environment

```bash
git clone <your-repo-url> quiz-app
cd quiz-app
python -m venv .venv
source .venv/bin/activate   # Windows: .venv\Scripts\activate
pip install -r requirements.txt
```

### 2. Migrate Database

```bash
python manage.py migrate
```

### 3. Create a Superuser (for quiz creation)

```bash
python manage.py createsuperuser
```

### 4. Run the Development Server

```bash
python manage.py runserver
```

Then open [http://127.0.0.1:8000/](http://127.0.0.1:8000/) in your browser.

---

## 👩‍🏫 Usage

### For Admin/Creator
1. Log in as superuser from the Django admin panel (`/admin/`)
2. Create quizzes and add questions (with correct answers and time limits)
3. Share quiz URLs with users or students

### For Students
1. Sign up and log in
2. Choose a quiz and start it
3. Answer MCQs before the timer ends
4. Quiz auto-submits when time runs out or user manually submits
5. View score and percentage on the results page

---

## 🕒 Timed Quiz & Auto-Submission

The quiz page includes a **JavaScript countdown timer** that:
* Starts when the quiz begins  
* Shows remaining time  
* Auto-submits when time expires  
* Prevents multiple submissions  

This ensures fairness and consistency during attempts.

---

## 🔐 Security & Integrity

* CSRF protection (Django default)
* Authenticated routes for quiz attempts and results
* Tab-switch / fullscreen detection to prevent cheating
* Time tracking handled on both client (JS) and server (validation)

---

## 🔮 Future Scope

The following advanced features are **planned but not yet implemented**:

* **Role Management** – Distinct dashboards and permissions for Admins/Instructors and Students  
* **ML-Powered Proctoring** – Using webcam + OpenCV/MediaPipe for:
  - Face detection and recognition  
  - Multiple-face detection  
  - Automatic warnings and submission on policy violations  
* **Question Randomization & Pools** – Randomized question selection for each attempt  
* **Advanced Analytics** – Per-question performance stats and export options  
* **API Endpoints** – For integration with mobile apps or SPAs  
* **Real-Time Monitoring** – Instructor live dashboard for ongoing attempts  

---

## 🧪 Testing

Run built-in Django tests or use pytest (optional):

```bash
python manage.py test
```

---

## 📦 Deployment

* Production database: PostgreSQL or MySQL  
* Static files: Use `collectstatic` for deployment  
* Environment variables stored in `.env` (e.g., `SECRET_KEY`, `DEBUG`, etc.)  
* Host using services like Render, Railway, or Heroku  

---

## 🙌 Acknowledgements

* [CS50 Web Programming with Python and JavaScript](https://cs50.harvard.edu/web/)
* Django documentation and community
* Open-source developers behind Django, Bootstrap, and JavaScript libraries used
