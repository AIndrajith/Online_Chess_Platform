# Online Multiplayer Chess Platform ♟️

A **backend-first, production-style online multiplayer chess platform** built using **Python and FastAPI**, focusing on clean architecture, real-time communication, and scalable system design.

> 🚧 **Project Status:** In Progress (Active Development)  
> 🛠️ **Current Phase:** Backend foundation & database connectivity

---

## 🎯 Project Objective

The objective of this project is to design and build a **real-time online chess platform** where two remote players can play a complete chess game with:

- Enforced chess rules
- Live move synchronization
- User authentication
- Persistent game state

The project is developed using a **real-world backend engineering approach**, emphasizing clear separation of concerns, maintainability, and production readiness.

---

## 🧱 Technology Stack

### Backend
- Python 3.11
- FastAPI
- WebSockets (planned)

### Chess Logic
- python-chess (planned)

### Database
- MySQL
- SQLAlchemy (ORM)

### Frontend
- HTML, CSS, JavaScript  
  (served by FastAPI — planned)

### DevOps & Deployment
- Docker
- Docker Compose

### Tooling
- Git & GitHub
- Virtual Environment (venv)

---

## 📌 Current Implementation Status

✅ FastAPI application initialized  
✅ Backend entry point (`main.py`) established  
✅ Health / proof-of-life endpoint implemented  
✅ Database connection layer created (MySQL + SQLAlchemy)  
🚫 No database tables or models yet  
🚫 No business logic implemented yet  

This phase focuses on **infrastructure and architecture**, not features.

---

## 🏗️ Project Structure (Current)

```text
online-chess/
│
├── app/
│   ├── main.py              # FastAPI application entry point
│   └── database/
│       ├── database.py      # Database engine & session factory
│       └── deps.py          # Database dependency provider
│
├── frontend/                # Frontend (planned)
├── tests/                   # Automated tests (planned)
├── docs/                    # Documentation
├── requirements.txt
└── README.md
