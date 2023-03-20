from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import sessionmaker

db_url = "sqlite+pysqlite:///:memory:"
#engine = create_engine(db_url, echo=True, future=True)
engine = create_engine(db_url, future=True)
SessionLocal = sessionmaker(bind=engine)
Base = declarative_base()
