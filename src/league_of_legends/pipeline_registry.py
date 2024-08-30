"""Project pipelines."""
from typing import Dict

from kedro.framework.project import find_pipelines
from kedro.pipeline import Pipeline
from .pipelines import process_raw_data as process_raw_data_pipeline


def register_pipelines() -> Dict[str, Pipeline]:
    """Register the project's pipelines.

    Returns:
        A mapping from pipeline names to ``Pipeline`` objects.
    """
    "process_raw_data": process_raw_data_pipeline.create_pipeline()
    "__default__": process_raw_data_pipeline.create_pipeline()

    pipelines = find_pipelines()
    pipelines["__default__"] = sum(pipelines.values())
    return pipelines
