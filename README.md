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

    Scrape messages from specified public Telegram channels using the Telegram API via Telethon.

    Download and save images posted in those channels for later enrichment.

    Store all raw data as JSON files, preserving the original message structure.

    Organize raw data in a partitioned directory structure by date and channel.

    Implement logging to track scraping progress and errors for robustness.

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

The scraper connects to the Telegram API using stored credentials in .env.

For each channel:

It fetches up to 200 recent messages.

Checks for media (images) and downloads them to the designated folder.

Saves all messages as a JSON array in a file named {channel_name}.json under the date folder.

Logs are saved in the logs/ directory with timestamps to track scraping sessions and errors.

## Running the Scraper

Ensure your .env file contains valid:

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

# Task 2: Data Modeling & Transformation with dbt

## Goal

Transform raw Telegram message data stored in JSON format into a clean, analytics-ready star schema using dbt (data build tool).

## Setup

Install dbt and PostgreSQL adapter:
pip install dbt-core dbt-postgres

Initialize dbt project:
dbt init telegram_analytics
Configure your profiles.yml (in ~/.dbt/) to connect to PostgreSQL:

telegram_analytics:
target: dev
outputs:
dev:
type: postgres
host: localhost
user: postgres
password: **\*\*\***
port: 5432
dbname: telegram_db
schema: raw

## Model Structure

I follow a layered dbt model structure:

models/
├── staging/
│ └── stg_telegram_messages.sql
└── marts/
└── messages/
├── dim_channels.sql
├── dim_dates.sql
└── fct_messages.sql
stg_telegram_messages.sql

Casts raw JSON into structured columns and extracts key fields like id, channel_id, message, and media.

dim_channels.sql
A dimension table capturing distinct Telegram channel IDs and synthetic channel names.

dim_dates.sql
A time dimension table based on unique message dates for temporal analysis.

fct_messages.sql
A fact table containing each message with metadata like length, has_image, and foreign keys to dim_channels and dim_dates.

## Tests & Validation

Used built-in dbt tests (not_null, unique) to validate model quality:

fct_messages.message_id: must be not_null and unique

fct_messages.sent_at: must be not_null

Custom data tests can be added in tests/ directory for advanced business rules.

## Run & Document

Run models:
dbt run

Run tests:
dbt test

Generate documentation:
dbt docs generate
dbt docs serve

## Outcome

By the end of this task, I’ve created a modular, testable, and documented dbt transformation layer converting messy Telegram message data into a trusted star schema for analytics and reporting.

# Task 3 - Data Enrichment with Object Detection (YOLOv8)

## Overview

This task enhances the Telegram data pipeline by applying computer vision techniques to analyze images associated with Telegram messages. Using a modern, pre-trained YOLOv8 model, the pipeline detects objects within images and integrates the detection results into the data warehouse for enriched analysis.

## Setup & Dependencies

- Install the required package for YOLOv8:
  pip install ultralytics

Ensure your Python environment includes access to the raw Telegram messages and associated images scraped in Task 1.

## Process

Image Collection
The script scans the folder where Task 1 stored scraped Telegram images (e.g., data/images/).

## Object Detection

Using the YOLOv8 pre-trained model, the script processes each image and detects objects along with confidence scores.

## Result Formatting

The detection results are stored in a structured JSON file containing:

Image filename

Detected object class ID

Confidence score

Database Integration

Create the raw_yolo_detections table in the raw schema to store raw detection data.

Use dbt models to transform raw detections into the fact table fct_image_detections, linking detections to Telegram messages via foreign keys.

## Key Files & Structure

scripts/yolo_detector.py
Script performing object detection using YOLOv8.

models/staging/stg_yolo_detections.sql
Staging model to clean and standardize YOLO detection data.

models/marts/messages/fct_image_detections.sql
Fact table model that integrates image detections with message data for analysis.

## How to Run

Execute the detection script manually or schedule it as part of your pipeline:

python scripts/yolo_detector.py
Load the raw detection JSON output into the PostgreSQL table raw_yolo_detections.

Run dbt models to process and materialize enriched detection data:

dbt run --select stg_yolo_detections fct_image_detections

## Notes

Make sure the raw images are up-to-date before running detection.

Tune the YOLO model or confidence thresholds as needed for accuracy.

Integration with the overall pipeline is recommended for automated end-to-end processing.
