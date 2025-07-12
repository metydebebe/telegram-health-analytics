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

In Task 1, I implemented the data scraping and collection pipeline to extract raw data from public Telegram channels related to Ethiopian medical businesses. The goal was to gather both textual messages and images, and store them in a structured data lake for further processing.

## Objectives

- Scrape messages from specified public Telegram channels using the Telegram API via Telethon
- Download and save images posted in those channels for later enrichment.
- Store all raw data as JSON files, preserving the original message structure.
- Organize raw data in a partitioned directory structure by date and channel.
- Implement logging to track scraping progress and errors for robustness.

## Scraped Channels

lobelia4cosmetics

tikvahpharma

## Folder Structure

data/
├── raw/
│ ├── telegram_messages/
│ │ └── YYYY-MM-DD/
│ │ ├── lobelia4cosmetics.json
│ │ ├── tikvahpharma.json
│ ├── images/
│ └── YYYY-MM-DD/
│ ├── lobelia4cosmetics/
│ │ ├── 123456.jpg
│ │ └── 123457.jpg

## How It Works

- The scraper connects to the Telegram API using stored credentials in .env.
- For each channel:
  It fetches up to 200 recent messages.
  Checks for media (images) and downloads them to the designated folder.
  Saves all messages as a JSON array in a file named {channel_name}.json under the date folder.
  Logs are saved in the logs/ directory with timestamps to track scraping sessions and errors.

## Running the Scraper

Ensure your .env file contains valid:

TELEGRAM_API_ID=your_api_id
TELEGRAM_API_HASH=your_api_hash

Run the scraper script:

python scripts/telegram_scraper.py
Check the data/raw/ directory for saved messages and images.

Review logs in logs/scraper_YYYY-MM-DD.log for detailed scraping info.

## Logging

Logging is set up to record the start, success, and failure of scraping per channel.

Errors like network issues or Telegram API limits are captured for troubleshooting.
