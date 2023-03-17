
from dmbalm.encounter_model import Creature, CreatureInstance

from dmbalm.connection import Session

def get_creature(creature_name):
    with Session() as session:
        res = session.query(Creature).filter_by(name=creature_name)
        return res.first()

def get_instances():
    """Get all creature instances"""
    with Session() as session:
        return session.query(CreatureInstance)
