import os
from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models.task import Base

# Load environment variables from .env
load_dotenv()

# Retrieve database connection details from environment variables
DB_HOST = os.environ.get("MYSQL_HOST")
DB_PORT = int(os.environ.get("MYSQL_PORT"))
DB_USER = os.environ.get("MYSQL_USER")
DB_PASSWORD = os.environ.get("MYSQL_PASSWORD")
DB_NAME = os.environ.get("MYSQL_DB")

# Create a database connection string
DATABASE_URL = f"mysql+mysqlconnector://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"

# Create a SQLAlchemy engine
engine = create_engine(DATABASE_URL, echo=True)  # Set echo=True for debugging
Base.metadata.create_all(engine)

# Create a Session class to manage database sessions
Session = sessionmaker(bind=engine)