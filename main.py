from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.lang import Builder
import wikipedia
import requests
import shutil

Builder.load_file('frontend.kv')


class FirstScreen(Screen):
    def search_image(self):
        search = self.manager.current_screen.ids.user_query.text
        page = wikipedia.page(search)
        link = page.images[0]
        headers = {'User-Agent': 'copied user agent that came out when I googled it'}
        image = requests.get(link, headers=headers)
        path = f'files/{search}.jpg'
        with open (path, 'wb') as img:
            img.write(image.content)
        self.manager.current_screen.ids.img.source = path



class RootWidget(ScreenManager):
    pass


class MainApp(App):
    def build(self):
        return RootWidget()


MainApp().run()
