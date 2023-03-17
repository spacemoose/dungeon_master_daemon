# So  I can call the same db session from all over the place.

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

engine = create_engine("sqlite+pysqlite:///:memory:", echo=True, future=True)
Session = sessionmaker(bind=engine)
