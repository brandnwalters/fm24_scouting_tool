import pandas as pd

def load_export(path: str):
    """Loading an FM export into a dataframe"""
    lower_path = path.lower()
    if lower_path.endswith('.csv'):
        df = pd.read_csv(filepath_or_buffer= path, sep = ";")
        return df
    elif lower_path.endswith('.html'):
        tables = pd.read_html(path)
        df = tables[0]
        return df
    else:
        raise ValueError("Path did not have .csv or .html")
    
METADATA_COLS = ["Inf", "RF Matches", "Name", "Club", "Position", "Transfer Value", "Salary",
                 "Rec", "Knowledge"]

def clean(df):
    """Normalizing the raw export"""
    stripped_cols = [col.strip() for col in df]
    df.columns = stripped_cols
    df = df.drop(columns = ['Inf', 'RF Matches', "Rec", 'Knowledge'], errors= 'ignore')
    attr_cols = [col for col in df.columns if col not in METADATA_COLS]
    for col in attr_cols:
        df[col] = pd.to_numeric(df[col], errors='coerce')
    return df