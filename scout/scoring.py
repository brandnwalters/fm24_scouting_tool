def score_players(df, role_weights):
    """Return df with a score column, giving the weighted sum of each players
    attributes for the role"""
    df = df.copy()
    weighted_sum: float = 0
    total_weight: float = 0
    for attr, weight in role_weights.items():
        if attr not in df.columns: 
            continue
        else: 
            weighted_sum += weight * df[attr]
            total_weight += weight
    weighted_sum /= total_weight
  
    df["Score"] = (weighted_sum).round(1)
    return df
