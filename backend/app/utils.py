import os
import pandas as pd
#from langchain.schema import Document

def load_weather_data(filename="curated_data.csv"):
    # Resolve path: backend/app/ → backend/ → backend/data/curated_data.csv
    base_dir = os.path.dirname(os.path.dirname(__file__))
    file_path = os.path.join(base_dir, "data", filename)

    df = pd.read_csv(file_path)
    return df

def to_context_string(df, limit=20):
    return df.head(limit).to_string(index=False)
