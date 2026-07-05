import json
import random

# -----------------------------
# Categories
# -----------------------------
categories = [
    {"category_id": "CAT001", "category_name": "ATP Men"},
    {"category_id": "CAT002", "category_name": "WTA Women"},
    {"category_id": "CAT003", "category_name": "ATP Challenger"},
    {"category_id": "CAT004", "category_name": "ITF Men"},
    {"category_id": "CAT005", "category_name": "ITF Women"},
    {"category_id": "CAT006", "category_name": "Grand Slam"},
    {"category_id": "CAT007", "category_name": "ATP 1000"},
    {"category_id": "CAT008", "category_name": "ATP 500"},
    {"category_id": "CAT009", "category_name": "ATP 250"},
    {"category_id": "CAT010", "category_name": "WTA 1000"}
]

# -----------------------------
# Competitions
# -----------------------------
competition_types = ["Singles", "Doubles"]
genders = ["Men", "Women"]

competitions = []

for i in range(1, 51):
    competitions.append({
        "competition_id": f"COMP{i:03}",
        "competition_name": f"Tennis Championship {i}",
        "parent_id": "",
        "type": random.choice(competition_types),
        "gender": random.choice(genders),
        "category_id": random.choice(categories)["category_id"]
    })

# -----------------------------
# Complexes
# -----------------------------
complexes = []

for i in range(1, 21):
    complexes.append({
        "complex_id": f"COM{i:03}",
        "complex_name": f"Tennis Complex {i}"
    })

# -----------------------------
# Venues
# -----------------------------
countries = [
    ("Australia","AUS"),
    ("USA","USA"),
    ("France","FRA"),
    ("Spain","ESP"),
    ("Italy","ITA"),
    ("United Kingdom","GBR")
]

venues = []

for i in range(1,41):

    country = random.choice(countries)
    complex_data = random.choice(complexes)

    venues.append({
        "venue_id":f"VEN{i:03}",
        "venue_name":f"Stadium {i}",
        "city_name":f"City {i}",
        "country_name":country[0],
        "country_code":country[1],
        "timezone":"UTC",
        "complex_id":complex_data["complex_id"]
    })

# -----------------------------
# Competitors
# -----------------------------
first_names=[
"Novak","Carlos","Jannik","Rafael","Roger","Andy",
"Daniil","Alexander","Casper","Stefanos",
"Emma","Iga","Aryna","Coco","Naomi",
"Elena","Jessica","Ons","Maria","Paula"
]

last_names=[
"Djokovic","Alcaraz","Sinner","Nadal","Federer","Murray",
"Medvedev","Zverev","Ruud","Tsitsipas",
"Raducanu","Swiatek","Sabalenka","Gauff","Osaka",
"Rybakina","Pegula","Jabeur","Sakkari","Badosa"
]

competitors=[]

for i in range(1,101):

    first=random.choice(first_names)
    last=random.choice(last_names)

    country=random.choice(countries)

    competitors.append({

        "competitor_id":f"P{i:03}",
        "competitor_name":first+" "+last,
        "country":country[0],
        "country_code":country[1],
        "abbreviation":first[:3].upper()

    })

# -----------------------------
# Rankings
# -----------------------------
rankings=[]

rank=1

for player in competitors:

    rankings.append({

        "competitor_id":player["competitor_id"],
        "rank":rank,
        "movement":random.randint(-5,5),
        "points":random.randint(800,12000),
        "competitions_played":random.randint(10,35)

    })

    rank+=1

# -----------------------------
# Save JSON Files
# -----------------------------

with open("data/categories.json","w") as f:
    json.dump(categories,f,indent=4)

with open("data/competitions.json","w") as f:
    json.dump(competitions,f,indent=4)

with open("data/complexes.json","w") as f:
    json.dump(complexes,f,indent=4)

with open("data/venues.json","w") as f:
    json.dump(venues,f,indent=4)

with open("data/competitors.json","w") as f:
    json.dump(competitors,f,indent=4)

with open("data/rankings.json","w") as f:
    json.dump(rankings,f,indent=4)

print("✅ Dataset Generated Successfully!")