from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.lang import Builder

IMAGES_PATH = "files"
Builder.load_file("frontend.kv")


# class for screen manager
class RootWidget(ScreenManager):
    pass


# write multiple classes if you need multiple screens
class CameraScreen(Screen):
    def start(self):
        self.ids.camera.play = True
        self.ids.start_stop.text = "Stop camera"

    def stop(self):
        self.ids.camera.play = False
        self.ids.start_stop.text = "Start camera"

    def capture(self):
        pass


class ImageScreen(Screen):
    pass


class MainApp(App):
    def build(self):
        return RootWidget()


MainApp().run()
