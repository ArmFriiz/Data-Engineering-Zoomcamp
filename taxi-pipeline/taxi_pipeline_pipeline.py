"""
DLT pipeline to ingest NYC taxi data from a REST API.

This pipeline fetches NYC taxi trip data from the Data Engineering Zoomcamp API and loads
it into a DuckDB database. The API returns paginated JSON responses with 1,000 records
per page, and pagination automatically stops when an empty page is encountered.

API Configuration:
- Base URL: https://us-central1-dlthub-analytics.cloudfunctions.net/data_engineering_zoomcamp_api
- Response Format: Paginated JSON with 1,000 records per page
- Pagination: Page-number based (page=1, page=2, etc.)

Data Load Flow:
1. REST API source fetches taxi data from the specified endpoint
2. Data is normalized and loaded into DuckDB
3. Pipeline state is managed automatically by dlt
"""

import dlt
from dlt.sources.rest_api import rest_api_resources
from dlt.sources.rest_api.typing import RESTAPIConfig


@dlt.source
def taxi_pipeline_source():
    """
    Define the NYC taxi data source using dlt REST API resources.

    This source configures the connection to the data engineering zoomcamp API
    and sets up pagination to fetch all available taxi trip records.

    Returns:
        Generator of REST API resources configured for taxi data ingestion
    """
    # Configure REST API connection and resources
    config: RESTAPIConfig = {
        "client": {
            # NYC taxi data API endpoint
            "base_url": "https://us-central1-dlthub-analytics.cloudfunctions.net/data_engineering_zoomcamp_api",
        },
        "resources": [
            {
                # Name of the resource - becomes the table name in the destination
                "name": "taxi_data",
                "endpoint": {
                    # Path relative to base_url (empty path "/" means root)
                    "path": "/",
                    # Configure page-number based pagination
                    # The API expects ?page=1, ?page=2, etc. in query parameters
                    "paginator": {
                        "type": "page_number",  # Use page number pagination
                        "page_param": "page",  # Query parameter name for the page number
                        "base_page": 1,  # Start pagination from page 1
                        "stop_after_empty_page": True,  # Stop when API returns empty page
                    },
                },
            },
        ],
    }

    # Yield REST API resources for dlt to process
    yield from rest_api_resources(config)


# Initialize the dlt pipeline
pipeline = dlt.pipeline(
    pipeline_name="taxi_pipeline",  # Pipeline name for state and schema management
    destination="duckdb",  # Store data in DuckDB
    refresh="drop_sources",  # Drop and recreate schema/state on each run (useful during development)
    progress="log",  # Log progress to stdout
)


if __name__ == "__main__":
    # Run the pipeline: fetch data from the source and load into DuckDB
    load_info = pipeline.run(taxi_pipeline_source())
    # Print execution summary including row counts, files processed, and load duration
    print(load_info)  # noqa: T201
