# Quiz Application (Django) – with Timed MCQs & ML‑Powered Proctoring

A production‑ready Django-based quiz platform featuring secure user authentication, timed multiple‑choice assessments, real‑time session management (auto‑submit on expiry), and ML-powered facial detection for remote proctoring.

---

## ✨ Features

* **Authentication & Roles**: Secure sign up / login (Django auth). Roles for **Admin/Instructor** and **Student**.
* **Quiz Builder**: Create quizzes with sections, MCQs (single/multi-select), points, negative marking (optional), and time limit.
* **Taking Quizzes**: Clean UI, per-quiz timer, autosave of answers, prevention of multiple attempts (configurable), and **automatic submission** when time expires.
* **Real‑Time Management**: Live session tracking; instructor can monitor attempt status.
* **Proctoring (ML)**: Browser camera capture + backend checks for **face presence**, **multiple faces**, and **face mismatch** (optional). Suspicious events are logged and can auto‑submit based on policy.
* **Integrity Controls**: Fullscreen enforcement (optional), tab‑switch/blur detection, copy/paste prevention (optional).
* **Results & Analytics**: Instant scores (configurable), per‑question breakdown, export to CSV.
* **API-Ready**: JSON endpoints for SPA/mobile integrations.

---

## 🧱 Tech Stack

* **Backend**: Django, Django REST Framework (optional), Celery/Redis (optional for async tasks)
* **DB**: SQLite (dev) → PostgreSQL/MySQL (prod)
* **Frontend**: Django templates (or your SPA)
* **Proctoring**: WebRTC `getUserMedia` on client; OpenCV/MediaPipe/face-recognition model on server
* **Realtime** (optional): Django Channels + Redis

---

## 📦 Project Structure (example)

```
quiz_app/
├─ manage.py
├─ requirements.txt
├─ .env.example
├─ core/                 # settings, urls, asgi/wsgi
├─ accounts/             # auth, roles, profiles
├─ quizzes/              # quiz, question, option, attempt models
├─ proctoring/           # camera capture endpoints, validators
├─ api/                  # DRF serializers & viewsets (optional)
└─ static/ templates/    # assets & HTML templates
```

---

## 🚀 Quickstart

### 1) Clone & create environment

```bash
git clone <your-repo-url> quiz-app
cd quiz-app
python -m venv .venv
source .venv/bin/activate   # Windows: .venv\Scripts\activate
pip install -r requirements.txt
```

### 2) Configure environment

Create `.env` (or export env vars) based on `.env.example`:

```
# Core
SECRET_KEY=change-me
DEBUG=True
ALLOWED_HOSTS=*

# Database (SQLite by default; for Postgres use DATABASE_URL)
# DATABASE_URL=postgres://user:pass@host:5432/dbname

# Proctoring
PROCTORING_ENABLED=true
PROCTORING_FRAME_INTERVAL_MS=1500
PROCTORING_MAX_WARNINGS=3
PROCTORING_AUTO_SUBMIT=true
FACE_MODEL_PATH=proctoring/models/shape_predictor.dat
FACE_RECOGNITION_ENABLED=false

# Channels/Redis (optional)
# CHANNEL_LAYERS=redis://localhost:6379/1
```

### 3) Migrate & create admin

```bash
python manage.py migrate
python manage.py createsuperuser
```

### 4) Run

```bash
python manage.py runserver
```

Open: [http://127.0.0.1:8000/](http://127.0.0.1:8000/)

---

## 👩‍🏫 Usage

### Instructors

1. Login as admin → **Quizzes → Create**
2. Add questions (single/multi‑select), set **time limit**, optional **negative marking**
3. Publish and share the join link/access code

### Students

1. Sign up / Login
2. Open quiz → **Allow camera** (if proctoring enabled)
3. Stay focused: switching tabs/fullscreen may trigger warnings
4. Answers autosave; on time expiry the attempt **auto‑submits**

---

## 🛡️ Proctoring (How it works)

* **Client**: Uses `navigator.mediaDevices.getUserMedia({ video: true })` to access the webcam. Periodically captures frames (canvas snapshots) and posts to `/proctoring/frame/`.
* **Server**: Runs lightweight models (OpenCV/MediaPipe). Checks:

  * **Face present**: No face → warning
  * **Multiple faces**: >1 face → warning
  * **Face mismatch (optional)**: Compare embeddings with enrolled face
  * **Environment anomalies (optional)**: sudden lighting/pose extremes
* **Policy**: After `PROCTORING_MAX_WARNINGS`, system can **auto‑submit** or **flag** the attempt for manual review.
* **Privacy**: Frames are processed transiently; storage is **configurable** (default: not persisted). Show a consent notice before the quiz.

> ⚠️ **Disclaimer**: Computer vision signals are probabilistic. Keep a manual review path and accessibility alternative for legitimate cases (e.g., lighting, hardware limits).

---

## 🔒 Security Best Practices

* Use HTTPS (TLS), secure cookies, CSRF protection (Django default)
* Rotate `SECRET_KEY` and keep it out of VCS
* Set `DEBUG=False` and proper `ALLOWED_HOSTS` in production
* Validate quiz/attempt ownership on every request
* Rate‑limit proctoring frame uploads (interval + size caps)
* CORS/Content‑Security‑Policy if exposing APIs

---

## 🗃️ Data Model (simplified)

* `Quiz(title, description, time_limit, published, created_by)`
* `Question(quiz, text, type, points, negative_points)`
* `Option(question, text, is_correct)`
* `Attempt(user, quiz, started_at, submitted_at, score, status)`
* `Answer(attempt, question, selected_options[])`
* `ProctorEvent(attempt, kind, severity, note, ts)`

---

## 🧩 API (sample endpoints)

```
GET    /api/quizzes/
POST   /api/quizzes/
GET    /api/quizzes/{id}/
POST   /api/quizzes/{id}/questions/
POST   /api/attempts/{id}/answers/
POST   /api/attempts/{id}/submit/
POST   /proctoring/frame/           # receives image frames
GET    /proctoring/events?attempt=  # instructor review
```

---

## 🧪 Testing

```bash
pytest -q
# or
python manage.py test
```

Recommended: factory\_boy, pytest-django, coverage.

---

## 📦 Deployment

* **Docker**: Provide a `Dockerfile` and `docker-compose.yml` (Django + Postgres + Redis)
* **Static files**: `collectstatic` to S3 or mounted volume
* **Workers**: Run Celery worker/beat if using async tasks
* **ASGI**: For realtime (Channels), use Daphne/Uvicorn behind Nginx

---

## 🗺️ Roadmap

* Question pools & randomized sections
* Descriptive/subjective questions with rubric grading
* Enhanced analytics and per‑tag difficulty
* Mobile app (same API)

---

## 🤝 Contributing

PRs welcome! Please open an issue for discussion first. Follow conventional commits and run tests before pushing.

---

## 📝 License

Choose a license (e.g., MIT) and place it in `LICENSE`.

---

## 🙌 Acknowledgements

* Django, DRF, OpenCV/MediaPipe/face-recognition community
* Everyone who reported bugs & suggested features
