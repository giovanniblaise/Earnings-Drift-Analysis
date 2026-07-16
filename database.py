import os
from dotenv import load_dotenv
from sqlalchemy import create_engine

load_dotenv()

database_url = os.getenv("ENGINE")

if not database_url:
    raise RuntimeError("ENGINE not found!")

engine = create_engine(database_url)
