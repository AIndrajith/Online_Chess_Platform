# Online Multiplayer Chess Platform ♟️

A **backend-first, production-style online multiplayer chess platform** built using **Python and FastAPI**, with a strong emphasis on clean architecture, real-time communication, and scalable system design.

> 🚧 **Project Status:** In Progress (Active Development)  
> 🛠️ **Current Phase:** Backend core services & authentication foundation

---

## 🎯 Project Objective

The objective of this project is to design and implement a **real-time online chess platform** where two remote players can play a complete chess game with:

- Enforced chess rules
- Live move synchronization
- Secure user authentication
- Persistent game state storage

This project is developed using a **real-world backend engineering approach**, focusing on maintainability, correctness, and production readiness rather than rapid feature delivery.

---

## 🧱 Technology Stack

### Backend
- Python 3.11
- FastAPI
- WebSockets (planned for real-time gameplay)

### Chess Logic
- python-chess (planned)

### Database
- MySQL
- SQLAlchemy ORM

### Frontend
- HTML, CSS, JavaScript  
  (served by FastAPI — planned)

### DevOps & Deployment
- Docker (planned)
- Docker Compose (planned)

### Tooling
- Git & GitHub
- Virtual Environment (venv)

---

## 📌 Current Implementation Status

### ✅ Completed
- FastAPI application initialized
- Backend entry point (`main.py`) established
- Health / proof-of-life endpoint implemented
- Database connection layer (MySQL + SQLAlchemy)
- Shared SQLAlchemy Base for all ORM models
- User ORM model defined
- Database table initialization handled via SQLAlchemy
- Password hashing & verification utilities
- User creation service (no login flow yet)

### 🚧 In Progress / Planned
- User authentication (login flow)
- Password verification during login
- Token/session handling
- WebSocket-based game communication
- Chess rule enforcement
- Game state persistence
- Frontend user interface
- Containerized deployment

At this stage, the focus is on **backend correctness and architecture**, not feature completeness.

---

## 🏗️ Project Structure

```text
online-chess/
│
├── app/
│   ├── main.py                # FastAPI application entry point
│   │
│   ├── database/
│   │   ├── database.py        # Database engine & session factory
│   │   └── deps.py            # Database dependency provider
│   │
│   ├── models/
│   │   ├── base.py            # Shared SQLAlchemy Base
│   │   └── user.py            # User ORM model
│   │
│   ├── services/
│   │   ├── security.py        # Password hashing & verification
│   │   └── user_service.py    # User creation business logic
│   │
│   └── routes/                # API routes (planned)
│
├── frontend/                  # Frontend UI (planned)
├── tests/                     # Automated tests (planned)
├── docs/                      # Project documentation
├── requirements.txt
└── README.md
