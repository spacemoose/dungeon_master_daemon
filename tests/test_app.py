from sqlalchemy import create_engine

# This is so ugly.  Is there a better way?
from dmbalm.encounter_model import Base
from dmbalm.encounter_model import Creature, CreatureInstance, Encounter

engine = create_engine("sqlite+pysqlite:///memory:", echo=True, future=True)


def test_first():
    Base.metadata.create_all(engine)

def test_add_kobold():
kobold = Creature(
    name = "Kobold"
    dexterity = 15
    hit_dice = "2d6-2"
    armor_class = 12
    xp = 25
    challenge = 1/8
    senses = "Darkvision 60 ft, Passive Perception 8"
    languages = "Common, Draconic"
    proficiency_bonus=2
)
