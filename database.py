
import os
from pymongo import MongoClient
from dotenv import load_dotenv

# Load environment variables from .env
load_dotenv()

# Get MongoDB connection details
MONGODB_URI = os.getenv("MONGODB_URI")
DATABASE_NAME = os.getenv("DATABASE_NAME")

# Connect to MongoDB Atlas
client = MongoClient(
    MONGODB_URI,
    serverSelectionTimeoutMS=10000
)

# Select the database
db = client[DATABASE_NAME]

# Test the connection
def test_connection():
    try:
        client.admin.command("ping")
        print("SUCCESS: Connected to MongoDB Atlas!")
        print(f"Database: {DATABASE_NAME}")
    except Exception as error:
        print("Connection failed:")
        print(error)

if __name__ == "__main__":
    test_connection()
