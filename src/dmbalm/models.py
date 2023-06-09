import dice
from dmbalm import modifiers
from dmbalm import schemas
from dmbalm.db import Base, SessionLocal

from sqlalchemy import (
    Boolean,
    Column,
    ForeignKey,
    Integer,
    String,
    Numeric,
 )

from sqlalchemy.orm import relationship

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
    description = Column(String)
    armor_class = Column(Numeric)
    challenge = Column(Numeric)
    dexterity = Column(Numeric)
    hit_dice = Column(String)  # Instructions for calculating hit points
    languages = Column(String)
    proficiency_bonus = Column(Numeric)
    senses = Column(String)
    speed = Column(Numeric)  # ft/turn
    xp = Column(Numeric)  # xp provided by defeating the creature.


    actions = relationship("Action", back_populates="creature")

    # Not sure if this is sane, but I wanted to be able to construct a
    # models.Creature from a schemas.CreatureCreate.
    def __init__(self, creature: schemas.CreatureCreate):
        self.name = creature.name
        self.description = creature.description
        self.armor_class = creature.armor_class
        self.challenge = creature.challenge
        self.dexterity = creature.dexterity
        self.hit_dice = creature.hit_dice
        self.languages = creature.languages
        self.proficiency_bones = creature.proficiency_bonus
        self.senses = creature.senses
        self.speed = creature.speed
        self.xp = creature.xp

        self.actions = []
        for act in creature.actions:
            self.actions.append(Action(act))


    def __repr__(self):
        return '<Creature(name={}, dexterity={}, hit_dice={}, armor_class=={}, actions={})>'.format(self.name, self.dexterity, self.hit_dice, self.armor_class, self.actions)

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
    creature_id = Column(String, ForeignKey("creature.name"))
    hit_points = Column(Integer)
    is_pc = Column(Boolean)  # is it a player character?
    initiative = Column(Integer)
    encounter_id = Column(Integer, ForeignKey("encounter.id"))
    name = Column(String, nullable=True)

    # not sure I need/want this:
    encounter = relationship("Encounter", back_populates="creature_instances")

    def __init__(self, cic: schemas.CreatureInstanceCreate):
        """Construct an instance of creature of type creature."""
        self.creature_id  = cic.creature_id
        with SessionLocal() as session:
            res = session.query(Creature).filter_by(name=self.creature_id)
            crit = res.first()
        assert(crit != None)
        self.hit_points = int(dice.roll(crit.hit_dice))
        self.is_pc = False
        self.initiative = int(dice.roll('1d20t') + modifiers.lookup(crit.dexterity))
        self.name = cic.name


    def __repr__(self):
        return "<CreatureInstance(creature_id={}, hit_points={}, is_pc={}, initiative={}, encounter_id={}>".format(self.creature_id, self.hit_points, self.is_pc, self.initiative, self.encounter_id)


# Stores encounters, which are essentially lists of creatures and PC's.  There are
class Encounter(Base):
    __tablename__ = "encounter"
    id = Column(Integer, primary_key=True)
    name = Column(String(30))
    description = Column(String)

    creature_instances = relationship("CreatureInstance", back_populates="encounter")

    def __init__(self, encounter: schemas.EncounterCreate):
        """Construct an instance of Encounter from the corresponding schema create"""
        self.name = encounter.name
        self.description = encounter.description
        self.creature_instances = []
        for ci in encounter.creature_instances:
            self.creature_instances.append(CreatureInstance(ci))


    def __repr__(self):
        return "<Encounter(name={},description={},creature_instances={}>".format(self.name, self.description, self.creature_instances)


# For now actions are just labels and descriptions.
# stored in a table to allow n actions per creature.
class Action(Base):
    __tablename__ = "action"
    id = Column(Integer, primary_key=True)
    name = Column(String(30))
    description = Column(String(50))
    creature_id = Column(String, ForeignKey("creature.name"))

    creature = relationship("Creature", back_populates="actions")

    def __init__(self, action: schemas.ActionCreate):
        self.name = action.name
        self.description = action.description

    def __repr__(self):
        return "<Action(name='%s', description='%s', creature_id='%s')>" % (
            self.name, self.description, self.creature_id)
