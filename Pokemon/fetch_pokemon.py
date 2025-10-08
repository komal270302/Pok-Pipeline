import requests

# Fetches Pokemon data from the PokeAPI.
def fetch_pokemon_data(limit=10):
    base_url = "https://pokeapi.co/api/v2/pokemon/"
    pokemon_data = []

    # Step 1: Get a list of Pokémon 
    response = requests.get(f"{base_url}?limit={limit}")

    # Check if the request was successful
    if response.status_code != 200:
        print("Failed to fetch Pokémon list!")
        return []

    # Convert the JSON response to a Python dictionary
    data = response.json()

    # Step 2: Loop through each Pokemon and fetch detailed info
    for pokemon in data["results"]:
        details = requests.get(pokemon["url"]).json()

        # Extract selected attributes for each Pokemon
        pokemon_info = {
            "id": details["id"],
            "name": details["name"],
            "height": details["height"],
            "weight": details["weight"],
            "base_experience": details["base_experience"],
            "types": [t["type"]["name"] for t in details["types"]],
            "abilities": [a["ability"]["name"] for a in details["abilities"]],
            "stats": {s["stat"]["name"]: s["base_stat"] for s in details["stats"]}
        }

        # Add the structured Pokemon info to the list
        pokemon_data.append(pokemon_info)

    # Return the complete Pokémon data list
    return pokemon_data

# Run the script directly (not when imported as a module)
if __name__ == "__main__":
    
    # Fetch data for the first 10 Pokémon
    data = fetch_pokemon_data(limit=10)
    print(f"✅ Successfully fetched {len(data)} Pokémon!")
    print(data[0]) 
