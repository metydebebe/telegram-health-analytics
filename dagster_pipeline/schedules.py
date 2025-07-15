from dagster import schedule
from dagster_pipeline.pipeline import telegram_data_pipeline

@schedule(
    cron_schedule="0 0 * * *",  # Every day at midnight UTC
    job=telegram_data_pipeline,
    execution_timezone="UTC"
)
def daily_telegram_pipeline_schedule():
    return {}  
