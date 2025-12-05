import pandas as pd

def load_tce_catalog(path):
    df = pd.read_csv(path)
    df.columns = df.columns.str.lower()
    return df

def clean_tce(df):
    df = df.dropna(subset=["tce_period", "tce_time0bk", "tce_duration"])
    df = df[df["tce_period"] > 0]
    df = df[df["tce_duration"] > 0]
    return df

def preprocess_tce(path):
    df = load_tce_catalog(path)
    df = clean_tce(df)
    return df
    