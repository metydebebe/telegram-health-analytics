from dagster import op, job

@op
def scrape_telegram_data():
    # call your scraping script or function here
    print("Scraping telegram data...")
    # simulate returning some result (can be None if not needed)
    return "scraped_data"

@op
def load_raw_to_postgres(scraped_data):
    # call your loading script here, use scraped_data if needed
    print(f"Loading raw data to Postgres with input: {scraped_data}")
    return "loaded_data"

@op
def run_dbt_transformations(loaded_data):
    # call dbt run commands here, use loaded_data if needed
    print(f"Running dbt transformations with input: {loaded_data}")
    return "transformed_data"

@op
def run_yolo_enrichment(transformed_data):
    # call YOLO enrichment script here, use transformed_data if needed
    print(f"Running YOLO enrichment with input: {transformed_data}")
    return "yolo_results"

@job
def telegram_data_pipeline():
    scraped = scrape_telegram_data()
    loaded = load_raw_to_postgres(scraped)
    transformed = run_dbt_transformations(loaded)
    yolo = run_yolo_enrichment(transformed)
