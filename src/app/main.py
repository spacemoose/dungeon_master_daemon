import sys
sys.path.append("../")
from kivy.lang import Builder
from kivymd.app import MDApp
from kivymd.uix.list import OneLineListItem
from dmbalm import initialize_db, crud, db


class EncounterList(MDApp):
    title = "List of Encounters"
    def build(self):
        print (self.root)
        self.theme_cls.theme_style = "Dark"


    def on_start(self):
        encounters = crud.get_encounters(db.SessionLocal())
        for enc in encounters:
            self.root.ids.container.add_widget(
                OneLineListItem(text=enc.name)
            )

initialize_db.populate_db()
EncounterList().run()
