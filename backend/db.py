# backend/db.py

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.sql import text

DATABASE_URL = "postgresql://postgres:postgres@localhost:5432/sme_financial_health"

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(bind=engine)
