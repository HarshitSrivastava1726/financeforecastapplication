import pandas as pd

REQUIRED_COLS = ["date", "amount", "type"]

def load_file(file):
    df = pd.read_excel(file)
    df.columns = df.columns.str.lower()

    missing = set(REQUIRED_COLS) - set(df.columns)
    if missing:
        raise ValueError(f"Missing columns: {missing}")

    df["date"] = pd.to_datetime(df["date"])
    return df
