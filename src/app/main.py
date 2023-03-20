import sys
sys.path.append("../")
import functools

from kivy.lang import Builder
from kivy.uix.label import Label
from kivy.uix.modalview import ModalView
from kivymd.app import MDApp
from kivymd.uix.list import OneLineListItem

from dmbalm import crud, db, initialize_db


EncounterView = ModalView()
EncounterView.add_widget(Label(text="Encounter View"))

# OK, I guess I can construct an EncounterItem from an Encounter object,
# and be able to do what I want.
class EncounterListItem(OneLineListItem):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.on_release = self.presser

    def presser(self):
        EncounterView.open()

class EncounterList(MDApp):
    title = "List of Encounters"
    def build(self):
        print (self.root)
        self.theme_cls.theme_style = "Dark"

    def presser(self, text):
        print(text)


    def on_start(self):
        encounters = crud.get_encounters(db.SessionLocal())
        for enc in encounters:
            self.root.ids.container.add_widget(
                EncounterListItem(text =enc.name))


initialize_db.populate_db()
EncounterList().run()
