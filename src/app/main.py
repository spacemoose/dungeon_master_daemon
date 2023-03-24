import sys
sys.path.append("../")
import functools

from kivymd.app import MDApp
from kivymd.uix.list import OneLineListItem
from kivymd.uix.scrollview import MDScrollView
from kivy.uix.boxlayout import BoxLayout

from dmbalm import crud, db, initialize_db


class DMDRoot(BoxLayout):
    pass

# I can construct an EncounterItem from an Encounter object,
# and be able to do what I want.
# Can I put the self.on_release into the kv file now?
class EncounterListItem(OneLineListItem):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.on_release = self.press

    def press(self):
        print("pressed {}".format(self.text))

class EncounterList(MDScrollView):
    pass

class CreatureListItem(OneLineListItem):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.on_release = self.press


class dmdApp(MDApp):
    title = "List of Encounters"
    def build(self):
        self.theme_cls.theme_style = "Dark"
        return self.root

    def pressed(self, text):
        print(text)


    def on_start(self):
        encounters = crud.get_encounters(db.SessionLocal())
        for enc in encounters:
            self.root.ids.encounters_list.add_widget(
                EncounterListItem(text = enc.name))


initialize_db.populate_db()
dmdApp().run()
