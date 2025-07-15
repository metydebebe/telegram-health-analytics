from dagster import repository
from dagster_pipeline.pipeline import telegram_data_pipeline
from dagster_pipeline.schedules import daily_telegram_pipeline_schedule

@repository
def telegram_repo():
    return [telegram_data_pipeline, daily_telegram_pipeline_schedule]
