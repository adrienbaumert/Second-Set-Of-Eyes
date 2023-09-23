from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.lang import Builder
from kivy.clock import Clock

class AppBoxLayout(BoxLayout):
    # Need dt because Clock.schedule_one() automatically passed dt
    # argument
    def on_button_hold(self, dt=None):
        print("Held")

    def on_button_press(self):
        self.hold_event = Clock.schedule_once(self.on_button_hold, 2)

    def on_button_release(self):
        self.hold_event.cancel()

class Application(App):
    def build(self):
        Builder.load_file("visionimpared.kv")
        return AppBoxLayout()

