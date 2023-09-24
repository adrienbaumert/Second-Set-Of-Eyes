from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.lang import Builder
from kivy.clock import Clock
import threading
from time import time
import pygame.mixer

from BackendController import Controller
controller = Controller()

class AppBoxLayout(BoxLayout):
    # Making a flag for the tutorial being skipped
    welcome_playing = False

    # Defining a variable for the last time the main button was pressed
    last_tap_time = 0

    # Defining variable that keeps track of if the program is processing
    is_processing = False

    # Defining variable that keeps track of if tutorial is playing
    is_tutorial_playing = False

    # Making a flag for the tutorial being skipped
    tutorial_skipped = False

    # Setting the pygame mixer module
    pygame.mixer.init()

    # Need dt because Clock.schedule_one() automatically passed dt
    # argument
    def on_button_hold(self, dt=None):
        if self.is_tutorial_playing:
            pygame.mixer.stop()
            self.tutorial_skipped = True

        else:
            threading.Thread(target=self.playingTutorial).start()

    def playingTutorial(self):
        self.is_tutorial_playing = True

        tutorial_1 = pygame.mixer.Sound("Assets/Sounds/tutorial_1.mp4")
        tutorial_1.play()

        # Loop of nothing while text finishes playing
        while pygame.mixer.get_busy():
            pass

        if self.tutorial_skipped == False:
            tutorial_2 = pygame.mixer.Sound("Assets/Sounds/tutorial_2.mp4")
            tutorial_2.play()

            # Loop of nothing while text finishes playing
            while pygame.mixer.get_busy():
                pass

        self.is_tutorial_playing = False
        self.tutorial_skipped = False

    def on_button_press(self):
        if self.is_processing:
            return

        else:
            # Schedule an event for button being held
            self.hold_event = Clock.schedule_once(self.on_button_hold, 1.5)

            # Checking if the last time the main button was pressed was less than .5 seconds
            # ago
            current_time = time()
            if current_time - self.last_tap_time < .5 and self.last_tap_time != 0:
                self.hold_event.cancel()

                # Starting the BackendController in a different thread
                threading.Thread(target=controller.takingPictureToSpeech).start()

                # Setting the processing flag
                self.is_processing = True

                # Scheduling the audible processing message
                self.event = Clock.schedule_interval(self.processing, 1)

                self.last_tap_time = current_time

            else:
                self.last_tap_time = current_time

# Canceling the event scheduled to happen on button hold
    def on_button_release(self):
        self.hold_event.cancel()

    # Plays processing on a different thread than the image captioning api
    # so that a loading noise can be played
    # Need dt because Clock.schedule_one() automatically passed dt
    # argument
    def processing(self, dt=None):
        if controller.checkFinished() == False:
            processingSound = pygame.mixer.Sound("Assets/Sounds/processing.mp4")
            processingSound.play()

        else:
            self.event.cancel()
            controller.setFinishedFalse()

            # Setting the processing flag
            self.is_processing = False

class Application(App):
    def build(self):
        Builder.load_file("visionimpared.kv")
        return AppBoxLayout()

    def on_start(self):
        threading.Thread(target=self.welcomeMessage).start()

    # Need dt because Clock.schedule_one() automatically passed dt
    # argument
    def welcomeMessage(self, dt=None):
        # Playing welcome message on app boot
        welcomeSound = pygame.mixer.Sound("Assets/Sounds/welcome.mp4")
        welcomeSound.play()