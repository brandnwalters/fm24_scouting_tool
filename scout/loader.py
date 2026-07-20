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
    
METADATA_COLS = ["Name", "Club", "Position", "Age", "Transfer Value", "Salary", "Aer", "Cmd",
                 "Com", "Ecc", "Han", "Thr", "TRO", "Kic", "Ref", "1v1", "Agg", "Ant", "Bra",
                 "Cmp", "Det", "OtB", "Pos", "Tea", "Pac", "Tec", "Sta", "Str", "Cor", "Tck",
                 "Pen", "Fin", "LTh", "Hea", "Fir", "Dri", "Vis", "Cro", "Acc", "Agi", "Bal",
                 "Nat", "Jum", "Wor", "Fla", "Ldr", "Fre", "Dec", "Mar", "Lon", "Pas", "Cnt",
                 "Pun"]

def clean(df):
    """Normalizing the raw export"""