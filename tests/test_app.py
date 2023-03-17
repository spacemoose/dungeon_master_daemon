import sys
sys.path.insert(0,"../src/")

from sqlalchemy import create_engine
from sqlalchemy.orm import Session

from dmbalm.encounter_model import Base
from dmbalm.encounter_model import Creature
from dmbalm.encounter_model import Action

from dmbalm.encounter_model import Base
from dmbalm.encounter_model import Creature, CreatureInstance, Encounter


engine = create_engine("sqlite+pysqlite:///:memory:", echo=True, future=True)


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


def test_create_encounter():
    four_kobolds = Encounter(name = "four kobolds", description = "random encounter in Dragon Hatchery")
    creature_instance =

# Okay, up next let's make some crud methods for creating and reading
# stuff from the db.
