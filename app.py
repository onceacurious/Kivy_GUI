import kivy

from kivy.app import App
from kivy.core.window import Window

from modules.auth import *


Window.size = (300, 300)


class MyApp(App):
    def build(self):
        self.title = "MyBusiness"
        return AuthLayout()


if __name__ == "__main__":
    MyApp().run()
