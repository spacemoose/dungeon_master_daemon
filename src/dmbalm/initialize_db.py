""" methods to populate some creatures & encounters"""

from dmbalm import monster_texts
from dmbalm.db import Base
from dmbalm import crud
from dmbalm.db import SessionLocal
from dmbalm.db import engine
from dmbalm import monster_texts
from dmbalm import text_parser
from dmbalm import schemas


def add_random_encounters():
    """Adds the random encounters from Chapter 3 of Tyranny of Dragons.
    This method assumes that the DB has already been populated with the
    necessary creatures."""

    rand1 = schemas.EncounterCreate(name="4 kobolds", description = "1/6 random encounters in Dragon Hatchery")
    for _ in range(4):
        rand1.creature_instances.append(schemas.CreatureInstanceCreate(creature_id ="Kobold"))
    crud.add_encounter(SessionLocal(), rand1)

    # I use add single and add multiple here to ensure both work.
    addme = []
    rand2 = schemas.EncounterCreate(name="6 kobold and 2 winged kobolds", description = "2/6 random encounters in Dragon Hatchery")
    for _ in range(6):
        rand2.creature_instances.append(schemas.CreatureInstanceCreate(creature_id = "Kobold"))
    for _ in range(2):
        rand2.creature_instances.append(schemas.CreatureInstanceCreate(creature_id = "Winged Kobold"))
    addme.append(rand2)

    rand3 = schemas.EncounterCreate(name = "3 winged kobolds", description = "3/6 random encounters in Dragon Hatchery")
    for _ in range(3):
        rand3.creature_instances.append(schemas.CreatureInstanceCreate(creature_id = "Winged Kobold"))
    addme.append(rand3)

    rand4 = schemas.EncounterCreate(name = "5 winged kobolds", description = "4/6 random encounters in Dragon Hatchery")
    for _ in range(5):
        rand4.creature_instances.append(schemas.CreatureInstanceCreate(creature_id = "Winged Kobold"))
    addme.append(rand4)

    rand5 = schemas.EncounterCreate(name = "2 winged kobolds and 1 guard drake", description = "5/6 random encounters in Dragon Hatchery")
    for _ in range(2):
        rand4.creature_instances.append(schemas.CreatureInstanceCreate(creature_id = "Winged Kobold"))
    rand5.creature_instances.append(schemas.CreatureInstanceCreate(creature_id = "Guard Drake"))
    addme.append(rand5)

    rand6 = schemas.EncounterCreate(name = "2 ambush drakes", description = "6/6 random encounters in Dragon Hatchery")
    for _ in range (2):
        rand6.creature_instances.append(schemas.CreatureInstanceCreate(creature_id = "Guard Drake"))
    addme.append(rand6)

    crud.add_encounters(SessionLocal(), addme)



def add_creatures():

    kobold = text_parser.parse_creature(monster_texts.get_kobold_text())
    ambush_drake = text_parser.parse_creature(monster_texts.get_ambush_drake_text())
    guard_drake = text_parser.parse_creature(monster_texts.get_guard_drake_text())
    winged_kobold = text_parser.parse_creature(monster_texts.get_winged_kobold_text())
    crud.add_creatures(SessionLocal(), [ kobold, ambush_drake, guard_drake, winged_kobold])


def populate_db():
    Base.metadata.create_all(bind=engine)
    add_creatures()
    add_random_encounters()


def print_creatures():
    critters = crud.get_creatures(SessionLocal());
    print(len(critters))
