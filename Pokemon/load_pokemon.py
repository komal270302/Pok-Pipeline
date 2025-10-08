from sqlalchemy import text
from db_connection import engine
from fetch_pokemon import fetch_pokemon_data

# DATA EXTRACTION!
# Step 1: Fetch Pokemon data from API
pokemon_list = fetch_pokemon_data(limit=10)

# DATA TRANSFORMATION & MAPPING!
# Step 2: Initialize caches to prevent duplicate inserts
type_cache = {}
ability_cache = {}

# DATA LOADING!
# Step 3: Helper function to insert Pokemon types
def insert_type(conn, type_name):
    if type_name not in type_cache:
        result = conn.execute(
            text("INSERT INTO type (name) OUTPUT inserted.id VALUES (:name)"),
            {"name": type_name}  
        )
        type_cache[type_name] = result.scalar()
    return type_cache[type_name]

# Step 4: Helper function to insert Pokémon abilities
def insert_ability(conn, ability_name):
    if ability_name not in ability_cache:
        result = conn.execute(
            text("INSERT INTO ability (name) OUTPUT inserted.id VALUES (:name)"),
            {"name": ability_name}  
        )
        ability_cache[ability_name] = result.scalar()
    return ability_cache[ability_name]

# Step 5: Insert Pokemon data into database tables
with engine.begin() as conn:
    for p in pokemon_list:

        # Insert basic Pokemon info
        conn.execute(
            text("""
                INSERT INTO pokemon (id, name, height, weight, base_experience)
                VALUES (:id, :name, :height, :weight, :base_experience)
            """),
            {
                "id": p["id"],
                "name": p["name"],
                "height": p["height"],
                "weight": p["weight"],
                "base_experience": p["base_experience"]
            }
        )

        # Insert Pokemon types and mapping
        for t in p["types"]:
            type_id = insert_type(conn, t)
            conn.execute(
                text("INSERT INTO pokemon_type (pokemon_id, type_id) VALUES (:pokemon_id, :type_id)"),
                {"pokemon_id": p["id"], "type_id": type_id}
            )

        # Insert abilities and mapping
        for a in p["abilities"]:
            ability_id = insert_ability(conn, a)
            conn.execute(
                text("INSERT INTO pokemon_ability (pokemon_id, ability_id) VALUES (:pokemon_id, :ability_id)"),
                {"pokemon_id": p["id"], "ability_id": ability_id}
            )

        # Insert Pokemon stats (e.g., speed, attack, defense)
        for stat_name, stat_value in p["stats"].items():
            conn.execute(
                text("""
                    INSERT INTO pokemon_stats (pokemon_id, stat_name, stat_value)
                    VALUES (:pokemon_id, :stat_name, :stat_value)
                """),
                {"pokemon_id": p["id"], "stat_name": stat_name, "stat_value": stat_value}
            )

# The ETL pipeline has successfully: Extracted data from the PokéAPI, Transformed JSON into relational schema and Loaded normalized data into SQL tables
print("Pokemon data loaded successfully!")


