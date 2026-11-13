from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.uix.screenmanager import Screen

class App(MDApp):
    def build(self):
        return Builder.load_file("interface.kv")

class Accueil(Screen):
    pass

class Parametres(Screen):
    pass

class Connexion(Screen):
    pass

class Inscription(Screen):
    pass

class Classements(Screen):
    pass

class Ligues(Screen):
    pass

if __name__ == "__main__":
    App().run()
