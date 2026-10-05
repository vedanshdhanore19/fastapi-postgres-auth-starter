# 🚀 FastAPI PostgreSQL Auth Starter

<p align="center">
  <b>A production-ready FastAPI authentication backend powered by PostgreSQL, SQLAlchemy, Alembic, Pydantic, JWT, and Argon2.</b>
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.10%2B-3776AB?style=for-the-badge&logo=python&logoColor=white" alt="Python">
  <img src="https://img.shields.io/badge/FastAPI-0.1%2B-009688?style=for-the-badge&logo=fastapi&logoColor=white" alt="FastAPI">
  <img src="https://img.shields.io/badge/PostgreSQL-15%2B-4169E1?style=for-the-badge&logo=postgresql&logoColor=white" alt="PostgreSQL">
  <img src="https://img.shields.io/badge/SQLAlchemy-ORM-D71F00?style=for-the-badge&logo=sqlalchemy&logoColor=white" alt="SQLAlchemy">
  <img src="https://img.shields.io/badge/Alembic-Migrations-6BA81E?style=for-the-badge" alt="Alembic">
  <img src="https://img.shields.io/badge/uv-Package%20Manager-DE5FE9?style=for-the-badge" alt="uv">
</p>

<p align="center">
  <a href="#-features">Features</a> •
  <a href="#-tech-stack">Tech Stack</a> •
  <a href="#-project-structure">Structure</a> •
  <a href="#-getting-started">Getting Started</a> •
  <a href="#-api-endpoints">API</a> •
  <a href="#-authentication">Authentication</a>
</p>

---

## 📌 About The Project

**FastAPI PostgreSQL Auth Starter** is a modern backend boilerplate designed to help developers quickly build secure and scalable REST APIs with authentication.

The project combines **FastAPI**, **PostgreSQL**, **SQLAlchemy**, **Alembic**, **Pydantic**, **JWT**, and **Argon2 password hashing** into a clean and extensible architecture.

Instead of starting authentication and database configuration from scratch, you can clone this project and immediately begin building your application on top of it.

---

## ✨ Features

### ⚡ FastAPI

- High-performance Python web framework
- Automatic request validation
- Automatic OpenAPI schema generation
- Interactive Swagger documentation
- Clean API routing architecture

### 🐘 PostgreSQL

- Reliable relational database
- Production-ready database engine
- Structured user and application data
- SQLAlchemy ORM integration

### 🗃️ SQLAlchemy

- Object Relational Mapping
- Python-based database models
- Database queries without writing raw SQL for common operations
- Easy integration with FastAPI dependencies

### 🔄 Alembic

- Database schema migrations
- Version-controlled database changes
- Upgrade and downgrade support
- Safe schema evolution during development

### 🔐 Authentication & Security

- JWT-based authentication
- Secure password hashing
- Argon2 password hashing through `pwdlib`
- Pydantic request validation
- Protected API endpoints
- Secure credential handling

### 📦 uv

- Extremely fast Python package management
- Virtual environment management
- Dependency locking
- Reproducible development environment

---

## 🛠️ Tech Stack

| Technology | Purpose |
|------------|---------|
| 🐍 **Python** | Programming language |
| ⚡ **FastAPI** | REST API framework |
| 🐘 **PostgreSQL** | Relational database |
| 🗃️ **SQLAlchemy** | ORM |
| 🔄 **Alembic** | Database migrations |
| 🔐 **PyJWT** | JWT token handling |
| 🛡️ **pwdlib** | Secure password hashing |
| ✅ **Pydantic** | Data validation |
| 📦 **uv** | Package & environment management |

---

# 📁 Project Structure

A typical project structure looks like this:

```text
fastapi-postgres-auth-starter/
│
├── app/
│   ├── database/
│   │   ├── schema/
│   │   │   ├── __init__.py
│   │   │   ├── user_schema.py
│   │   │   └── ...
│   │   │
│   │   ├── db.py
│   │   └── ...
│   │
│   ├── models/
│   │   ├── auth.py
│   │   └── ...
│   │
│   ├── routing/
│   │   ├── auth.py
│   │   ├── todo.py
│   │   └── ...
│   │
│   ├── helper.py
│   └── app.py
│
├── alembic/
│   ├── versions/
│   ├── env.py
│   └── ...
│
├── .env
├── alembic.ini
├── main.py
├── pyproject.toml
├── uv.lock
└── README.md