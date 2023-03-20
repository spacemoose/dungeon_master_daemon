import sys
sys.path.append("../")
from kivy.lang import Builder
from kivymd.app import MDApp
from kivymd.uix.list import OneLineListItem
from dmbalm import initialize_db, crud, db

KV = '''
MDScrollView:

    MDList:
        id: container
'''


class EncounterList(MDApp):
    def build(self):
        self.theme_cls.theme_style = "Dark"
        return Builder.load_string(KV)

    def on_start(self):
        encounters = crud.get_encounters(db.SessionLocal())
        for enc in encounters:
            self.root.ids.container.add_widget(
                OneLineListItem(text=enc.name)
            )

initialize_db.populate_db()
EncounterList().run()
