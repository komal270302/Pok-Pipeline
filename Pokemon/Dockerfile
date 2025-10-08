# Use official Python 3.11 slim image
FROM python:3.11-slim

# Set working directory
WORKDIR /app

# Copy project files into container
COPY . /app

# Install dependencies
RUN pip install --upgrade pip
RUN pip install requests pandas sqlalchemy pyodbc python-dotenv

# Default command to run ETL script
CMD ["python", "load_pokemon.py"]
