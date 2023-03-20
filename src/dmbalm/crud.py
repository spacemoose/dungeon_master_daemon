from . import models, schemas
from sqlalchemy.orm import Session
from typing import List


# should I be calling commit here, or from where I create the session?
def add_creature(db: Session, creature: schemas.Creature):
    db_creature = models.Creature(creature)
    db.add(models.Creature(db_creature))
    db.commit()


def add_creatures(db: Session, creatures: List[schemas.Creature]):
    db_creatures = []
    for crit in creatures:
        db_creatures.append(models.Creature(crit))
    db.add_all(db_creatures)
    db.commit()


def add_encounter(db: Session, enc: schemas.EncounterCreate):
    enc_model = models.Encounter(enc)
    db.add(enc_model)
    db.commit()

def add_encounters(db: Session, encounters: List[schemas.EncounterCreate]):
    """ Add a list of encounters to the DB."""
    db_encounters = []
    for enc in encounters:
        db_encounters.append(models.Encounter(enc))
    db.add_all(db_encounters)
    db.commit()


def get_creatures(db: Session) -> List[schemas.Creature]:
    critters =  db.query(models.Creature).all()
    return [schemas.Creature.from_orm(crit) for crit in critters]

def get_creature(db: Session, creature_name: str) -> schemas.Creature:
    return db.query(models.Creature).filter_by(name=creature_name).first()

def get_instances(db: Session) -> List[schemas.CreatureInstance]:
    """Get all creature instances"""
    critters = db.query(models.CreatureInstance).all()
    return [schemas.CreatureInstance.from_orm(crit) for crit in critters]

def get_encounter(db: Session, encounter_name: str) -> schemas.Encounter:
    """Get an encounter with the given name"""
    return db.query(models.Encounter).filter_by(name=encounter_name).first()

def get_encounters(db: Session) -> List[schemas.Encounter]:
    """Get all encounters"""
    encounters = db.query(models.Encounter)
    return [schemas.Encounter.from_orm(enc) for enc in encounters]
