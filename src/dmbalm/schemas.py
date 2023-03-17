# Schemas for the pydantic models

from typing import List, Optional
from pydantic import BaseModel

class ActionBase(BaseModel):
    name: str
    description: str

class ActionCreate(ActionBase):
    pass

class Action(ActionBase):
    id: int
    creature_id: int

    class Config:
        orm_mode=True


class CreatureBase(BaseModel):
    name: str
    dexterity: int
    hit_dice: str
    armor_class: str
    xp: int
    challenge: float
    languages: str
    speed: int
    senses: str
    proficiency_bonus: int

class CreatureCreate(CreatureBase):
    pass

class Creature(CreatureBase):
    actions: List[Action] = []
    class Config:
        orm_mode=True


class CreatureInstance(BaseModel):
    id: Optional[int]
    creature_id: str
    hit_points: int
    is_pc: bool
    initiative: int
    encounter_id: Optional[int]

    class Config:
        orm_mode = True


class Encounter(BaseModel):
    id: Optional[int]
    name: str
    description: Optional[str]
    creature_instances: Optional[List['CreatureInstance']] = []

    class Config:
        orm_mode = True
