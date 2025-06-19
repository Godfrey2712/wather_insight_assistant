import pandas as pd
from langchain.schema import Document

def load_weather_data(path="../data/curated_data.csv"):
    df = pd.read_csv(path)
    return df

def to_context_string(df, limit=20):
    return df.head(limit).to_string(index=False)