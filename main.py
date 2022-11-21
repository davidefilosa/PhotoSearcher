from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.lang import Builder
import wikipedia
import requests

Builder.load_file('frontend.kv')


class FirstScreen(Screen):
    def get_image_link(self):
        search = self.manager.current_screen.ids.user_query.text
        page = wikipedia.page(search)
        link = page.images[0]
        return link, search

    def get_image(self):
        link, search = self.get_image_link()
        headers = {'User-Agent': 'copied user agent that came out when I googled it'}
        image = requests.get(link, headers=headers)
        path = f'files/{search}.jpg'
        return image, path

    def save_image(self):
        image, path = self.get_image()
        with open (path, 'wb') as img:
            img.write(image.content)
        self.manager.current_screen.ids.img.source = path


class RootWidget(ScreenManager):
    pass


class MainApp(App):
    def build(self):
        return RootWidget()


MainApp().run()
