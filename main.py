from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.uix.screenmanager import Screen

class App(MDApp):
    def build(self):
        self.titre = "Mon App"
        return Builder.load_file("kv/accueil.kv")

    def aller(self, screen_name: str, direction: str = "left"):
        self.root.transition.direction = direction
        self.root.current = screen_name
    
    def test(self, par):
        print(par)


class Accueil(Screen):
    print("Accueil")

class Parametres(Screen):
    pass

class Regles(Screen):
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
