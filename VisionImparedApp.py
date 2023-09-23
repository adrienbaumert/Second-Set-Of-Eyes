from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.lang import Builder

class AppBoxLayout(BoxLayout):
    pass

class Application(App):
    def build(self):
        Builder.load_file("visionimpared.kv")
        return AppBoxLayout()