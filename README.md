# Telegram Health Analytics

# Task 0: Project Setup & Environment Management

This project sets up a reproducible development environment for building a full-stack data pipeline to analyze Ethiopian medical businesses using data from public Telegram channels.

---

## Objective

Ensure a robust, modular, and reproducible base environment that supports:

- Dockerized development
- Python dependency management
- Secure secret handling
- PostgreSQL data storage
- Modular project organization

---

## Folder and File Structure

telegram-health-analytics/
├── config/ # Configuration logic (env loader, constants)
│ └── config.py
├── .gitignore # Prevents committing secrets, virtualenv, etc.
├── .env # Local secrets (API keys, DB URL)
├── requirements.txt # All Python dependencies
├── Dockerfile # Container setup
├── docker-compose.yml # Container orchestration
├── README.md
