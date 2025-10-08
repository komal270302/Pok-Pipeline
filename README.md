# PokéPipeline: A Pokémon Data ETL Pipeline
## Project Overview
PokéPipeline is an end-to-end ETL (Extract, Transform, Load) pipeline that ingests data from the public PokeAPI, transforms JSON responses into a relational structure, and loads it into a SQL Server database.
This project demonstrates practical data engineering skills in API integration, ETL design, SQL schema modeling, and containerized deployment with Docker.

The project demonstrates :
1. Extraction: Collects detailed Pokémon data (types, abilities, stats, etc.) from the PokéAPI.
2. Transformation: Cleans and maps JSON responses into a normalized relational schema.
3. Loading: Inserts structured data into SQL Server tables using SQLAlchemy.
4. Containerized: Runs seamlessly with Docker Compose (SQL Server + ETL service).
5. Reusable: Modular design with separate scripts for fetching, transforming, and loading.

This solution is portable and reproducible .It can be run either locally or in a fully containerized environment.

## Tech Stack
- Python 3.11 – ETL scripting
- SQLAlchemy – ORM & database interaction
- SQL Server – Relational database
- Docker & Docker Compose – Container orchestration
- PokeAPI – Data source (public REST API)

## Setup & Running Instructions
1. Clone Repository : git clone https://github.com/komal270302/Pok-Pipeline.git, cd Pok-Pipeline

2. Environment Variables :
   - Review and update .env with your SQL Server details. The default uses SQL authentication: DB_SERVER=sqlserver DB_NAME=pokemon_db DB_USER=Komal DB_PASSWORD=Komal@123 DB_TRUSTED=NO.
   - For Windows Authentication (commented out), set DB_TRUSTED=YES and remove DB_USER/DB_PASSWORD.
   - Note: The SQL Server container uses SA_PASSWORD: "Komal@123" (update in docker-compose.yml if changing .env).

4. Run with Docker : 
Build and start services (SQL Server + ETL): docker-compose up --build. This builds the This builds the ETL image from Dockerfile, starts the SQL Server, and runs load_pokemon.py automatically.

5. Run Locally (without Docker) Install dependencies: pip install requests pandas sqlalchemy pyodbc python-dotenv. Ensure SQL Server is running locally (e.g., via SQL Server Express). Run: python load_pokemon.py.

## Database Schema
This design avoids duplication and allows efficient querying. The pipeline normalizes Pokémon data into the following relational tables:
- pokemon – core Pokémon attributes (id, name, height, weight, base_experience)
- type – unique list of Pokémon types
- ability – unique list of abilities
- pokemon_type – mapping between Pokémon and their types
- pokemon_ability – mapping between Pokémon and their abilities
- pokemon_stats – key-value stats (e.g., attack, defense, speed)

## Design Choices
1. ETL Structure:
   - fetch_pokemon.py handles API extraction & raw structuring fetch_pokemon
   - load_pokemon.py manages transformation + SQL inserts load_pokemon
   - db_connection.py abstracts database connectivity db_connection

2. Data Transformation:
   - JSON arrays (types, abilities, stats) → normalized mapping tables
   - Caches (type_cache, ability_cache) prevent duplicate inserts
   - Structured stats dictionary → row-based storage for flexibility

3. Database:
   - SQL Server chosen for robustness and real-world relevance
   - Schema normalization ensures scalability for thousands of Pokémon

## Assumptions
- Pokémon IDs from the API are globally unique so they are used as primary keys
- Types and abilities are reusable entities. Hence separate lookup tables are created
- Only a subset of Pokémon attributes is stored (height, weight, base exp, stats, abilities, types) for clarity.
- The pipeline is designed to handle duplicates via caches.

## Future Improvements
- Add logging & monitoring for ETL runs
- Parameterize pipeline to fetch all Pokémon instead of a limited subset
- Add Airflow orchestration for scheduled ETL runs
- Build visual dashboard (Power BI / Tableau) for Pokémon analytics

## Conclusion 
This project showcases:
- Data engineering fundamentals – designing ETL pipelines, handling APIs, database normalization.
- Production-ready practices – Dockerization, environment variables, modular scripts.
- SQL + Python integration – strong foundation for data workflows.

## Contributor 
Komal - komal202220@gmail.com
