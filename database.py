import sqlite3

conn = sqlite3.connect("tennis.db")
cursor = conn.cursor()

# Categories Table
cursor.execute("""
CREATE TABLE IF NOT EXISTS Categories (
    category_id TEXT PRIMARY KEY,
    category_name TEXT NOT NULL
)
""")

# Competitions Table
cursor.execute("""
CREATE TABLE IF NOT EXISTS Competitions (
    competition_id TEXT PRIMARY KEY,
    competition_name TEXT NOT NULL,
    parent_id TEXT,
    type TEXT NOT NULL,
    gender TEXT NOT NULL,
    category_id TEXT,
    FOREIGN KEY (category_id) REFERENCES Categories(category_id)
)
""")

print("Tables created successfully!")

conn.commit()
conn.close()
import sqlite3

# Connect to SQLite Database
conn = sqlite3.connect("tennis.db")
cursor = conn.cursor()

# ==========================
# Categories Table
# ==========================
cursor.execute("""
CREATE TABLE IF NOT EXISTS Categories (
    category_id TEXT PRIMARY KEY,
    category_name TEXT NOT NULL
)
""")

# ==========================
# Competitions Table
# ==========================
cursor.execute("""
CREATE TABLE IF NOT EXISTS Competitions (
    competition_id TEXT PRIMARY KEY,
    competition_name TEXT NOT NULL,
    parent_id TEXT,
    type TEXT,
    gender TEXT,
    category_id TEXT,
    FOREIGN KEY (category_id) REFERENCES Categories(category_id)
)
""")

# ==========================
# Complexes Table
# ==========================
cursor.execute("""
CREATE TABLE IF NOT EXISTS Complexes (
    complex_id TEXT PRIMARY KEY,
    complex_name TEXT NOT NULL
)
""")

# ==========================
# Venues Table
# ==========================
cursor.execute("""
CREATE TABLE IF NOT EXISTS Venues (
    venue_id TEXT PRIMARY KEY,
    venue_name TEXT NOT NULL,
    city_name TEXT,
    country_name TEXT,
    country_code TEXT,
    timezone TEXT,
    complex_id TEXT,
    FOREIGN KEY (complex_id) REFERENCES Complexes(complex_id)
)
""")

# ==========================
# Competitors Table
# ==========================
cursor.execute("""
CREATE TABLE IF NOT EXISTS Competitors (
    competitor_id TEXT PRIMARY KEY,
    competitor_name TEXT NOT NULL,
    country TEXT,
    country_code TEXT,
    abbreviation TEXT
)
""")

# ==========================
# Competitor Rankings Table
# ==========================
cursor.execute("""
CREATE TABLE IF NOT EXISTS Competitor_Rankings (
    ranking_id INTEGER PRIMARY KEY AUTOINCREMENT,
    competitor_id TEXT,
    rank INTEGER,
    movement INTEGER,
    points INTEGER,
    competitions_played INTEGER,
    FOREIGN KEY (competitor_id) REFERENCES Competitors(competitor_id)
)
""")

# Save Changes
conn.commit()

print("All tables created successfully!")

# Close Connection
conn.close()