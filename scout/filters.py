from loader import load_export, clean

def filter_players(df, max_age=None, position=None, max_value= None, min_attrs=None):
    """Returning the subset of the df matching all criteria"""
    if max_age is not None:
        df = df[df["Age"] <= max_age]
    if position is not None:
        df = df[df["Position"].str.contains(position)]
    if max_value is not None:
        df = df[df["Transfer Value"] <= max_value]
    if min_attrs is not None:
        for attr, threshold in min_attrs.items():
                if attr not in df.columns:
                     raise ValueError("Attribute not in DataFrame")
                else:
                    df = df[df[attr] >= threshold]
    return df

