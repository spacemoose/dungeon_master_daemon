import sys
sys.path.insert(0, "../")
import re
import dmbalm.schemas as schemas
from fractions import Fraction
from typing import List, Dict, Any

def parse_action_strings(action_strings: List[str]) -> List[Dict[str, str]]:
    retval = []
    for action in action_strings:
        parts = action.split(".", maxsplit=1)
        retval.append({"name": parts[0].strip(), "description": parts[1].strip()})
    return retval



# @todo modify this to match everything it can and handle missing matches gracefully.
def parse_creature(critter_text: str) -> schemas.CreatureCreate:
    name_regex = r'^([^\n]+)\n'
    description_regex = r'^[^\n]+\n([^\n]+)\n'
    armor_class_regex = r'Armor Class (\d+)'
    challenge_regex = r"Challenge (\d+(?:/\d+)?) \((\d+) XP\)"
    dexterity_regex = r'DEX\n(\d+)'
    languages_regex = re.compile(r"Languages(.*?)Challenge", re.DOTALL)
    proficiency_regex = re.compile(r"Proficiency Bonus (\+\d+)", re.DOTALL)
    speed_regex = r"Speed (\d+) ft\."
    senses_regex = re.compile(r"Senses(.*?)Languages", re.DOTALL)

    action_regex = re.compile(r"Actions\n\n(.*)", re.DOTALL)

    languages_match = re.search(languages_regex, critter_text)
    challenge_match = re.search(challenge_regex, critter_text)
    proficiency_match = re.search(proficiency_regex, critter_text)
    speed_match = re.search(speed_regex, critter_text)
    senses_match = senses_regex.search(critter_text)

    action_string = action_regex.findall(critter_text)[0].strip()
    actions_dict = parse_action_strings(action_string.split("\n\n"))


    return schemas.CreatureCreate(
        name = re.search(name_regex, critter_text).group(1),
        description = re.search(description_regex, critter_text).group(1),
        armor_class = int(re.search(armor_class_regex, critter_text).group(1)),
        challenge = float(Fraction(challenge_match.group(1))),
        dexterity = int(re.search(dexterity_regex, critter_text).group(1)),
        hit_dice = re.search(r'Hit Points \d+ \((.*?)\)', critter_text).group(1),
        languages = languages_match.group(1).strip(),
        proficiency_bonus = proficiency_match.group(1),
        speed = int(speed_match.group(1)),
        senses = senses_match.group(1).strip(),
        xp = challenge_match.group(2),

        actions = actions_dict
    )
