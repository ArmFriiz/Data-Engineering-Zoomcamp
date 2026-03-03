"""Pipeline to ingest NYC taxi data from Data Engineering Zoomcamp API."""

import dlt
from dlt.sources.rest_api import rest_api_source


@dlt.source
def taxi_pipeline():
    """Define dlt resources from NYC taxi REST API."""
    config = {
        "client": {
            "base_url": "https://us-central1-dlthub-analytics.cloudfunctions.net/data_engineering_zoomcamp_api",
        },
        "resources": [
            {
                "name": "taxi_data",
                "endpoint": {
                    "path": "",
                    "params": {
                        "limit": 1000,
                    },
                    "paginator": {
                        "type": "offset",
                        "limit": 1000,
                        "offset": 0,
                        "offset_param": "offset",
                        "limit_param": "limit",
                    },
                },
            },
        ],
    }

    yield from rest_api_source(config)


if __name__ == "__main__":
    # Create pipeline with dev_mode for development
    pipeline = dlt.pipeline(
        pipeline_name="taxi_pipeline",
        destination="duckdb",
        dataset_name="nyc_taxi",
        dev_mode=True,
        progress="log",
    )

    # Run the pipeline
    load_info = pipeline.run(taxi_pipeline())
    print(load_info)  # noqa: T201
