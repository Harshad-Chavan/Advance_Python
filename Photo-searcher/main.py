from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.lang import Builder
import wikipedia
import requests
import os

IMAGES_PATH = "files"
Builder.load_file("frontend.kv")

# class for screen manager
class RootWidget(ScreenManager):
    pass


# write multiple clasess if you need multiple screens
class FirstScreen(Screen):
    def search_image(self):
        # get user query from textbox
        query = self.manager.current_screen.ids.user_query.text

        #get wiki page and list of imageurl
        page = wikipedia.page(query)
        first_url = page.images[0]

        #download image
        file_path = os.path.join(IMAGES_PATH, query + ".jpg")
        with open(file_path, 'wb') as fd:
            response_content = requests.get(first_url).content
            fd.write(response_content)

        self.manager.current_screen.ids.img.source = file_path


class MainApp(App):
    def build(self):
        return RootWidget()


MainApp().run()
