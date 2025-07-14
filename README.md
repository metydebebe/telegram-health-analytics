# Telegram Health Analytics

# Task 0: Project Setup & Environment Management

This project sets up a reproducible development environment for building a full-stack data pipeline to analyze Ethiopian medical businesses using data from public Telegram channels.

## Objective

Ensure a robust, modular, and reproducible base environment that supports:

- Dockerized development
- Python dependency management
- Secure secret handling
- PostgreSQL data storage
- Modular project organization

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

# Task 1 - Data Scraping and Collection (Extract & Load)

## Overview

This task involves extracting data from selected public Telegram channels related to Ethiopian medical businesses, collecting both messages and images, and storing the raw data as JSON files in a structured Data Lake folder. The raw data serves as the foundation for later transformation and enrichment tasks.

## Channels Scraped

lobelia4cosmetics — https://t.me/lobelia4cosmetics

tikvahpharma — https://t.me/tikvahpharma

## Setup

Ensure .env file is created in the root with your Telegram API credentials:
env
TELEGRAM_API_ID=your_api_id
TELEGRAM_API_HASH=your_api_hash

Install dependencies:

pip install -r requirements.txt
The scraper is implemented as a Jupyter notebook (notebooks/telegram_scraper.ipynb) for improved control over execution and incremental scraping.

## Scraping Logic

The scraper connects to Telegram via Telethon using your credentials.

It iterates over the latest 200 messages per channel (configurable).

Messages are serialized into JSON, with datetime fields and bytes handled carefully to avoid serialization errors.

Images attached to messages are downloaded locally, and the path is saved in the message JSON.

Data is saved under:

data/raw/telegram_messages/YYYY-MM-DD/channel_name.json
data/raw/images/YYYY-MM-DD/channel_name/\*.jpg
Logging captures scraping progress and any errors (including Telegram API rate limits).

## Running the Scraper

Run the notebook cells step-by-step to scrape each channel.

Adjust the message limit parameter if needed for faster runs or larger datasets.

Check logs/scraper_YYYY-MM-DD.log for scraping details and troubleshooting.

## Data Quality and Validation

JSON files are verified for completeness and proper formatting after each run.

Message count per file matches expected limits (e.g., 200 messages per channel).

Serialization issues (datetime, bytes) have been handled in the notebook implementation.

## Notes

The data folder is .gitignored to avoid pushing raw data to version control.

The notebook approach allows manual control to prevent hitting Telegram API limits (FloodWaitError).

Future work includes automation and integration into an orchestrated pipeline with Dagster.
