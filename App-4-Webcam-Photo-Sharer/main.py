from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.lang import Builder
from datetime import datetime as dt
from kivy.core.clipboard import Clipboard
import webbrowser

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
        self.ids.camera.texture = None

    def capture(self):
        self.file_name = dt.now().strftime("%d%m%H%M%Y") + ".png"
        self.ids.camera.export_to_png(self.file_name)
        # changes to the next screen
        self.manager.current = "image_screen"
        # at this point current screen is images creen
        self.manager.current_screen.ids.img.source = self.file_name


class ImageScreen(Screen):
    link_message = " create a link first"

    def create_link(self):
        file_path = App.get_running_app().root.ids.camera_screen.file_name
        self.dummy_link = "http://" + file_path
        self.ids.link_lable.text = self.dummy_link

    def copy_link(self):
        try:
            Clipboard.copy(self.dummy_link)
        except:
            self.ids.link_lable.text = self.link_message

    def open_link(self):
        try:
            webbrowser.open(self.dummy_link)
        except:
            self.ids.link_lable.text = self.link_message


class MainApp(App):
    def build(self):
        return RootWidget()


MainApp().run()
