# Online Multiplayer Chess Platform ♟️

A production-style **online multiplayer chess application** built using **Python and FastAPI**, focusing on real-time gameplay, clean backend architecture, and containerized deployment.

> 🚧 Project Status: **In Progress (Active Development)**

---

## 🎯 Project Goal

The goal of this project is to design and develop a **real-time online chess platform** where two remote players can play a complete chess game with:

- Enforced chess rules
- Live move synchronization
- User authentication
- Persistent game state

This project is being built with a **backend-first, engineering-focused approach**, following real-world software development practices.

---

## 🧱 Technology Stack

### Backend
- Python 3.11
- FastAPI
- WebSockets (for real-time gameplay)

### Chess Logic
- python-chess

### Database
- MySQL

### Frontend
- HTML, CSS, JavaScript  
  (served via FastAPI)

### DevOps & Deployment
- Docker
- Docker Compose

### Tooling
- Git & GitHub
- Virtual Environments (venv)

---

## 🏗️ Project Structure

```text
online-chess/
│
├── app/
│   ├── main.py            # FastAPI entry point
│   ├── websocket.py       # Real-time game handling
│   ├── models/            # Database models
│   ├── routes/            # API routes
│   ├── services/          # Business logic
│   └── database.py        # Database connection
│
├── frontend/              # Client-side UI
├── tests/                 # Automated tests
├── docs/                  # Documentation
├── requirements.txt
└── README.md
