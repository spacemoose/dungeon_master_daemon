import sys
sys.path.append("../")

from kivy.uix.boxlayout import BoxLayout
from kivymd.app import MDApp
from kivymd.uix.label.label import Label
from kivymd.uix.list import TwoLineListItem, OneLineListItem
from kivymd.uix.list.list import MDList
from kivymd.uix.scrollview import MDScrollView


from dmbalm import crud, db, initialize_db, schemas


class DMDRoot(BoxLayout):
    """A screen manager.   Has methods to populate the various views we are
    interested in"""
    def show_encounter(self, enc: schemas.Encounter):
        """Show the contents of a single encounter.  Opens the EncounterView"""
        self.clear_widgets()
        self.add_widget(EncounterView(enc))

    def show_encounters(self):
        """Show all known encounters.  Opens the EncountersList view."""
        self.clear_widgets()
        ev = EncounterOverview()
        self.add_widget(ev)
        encounters = crud.get_encounters(db.SessionLocal())
        for enc in encounters:
            ev.ids.encounters_list.add_widget(
                EncounterItem(enc))


class EncounterItem(TwoLineListItem):
    """A OneLineListItem for listing encounters in the EncounterListView"""
    def __init__(self, encounter: schemas.Encounter, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.text = encounter.name
        self.secondary_text = encounter.description
        self.encounter = encounter

class EncounterView(BoxLayout):
    """A container for viewing the details of a single encounter."""
    def __init__(self, encounter: schemas.Encounter, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for crit in encounter.creature_instances:
            detes = f'Initiative {crit.initiative}  HP: {crit.hit_points}  name: {crit.name}'
            self.ids. encounter_creatures.add_widget(TwoLineListItem(text = crit.creature_id,
                                            secondary_text = detes))

class EncounterList(BoxLayout):
    pass

class EncounterOverview(BoxLayout):
    pass


# root of this object is DMDRoot.
class dmdApp(MDApp):
    title = "List of Encounters"
    def build(self):
        self.theme_cls.theme_style = "Dark"
        return self.root

    def open_encounter(self, enc: schemas.Encounter):
        self.root.show_encounter(enc)

    def show_encounters(self):
        self.root.show_encounters()

    def on_start(self):
        self.show_encounters()



initialize_db.populate_db()
dmdApp().run()
