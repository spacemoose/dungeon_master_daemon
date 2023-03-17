import sys
sys.path.insert(0,"../src/")


from dmbalm.models import Base
from dmbalm.models import Creature
from dmbalm.models import Action

from dmbalm.models import Base
from dmbalm.models import Creature, CreatureInstance, Encounter
from dmbalm import crud
from dmbalm.connection import engine
from dmbalm.connection import Session

import dice

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

add_kobold()

enc_name = "four kobolds"
enc_description = "random encounter in Dragon Hatchery"
enc = Encounter(name = enc_name, description =enc_description)
kobs = [CreatureInstance("Kobold") for _ in range(4)]
enc.creature_instances = kobs
# with Session(engine) as session, session.begin():
#     session.add(enc)
#     # is this redundant?
#     session.add_all(kobs)
#     session.commit()

# with Session(engine) as session, session.begin():
#     encounter = crud.get_encounter(enc_name)
