# import sys
# sys.path.insert(0,"../src/")

# from dmbalm import crud
# from dmbalm.db import Base, SessionLocal, engine
# from dmbalm.initialize_db import add_creatures
# import dice

# def test_create_tables():
#     Base.metadata.create_all(bind=engine)

# def test_add_creatures():
#     add_creatures()
#     kob = crud.get_creature(SessionLocal(), "Kobold")
#     assert(kob.name == "Kobold")
#     assert(len(kob.actions) == 2)


# def test_get_creature():
#     kob = crud.get_creature(SessionLocal(), creature_name= "Kobold")
#     assert(kob.name == "Kobold")

# def test_instantiate_kobold():
#     crname = "Kobold"
#     cr = crud.get_creature(SessionLocal(), crname)
#     kob = CreatureInstance(crname)
#     assert (kob.creature_id == crname)
#     assert( dice.roll_min(cr.hit_dice) <= kob.hit_points <= dice.roll_max(cr.hit_dice))
#     with SessionLocal() as session, session.begin():
#         session.add(kob)
#         session.commit()

#     instances = crud.get_instances(SessionLocal())
#     assert(len(instances) == 1)


# def test_encounter_4_kobolds():
#     enc_name = "four kobolds"
#     enc_description = "random encounter in Dragon Hatchery"
#     enc = Encounter(name = enc_name, description =enc_description)
#     kobs = [CreatureInstance("Kobold") for _ in range(4)]
#     enc.creature_instances = kobs
#     with SessionLocal() as session, session.begin():
#         # is this redundant?
#         # session.add_all(kobs)
#         # looks like it is.
#         session.add(enc)
#         session.commit()

#         #   with SessionLocal() as session, session.begin():
#         #   encounter = session.query(Encounter).filter_by(name=enc_name).first()

#     encounter = crud.get_encounter(SessionLocal(), enc_name)
#     assert(encounter.name ==enc_name)
#     assert(encounter.description == enc_description)
#     assert(len(encounter.creature_instances) == 4)


# Okay, up next let's make some crud methods for creating and reading
# stuff from the db.
