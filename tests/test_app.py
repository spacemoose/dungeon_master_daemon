from sqlalchemy import create_engine

# This is so ugly.  Is there a better way?
from  dmbalm.app import Base


engine = create_engine("sqlite+pysqlite:///memory:", echo=True, future=True)


def test_first():
    Base.metdata.create_all(engine)
