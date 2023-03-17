from sqlalchemy import create_engine
from sqlalchemy.orm import Session

from dmbalm.encounter_model import Base
from dmbalm.encounter_model import Creature
from dmbalm.encounter_model import Action

engine = create_engine("sqlite+pysqlite:///:memory:", echo=True, future=True)


Base.metadata.create_all(engine)


def add_kobold():
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

def do_it():
    with Session(engine) as session, session.begin():
        session.add(bob)
        session.add(dagger)
        session.add(sling)
        session.commit()

def get_creatures():
    with Session(engine) as session, session.begin():
        return session.query(Creature)
        #for instance in session.query(Creature):
        #   print(instance.name, instance.actions)
