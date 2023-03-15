from sqlalchemy import (
    Boolean,
    Column,
    ForeignKey,
    Integer,
    String,
    Numeric,
)
from sqlalchemy.orm import relationship, declarative_base

Base = declarative_base();


# Player Character's can be represented by a creature with everything Null
# except for the creature name, which let's us know who's initiative roll we
# need to enter.  NPCs participating in an encounter should be entered as fully
# creatures, enabling the DMD to automatically roll for initiative and track HP.
#
# The creature name is usually the type of the creature, e.g. "Kobold", or
# "Veteran", but might be a unique NPC, e.g. CyanWrath.
class Creature(Base):
    __tablename__ = "creature"
    name = Column(String, primary_key=True)
    dexterity = Column(Numeric)
    hit_dice = Column(String) # Instructions for calculating hit points
    armor_class = Column(Numeric)
    xp = Column(Numeric) #xp provided by defeating the creature.
    challenge = Column(Numeric)
    senses = Column(String)
    passive_perception  = Column(String)
    languages = Column(String)
    actions = Column(String)
    speed = Column(Numeric) # ft/turn
    reactions = Column(String)
    proficiency_bonus=Column(Numeric)

# Stores instances of the creatures used in various encounters.
# One creature instance belongs to one encounter (currently).
#
# The instance.name is optional, and let's you give names and personalities to
# instances of a creature type, e.g. a Kobold named Fred, or a Veteran name
# Johnny Toughguy.
#
# If a unique NPC, e.g. Cyanwrath, occurs in two encounters, he'll currently have
# two instances, and the instance name is totally redundant.
class CreatureInstance(Base):
    __tablename__ = "creature_instance"
    id = Column(Integer, primary_key=True)
    hit_points = Column(Integer)
    is_pc = Column(Boolean) # is it a player character?
    initiative = Column(Integer)

    creature_id = Column(Integer, ForeignKey("creature.name"))
    encounter_id = Column(Integer, ForeignKey("encounter.id"))

    # not sure I need/want this:
    encounter = relationship("Encounter", back_populates="encounter")


# Stores encounters, which are essentially lists of creatures and PC's.  There are
class Encounter(Base):
    __tablename__ = "encounter"
    id = Column(Integer, primary_key=True)
    name = Column(String(30))
    Description = Column(String)

    creature_instances = relationship("CreatureInstance", back_populates="encounters")

# For now actions are just labels and descriptions.
# stored in a table to allow n actions per creature.
class Action(Base):
    __tablename__ = "action"
    id = Column(Integer, primary_key=true)
    name = Column(String(30))
    description = Column(String(50))
