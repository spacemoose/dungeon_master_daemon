"""This tests the initialization of the database with the default
creatures & encounters"""

import sys

sys.path.insert(0, "../src/")
from dmbalm.initialize_db import populate_db, print_creatures
from dmbalm import crud
from dmbalm.db import SessionLocal


def get_attr_list(thing):
    """Returns a list of non-internal attributes for a class.  Useful for
    comparing base and derived class contents."""
    return [attr for attr in vars(thing) if not attr.startswith("__")]


# @todo pass the session to populate_db.
def test_populate():
    """Populate the DB into our in-memory session."""
    populate_db()


def test_creatures_exist():
    """Tests that the default creatures have been added to the DB."""
    creature_list = crud.get_creatures(SessionLocal())
    assert len(creature_list) == 4
    should_have = {"Kobold", "Winged Kobold", "Guard Drake", "Ambush Drake"}
    have = set([crit.name for crit in creature_list])

    assert have == should_have


def test_encounters_exist():
    should_have = {
        "2 ambush drakes",
        "2 winged kobolds and 1 guard drake",
        "3 winged kobolds",
        "4 kobolds",
        "5 winged kobolds",
        "6 kobold and 2 winged kobolds",
    }
    encounters = crud.get_encounters(SessionLocal())
    have = set([enc.name for enc in encounters])
    assert len(have) == len(should_have)
    assert have == should_have
