import streamlit as st

from scout.loader import load_export, clean
from scout.roles import ROLES
from scout.shortlist import shortlist, explain

st.title("FM Scouting")

uploaded_file = st.file_uploader("Upload FM export", type=["csv", "html"])

if uploaded_file is not None:
    df = clean(load_export(uploaded_file))
    st.write(f"Loaded {len(df)} players")
    st.dataframe(df.head())

    role_name = st.selectbox("Role", ROLES.keys())
    max_age = st.slider("Max age", min_value=15, max_value=40, value=30)
    top_n = st.number_input("Top N", min_value=1, max_value=100, value=20)

    result = shortlist(df, role_name, top_n=top_n, max_age=max_age)
    st.dataframe(result)

    player_name = st.selectbox("Player", result["Name"])
    player_row = result[result["Name"] == player_name].iloc[0]
    st.dataframe(explain(player_row, ROLES[role_name]))
