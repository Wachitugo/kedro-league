"""
This is a boilerplate pipeline 'process_raw_data'
generated using Kedro 0.19.7
"""

from kedro.pipeline import Pipeline,node 
from .nodes import load_arff_dataset 


def create_pipeline(**kwargs):
    return Pipeline(
        [
            node(
                func=load_arff_dataset,
                inputs="raw_arff_dataset",  
                outputs="arff_dataframe", 
                name="load_arff_data"
            ),
        ]
    )
