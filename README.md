# Movie Explorer Backend

A **Django REST Framework (DRF)** backend for exploring Movies, Actors, Directors, and Genres.  
The project runs entirely inside **Docker**, includes **Swagger API docs**, and enforces code quality with **Black, Flake8, Pytest, and Pre-commit**.

---

## Features

- Django + DRF (RESTful API)
- PostgreSQL as database (via Docker)
- Swagger (`/swagger/`) and ReDoc API docs
- Relationships:
  - Movies ↔ Genres (Many-to-Many)
  - Movies ↔ Actors (Many-to-Many)
  - Movies → Director (One-to-Many)
- Filtering:
  - Movies by genre, director, release year, or actor
  - Actors by movies or genres
- Pre-configured:
  - **Black** (formatter)
  - **Flake8** (linter)
  - **Pytest** (testing)
  - **Pre-commit hooks** (auto-format, lint, and test before commits)

---

## Getting Started

### 1. Clone the Repository
```bash
git clone https://github.com/manasmani104/movie-explorer-backend.git
cd movie-explorer-backend


