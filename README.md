# Backend Engineering Foundations

This repository contains foundational backend engineering concepts implemented in Python.

## Concepts Covered
- Object-Oriented Programming
- Service-based architecture
- Asynchronous programming
- Defensive coding and validation
- Custom exception handling

## Structure
- `models/` – Data models
- `services/` – Business logic
- `exceptions.py` – Domain-specific errors
- `main.py` – Application entry point

## Purpose
This project is part of a structured backend engineering roadmap focused on building production-ready, secure systems.

## Tech Stack
- FastAPI
- PostgreSQL
- SQLAlchemy (async)
- Pydantic

## Features
- User creation API
- Async database persistence
- Dependency injection
- Environment-based configuration

## Setup
1. Create PostgreSQL database
2. Configure `.env`
3. Install dependencies
4. Run `uvicorn app.main:app --reload`