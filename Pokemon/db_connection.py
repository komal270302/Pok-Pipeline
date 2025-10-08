import os
from dotenv import load_dotenv
from sqlalchemy import create_engine, text

# Load environment variables from the .env file
load_dotenv()

# Fetch database server and name from environment variables
server = os.getenv("DB_SERVER")
database = os.getenv("DB_NAME")
trusted = os.getenv("DB_TRUSTED", "NO").upper()  
username = os.getenv("DB_USER", "")
password = os.getenv("DB_PASSWORD", "")

# Build connection string
if trusted == "YES":
    # Windows Authentication
    connection_string = (
        f"mssql+pyodbc://@{server}/{database}?driver=ODBC+Driver+17+for+SQL+Server&trusted_connection=yes"
    )
else:
    # SQL Authentication
    connection_string = (
        f"mssql+pyodbc://{username}:{password}@{server}/{database}?driver=ODBC+Driver+17+for+SQL+Server"
    )

# Create an SQLAlchemy engine using the connection string
engine = create_engine(connection_string)

# Test the database connection
try:
    with engine.connect() as conn:
        result = conn.execute(text("SELECT 1"))
        print("✅ Connection successful!")
except Exception as e:
    print("❌ Connection failed:", e)
