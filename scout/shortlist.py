from scout.filters import filter_players
from scout.scoring import score_players
from scout.roles import ROLES

def shortlist(df, role_name, top_n=20, **filter_criteria):
    candidate_pool = filter_players(df, **filter_criteria)
    scored_pool = score_players(candidate_pool, ROLES[role_name])
    sorted_pool = scored_pool.sort_values("Score", ascending=False)
    return sorted_pool.head(top_n)


def explain(player_row, role_weights):
    """Show each attribute's contribution to one player's score."""
    contributions = []
    for attr, weight in role_weights.items():
        if attr not in player_row:      
            continue
        value = player_row[attr]        
        contribution = value * weight
        contributions.append((attr, value, weight, contribution))
        
    contributions.sort(key=lambda row: row[3], reverse=True)

    for attr, value, weight, contribution in contributions:
        print(f"{attr:<15} {value:>4} × {weight}  =  {contribution:>5}")