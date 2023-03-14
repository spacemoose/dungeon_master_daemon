"""
A tool for helping DMs manage encounters.
"""
import toga
import httpx

from toga.style import Pack
from toga.style.pack import COLUMN, ROW

def greeting(name):
    if name:
        return f"Next step, add {name}"
    else:
        return f"Next step, grey-out add until a name is entered"

class DMD(toga.App):
    def startup(self):
        """
        Construct and show the Toga application.

        Usually, you would add your application to a main content box.
        We then create a main window (with a name matching the app), and
        show the main window.
        """

        main_box = toga.Box(style=Pack(direction=COLUMN, padding=5))

        name_label = toga.Label(
            "Creature name: ",
            style=Pack(padding=(0,5))
        )
        self.name_input = toga.TextInput(style=Pack(flex=1))
        creature_box = toga.Box(style=Pack(direction=ROW, padding=5))
        creature_box.add(name_label)
        creature_box.add(self.name_input)

        button = toga.Button(
            "Save",
            on_press=self.add_creature,
            style=Pack(padding=5)
        )

        main_box.add(creature_box)
        main_box.add(button)

        self.main_window = toga.MainWindow(title=self.formal_name)
        self.main_window.content = main_box
        self.main_window.show()

    async def add_creature(self, widget):
        async with httpx.AsyncClient() as client:
            response = await client.get("https://jsonplaceholder.typicode.com/posts/42")

        payload = response.json();
        self.main_window.info_dialog(
            greeting(self.name_input.value),
            payload["body"],
        )



def main():
    return DMD()
