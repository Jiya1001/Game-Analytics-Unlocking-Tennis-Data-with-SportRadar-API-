import streamlit as st
import sqlite3
import pandas as pd
import matplotlib.pyplot as plt

# -----------------------------
# Page Configuration
# -----------------------------
st.set_page_config(
    page_title="🎾 Tennis Game Analytics Dashboard",
    page_icon="🎾",
    layout="wide"
)

# -----------------------------
# Database Connection
# -----------------------------
conn = sqlite3.connect("tennis.db")

# -----------------------------
# Sidebar
# -----------------------------
st.sidebar.title("🎾 Navigation")

menu = st.sidebar.radio(
    "Select Page",
    [
        "Dashboard",
        "Competitors",
        "Competitions",
        "Venues",
        "Rankings"
    ]
)

# -----------------------------
# Dashboard
# -----------------------------
if menu == "Dashboard":

    st.title("🎾 Tennis Game Analytics Dashboard")

    competitors = pd.read_sql("SELECT * FROM Competitors", conn)
    competitions = pd.read_sql("SELECT * FROM Competitions", conn)
    venues = pd.read_sql("SELECT * FROM Venues", conn)
    rankings = pd.read_sql("SELECT * FROM Competitor_Rankings", conn)

    col1, col2, col3, col4 = st.columns(4)

    col1.metric("👤 Competitors", len(competitors))
    col2.metric("🏆 Competitions", len(competitions))
    col3.metric("🏟️ Venues", len(venues))
    col4.metric("📈 Rankings", len(rankings))

    st.divider()

    st.subheader("Top 10 Ranked Players")

    query = """
    SELECT
    c.competitor_name,
    c.country,
    r.rank,
    r.points
    FROM Competitors c
    JOIN Competitor_Rankings r
    ON c.competitor_id=r.competitor_id
    ORDER BY r.rank
    LIMIT 10
    """

    df = pd.read_sql(query, conn)

    st.dataframe(df, use_container_width=True)

# -----------------------------
# Competitors
# -----------------------------
elif menu == "Competitors":

    st.title("👤 Competitors")

    df = pd.read_sql("SELECT * FROM Competitors", conn)

    search = st.text_input("Search Competitor")

    if search:

        df = df[df["competitor_name"].str.contains(search, case=False)]

    st.dataframe(df, use_container_width=True)

# -----------------------------
# Competitions
# -----------------------------
elif menu == "Competitions":

    st.title("🏆 Competitions")

    df = pd.read_sql("SELECT * FROM Competitions", conn)

    st.dataframe(df, use_container_width=True)

# -----------------------------
# Venues
# -----------------------------
elif menu == "Venues":

    st.title("🏟️ Venues")

    df = pd.read_sql("SELECT * FROM Venues", conn)

    st.dataframe(df, use_container_width=True)

# -----------------------------
# Rankings
# -----------------------------
elif menu == "Rankings":

    st.title("📈 Rankings")

    query = """
    SELECT
    c.competitor_name,
    c.country,
    r.rank,
    r.points,
    r.competitions_played
    FROM Competitors c
    JOIN Competitor_Rankings r
    ON c.competitor_id=r.competitor_id
    ORDER BY r.rank
    """

    df = pd.read_sql(query, conn)

    st.dataframe(df, use_container_width=True)

    st.subheader("Top 10 Players by Points")

    top = df.head(10)

    fig, ax = plt.subplots(figsize=(10,5))

    ax.bar(top["competitor_name"], top["points"])

    plt.xticks(rotation=45)

    st.pyplot(fig)

conn.close()