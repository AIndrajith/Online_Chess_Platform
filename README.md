# Online Multiplayer Chess Platform ♟️

A **backend-first, production-style online multiplayer chess platform** built using **Python and FastAPI**, focusing on **clean architecture, scalability, and real-time system design**.

> 🚧 **Project Status:** In Progress (Actively Developing)
> 🛠️ **Current Phase:** Game domain modeling & core gameplay APIs

---

## 🎯 Project Objective

The goal of this project is to build a **real-time multiplayer chess system** where two players can:

* Create and join games
* Play chess with synchronized state
* Persist game progress reliably
* Interact through a scalable backend system

This project emphasizes:

* Backend architecture
* Data modeling
* System correctness
* Interview-ready engineering practices

---

## 🧱 Technology Stack

### Backend

* Python 3.11
* FastAPI
* SQLAlchemy (ORM)
* WebSockets *(planned)*

### Database

* MySQL

### Chess Logic

* python-chess *(planned for move validation & rules)*

### Frontend

* HTML, CSS, JavaScript *(planned)*

### DevOps

* Docker & Docker Compose *(planned)*

---

## 📌 Current Implementation Status

### ✅ Completed

#### 🔹 Core Backend Setup

* FastAPI application initialized
* Health check endpoint (`/health`)
* Modular project structure

#### 🔹 Database Layer

* MySQL connection with SQLAlchemy
* Session management via dependency injection
* Shared declarative Base

#### 🔹 User System

* User ORM model
* Password hashing using `passlib`
* User creation service

#### 🔹 Chess Game Domain (Day 7)

* Game ORM model with role-based player mapping:

  * `creator_id`
  * `white_player_id`
  * `black_player_id`
* Board state stored using **FEN notation**
* Game lifecycle management:

  * `waiting` → `in_progress`
* Game services:

  * `create_game`
  * `join_game`
* API endpoints:

  * `POST /games/create`
  * `POST /games/join/{game_id}`

---

### 🚧 In Progress / Next Steps

* User authentication (login flow)
* Token-based authentication (JWT)
* Move handling & validation (python-chess)
* WebSocket-based real-time gameplay
* Concurrency handling (race conditions in joins)
* Game history tracking
* Frontend chess UI
* Dockerized deployment

---

## 🏗️ Project Structure

```text
Backend/
 └── app/
     ├── main.py                # FastAPI entry point
     │
     ├── database/
     │   ├── base.py            # SQLAlchemy Base
     │   ├── database.py        # Engine & session
     │   └── deps.py            # Dependency injection (DB session)
     │
     ├── models/
     │   ├── user.py            # User model
     │   └── game.py            # Game model
     │
     ├── services/
     │   ├── security.py        # Password hashing
     │   ├── user_service.py    # User logic
     │   └── game_service.py    # Game logic
     │
     └── api/
         └── game_router.py     # Game endpoints
```

---

## 🧠 Key Design Decisions

### 🔸 Role-Based Player Modeling

Players are stored as:

* `white_player_id`
* `black_player_id`

This avoids ambiguity and simplifies game logic.

---

### 🔸 FEN-Based State Storage

Game state is stored as a single **FEN string**, which:

* Encodes full board state
* Simplifies persistence
* Integrates directly with chess engines

---

### 🔸 Separation of Concerns

* Models → database schema
* Services → business logic
* API → request handling

---

### 🔸 Concurrency Awareness

The system is designed with awareness of **race conditions**, especially in multiplayer joins. Future improvements will include transaction safety and locking mechanisms.

---

## 🚀 How to Run

```bash
uvicorn Backend.app.main:app --reload
```

Then open:

```
http://127.0.0.1:8000/docs
```

---

## 💡 Interview Talking Points

This project demonstrates:

* Backend system design
* Relational data modeling
* REST API development
* Dependency injection (FastAPI)
* Handling of real-world issues like race conditions
* Scalable architecture planning

---
