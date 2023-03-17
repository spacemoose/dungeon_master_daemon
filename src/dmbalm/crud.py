from . import models, schemas
from sqlalchemy.orm import Session
from typing import List

def get_creature(db: Session, creature_name: str):
    return db.query(models.Creature).filter_by(name=creature_name).first()

def get_instances(db: Session) -> List[schemas.CreatureInstance]:
    """Get all creature instances"""
    return db.query(models.CreatureInstance)

def get_encounter(db: Session, encounter_name: str) -> schemas.Encounter:
    """Get an encounter with the given name"""
    return db.query(models.Encounter).filter_by(name=encounter_name).first()
