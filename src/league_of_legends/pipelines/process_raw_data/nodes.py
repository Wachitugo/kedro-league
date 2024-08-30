import pandas as pd
import arff

def load_arff_dataset(filepath: str) -> pd.DataFrame:
    with open(filepath, 'r') as f:
        arff_data = arff.load(f)
    
    df = pd.DataFrame(arff_data['data'], columns=[attr[0] for attr in arff_data['attributes']])
    
    return df