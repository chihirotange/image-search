from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.lang import Builder
from wikipedia import wikipedia as wp
import requests

Builder.load_file("frontend.kv")

class FirstScreen(Screen):
    def search_image(self):
        user_query = self.manager.current_screen.ids.user_query.text
        user_img = wp.page(user_query).images[0]
        user_img_byte = requests.get(user_img).content

        img_filepath = "file/img.png"
        with open(img_filepath, "wb") as f:
            f.write(user_img_byte)

        self.manager.current_screen.ids.img.source = img_filepath
                
class RootWidget(ScreenManager):
    pass


class MainApp(App):
    def build(self):
        return RootWidget()


MainApp().run()