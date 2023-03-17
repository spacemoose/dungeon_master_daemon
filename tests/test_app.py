import sys
sys.path.insert(0,"../src/")

from sqlalchemy import create_engine, engine_from_config
from sqlalchemy.orm import Session

from dmbalm.encounter_model import Base
from dmbalm.encounter_model import Creature
from dmbalm.encounter_model import Action

from dmbalm.encounter_model import Base
from dmbalm.encounter_model import Creature, CreatureInstance, Encounter
from dmbalm import crud

import dice

engine = crud.engine


def test_create_tables():
    Base.metadata.create_all(engine)


# with actions...
def test_add_kobold():
    k1 = Creature(
        name="Kobold",
        dexterity=15,
        hit_dice="2d6-2",
        armor_class=12,
        xp=25,
        challenge=1 / 8,
        senses="Darkvision 60 ft, Passive Perception 8",
        languages="Common, Draconic",
        proficiency_bonus=2,
    )

    dagger = Action(name="dagger", description="+4 to hit, reach 5ft, (1d4+2) piercing")
    sling = Action(name="sling", description="+4 to hit, range 30/120 ft, (1d4+2) bludgeoning")
    k1.actions.append(dagger)
    k1.actions.append(sling)

    with Session(engine) as session, session.begin():
        session.add(k1)
        session.add(dagger)
        session.add(sling)
        session.commit()

def test_count_creatures():
    with Session(engine) as session, session.begin():
        assert(session.query(Creature).count() == 1)

def test_get_creature():
    kob = crud.get_creature("Kobold")
    assert(kob.name == "Kobold")

def test_instantiate_kobold():
    crname = "Kobold"
    cr = crud.get_creature(crname)
    kob = CreatureInstance(crname)
    assert (kob.creature_id == crname)
    assert( dice.min_roll(cr.hit_dice) <= kob.hit_points <= dice.max_roll(cr.hit_dice))

# def test_create_four_kobolds():
#      enc = Encounter(name = "four kobolds", description = "random encounter in Dragon Hatchery")
#      enc.creature_instances = [CreatureInstance("Kobold") for _ in range(4)]





# Okay, up next let's make some crud methods for creating and reading
# stuff from the db.
