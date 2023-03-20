"""Test the parsing tool for extracting monster data out of a
D&D Beyond monster-description cut-paste

This could probably use a few more tests.
"""

from dmbalm import monster_texts
from dmbalm.text_parser import parse_creature
from dmbalm import schemas

def test_kobold():
    """Tests that the text parser returns the right values for Kobold.
    Because the string comparison's are brittle tests, this is the only one where
    I test the """
    kob_test = parse_creature(monster_texts.get_kobold_text())
    kob_ref = schemas.CreatureCreate(
        name="Kobold",
        description = "Small Humanoid (Kobold), Lawful Evil",
        dexterity=15,
        hit_dice="2d6 - 2",
        armor_class=12,
        xp=25,
        challenge=1 / 8,
        senses="Darkvision 60 ft., Passive Perception 8",
        languages="Common, Draconic",
        proficiency_bonus=2,
        speed=30,
        actions=[
            schemas.ActionCreate(
                name="Dagger", description="Melee Weapon Attack: +4 to hit, reach 5 ft., one target. Hit: 4 (1d4 + 2) piercing damage."
            ),
            schemas.ActionCreate(
                name="Sling",
                description="Ranged Weapon Attack: +4 to hit, range 30/120 ft., one target. Hit: 4 (1d4 + 2) bludgeoning damage."
            ),
        ],
    )
    assert (kob_test == kob_ref)
