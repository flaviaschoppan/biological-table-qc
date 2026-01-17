import pandas as pd

def load_table(path):
    df = pd.read_csv(path)
    return df
