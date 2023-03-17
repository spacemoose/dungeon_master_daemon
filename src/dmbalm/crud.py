
from dmbalm.encounter_model import Creature

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

engine = create_engine("sqlite+pysqlite:///:memory:", echo=True, future=True)
Session = sessionmaker(engine)

def get_creature(creature_name):
    with Session() as session:
        res = session.query(Creature).filter_by(name=creature_name)
        return res.first()
