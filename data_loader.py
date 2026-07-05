import sqlite3
import json

# Connect to database
conn = sqlite3.connect("tennis.db")
cursor = conn.cursor()

# ---------------------------------
# Clear old data before loading
# ---------------------------------
cursor.execute("DELETE FROM Competitor_Rankings")
cursor.execute("DELETE FROM Competitors")
cursor.execute("DELETE FROM Venues")
cursor.execute("DELETE FROM Complexes")
cursor.execute("DELETE FROM Competitions")
cursor.execute("DELETE FROM Categories")

# ---------------------------------
# Load Categories
# ---------------------------------
with open("data/categories.json", "r") as file:
    categories = json.load(file)

for category in categories:
    cursor.execute("""
        INSERT INTO Categories
        VALUES (?,?)
    """, (
        category["category_id"],
        category["category_name"]
    ))

# ---------------------------------
# Load Competitions
# ---------------------------------
with open("data/competitions.json", "r") as file:
    competitions = json.load(file)

for competition in competitions:
    cursor.execute("""
        INSERT INTO Competitions
        VALUES (?,?,?,?,?,?)
    """, (
        competition["competition_id"],
        competition["competition_name"],
        competition["parent_id"],
        competition["type"],
        competition["gender"],
        competition["category_id"]
    ))

# ---------------------------------
# Load Complexes
# ---------------------------------
with open("data/complexes.json", "r") as file:
    complexes = json.load(file)

for complex_data in complexes:
    cursor.execute("""
        INSERT INTO Complexes
        VALUES (?,?)
    """, (
        complex_data["complex_id"],
        complex_data["complex_name"]
    ))

# ---------------------------------
# Load Venues
# ---------------------------------
with open("data/venues.json", "r") as file:
    venues = json.load(file)

for venue in venues:
    cursor.execute("""
        INSERT INTO Venues
        VALUES (?,?,?,?,?,?,?)
    """, (
        venue["venue_id"],
        venue["venue_name"],
        venue["city_name"],
        venue["country_name"],
        venue["country_code"],
        venue["timezone"],
        venue["complex_id"]
    ))

# ---------------------------------
# Load Competitors
# ---------------------------------
with open("data/competitors.json", "r") as file:
    competitors = json.load(file)

for competitor in competitors:
    cursor.execute("""
        INSERT INTO Competitors
        VALUES (?,?,?,?,?)
    """, (
        competitor["competitor_id"],
        competitor["competitor_name"],
        competitor["country"],
        competitor["country_code"],
        competitor["abbreviation"]
    ))

# ---------------------------------
# Load Rankings
# ---------------------------------
with open("data/rankings.json", "r") as file:
    rankings = json.load(file)

for ranking in rankings:
    cursor.execute("""
        INSERT INTO Competitor_Rankings
        (competitor_id, rank, movement, points, competitions_played)
        VALUES (?,?,?,?,?)
    """, (
        ranking["competitor_id"],
        ranking["rank"],
        ranking["movement"],
        ranking["points"],
        ranking["competitions_played"]
    ))

# Save changes
conn.commit()

# Close database
conn.close()

print("✅ All JSON data loaded successfully!")