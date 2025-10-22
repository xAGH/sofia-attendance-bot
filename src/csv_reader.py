import pandas as pd


def load_absences(csv_url: str):
    df = pd.read_csv(csv_url)
    df = df.fillna("")
    records = df.to_dict(orient="records")
    return records
