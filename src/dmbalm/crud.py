
from dmbalm.encounter_model import Creature, CreatureInstance, Encounter
from dmbalm.db import SessionLocal

def get_creature(creature_name):
    with SessionLocal() as session:
        res = session.query(Creature).filter_by(name=creature_name)
        return res.first()

def get_instances():
    """Get all creature instances"""
    with SessionLocal() as session:
        return session.query(CreatureInstance)

def get_encounter(encounter_name):
    """Get an encounter with the given name"""
    with SessionLocal() as session:
        return session.query(Encounter).filter_by(name=encounter_name).first()
