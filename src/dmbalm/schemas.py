# Schemas for the pydantic models
from typing import List, Optional
from pydantic import BaseModel

class ActionBase(BaseModel):
    name: str
    description: str

    def to_base_dict(self):
        return

class ActionCreate(ActionBase):
    pass

class Action(ActionBase):
    id: int
    creature_id: str

    class Config:
        orm_mode=True


class CreatureBase(BaseModel):
    name: str
    description: Optional[str]
    armor_class: int
    challenge: Optional[float]
    dexterity: int
    hit_dice: str
    languages: Optional[str]
    proficiency_bonus: Optional[int]
    senses: Optional[str]
    speed: Optional[int]
    xp: Optional[int]


class CreatureCreate(CreatureBase):
    actions: List[ActionCreate] = []


class Creature(CreatureBase):
    actions: Optional[List[Action]] = []
    class Config:
        orm_mode=True


class CreatureInstanceBase(BaseModel):
    """name is optional, may want to label individual instances of
    creatures, for example bob the kobold"""
    creature_id: str
    is_pc: bool = False
    name: Optional[str]

# @todo support optional instance name, e.g. bob the kobold.
class CreatureInstanceCreate(CreatureInstanceBase):
    pass

class CreatureInstance(CreatureInstanceBase):
    id: Optional[int]
    hit_points: int
    initiative: int
    encounter_id: Optional[int]

    class Config:
        orm_mode = True


class EncounterBase(BaseModel):
    name: str
    description: Optional[str]

class EncounterCreate(EncounterBase):
    creature_instances: List['CreatureInstanceCreate'] = []

class Encounter(EncounterBase):
    id: Optional[int]
    creature_instances: List['CreatureInstance'] = []
    class Config:
        orm_mode = True
