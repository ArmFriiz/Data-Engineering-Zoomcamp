"""Pipeline for ingesting NYC taxi data from a REST API."""

import dlt
from dlt.sources.rest_api import rest_api_resources
from dlt.sources.rest_api.typing import RESTAPIConfig


@dlt.source
def taxi_pipeline_rest_api_source():
    """Define dlt resources from REST API endpoints."""
    config: RESTAPIConfig = {
        "client": {
            "base_url": "https://us-central1-dlthub-analytics.cloudfunctions.net/data_engineering_zoomcamp_api",
            "paginator": {
                "type": "offset",
                "limit": 1000,
                "offset": 0,
                "offset_param": "offset",
                "limit_param": "limit",
                "total_path": None,
                "stop_after_empty_page": True,
                "maximum_offset": 0,  # API cycles every 1000 records - set limit to 1 page
            },
        },
        "resources": [
            {
                "name": "taxi_data",
                "endpoint": {
                    "path": "",  # Root endpoint
                },
            },
        ],
    }

    yield from rest_api_resources(config)


pipeline = dlt.pipeline(
    pipeline_name="taxi_pipeline",
    destination="duckdb",
    dataset_name="nyc_taxi_data",
    progress="log",
)


if __name__ == "__main__":
    load_info = pipeline.run(taxi_pipeline_rest_api_source())
    print(load_info)  # noqa: T201
