from kivy.config import Config
Config.set('graphics', 'resizable', 0)

import kivy

from kivy.app import App

from modules.auth import *
from scratches.auth import *
from scratches.auth_widget import Auth

from kivy.core.window import Window
# from kivy.config import Config


class MyApp(App):
    def build(self):
        self.title = "MyBusiness"
        return Auth()

    # def do_layout(self, *args, **kwargs):
    #     super(MyApp, self).do_layout()
    #     width, height = Window.size
    #     if width > 300:
    #         Window.size = 300, Window.size[1]
    #     if height > 300:
    #         Window.size = 300, Window.size[0]


if __name__ == "__main__":
    MyApp().run()
