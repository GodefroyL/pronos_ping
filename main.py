from kivymd.app import MDApp
from kivymd.uix.label import MDLabel
from kivy.lang import Builder
from kivymd.uix.screen import MDScreen
from kivy.core.window import Window
from kivymd.uix.button import MDIconButton
from kivy.clock import Clock
from kivymd.icon_definitions import md_icons


DONNEES = {
    'Champions de Montpellier': {
        'Quart de finale': {
            'f': {1: ('Wang Manyu','Hina Hayata'), 2: ('Wang Yidi', 'Chen Xingtong'), 3: ('Miwa Harimoto', 'Chen Yi'), 4: ('Mima Ito','Sun Yingsha')},
            'h': {1: ('Sora Matsushima','Lin Yun-Ju'), 2: ('Tomokazu Harimoto', 'Jang Woojin'), 3: ('Hugo Calderano', 'Alexis Lebrun'), 4: ('Felix Lebrun','Truls Möregårdh')}
        }
    }
}

class App(MDApp):
    def build(self):
        self.titre = "Pronos Ping"
        self.historique = []

        Builder.load_file("kv/accueil.kv")
        Builder.load_file("kv/parametres.kv")
        Builder.load_file("kv/regles.kv")
        Builder.load_file("kv/connexion.kv")
        Builder.load_file("kv/inscription.kv")
        Builder.load_file("kv/classements.kv")
        Builder.load_file("kv/ligues.kv")

        return Builder.load_file("kv/interface.kv")

    def aller(self, page: str, direction: str = "left"):
        if self.root:
            self.root.transition.direction = direction
            self.root.current = page
            self.historique.append(self.root.current)
            self.root.current = page

    def retour(self):
        if self.root and self.historique:
            self.root.current = self.historique.pop()
    
    def test(self, par):
        print(par)


class Accueil(MDScreen):
    def on_enter(self):
        Clock.schedule_once(self.maj_donnee,0.1)

    def maj_donnee(self,dt=0):
        championnat = self.ids.championnat.text
        tour = self.ids.tour.text
        sexe = self.ids.sexe.text
        self.ids.matchs.clear_widgets()
        if sexe == 'tous':
            matchs = DONNEES[championnat][tour]['f']
            for i in range(len(matchs)):
                self.ids.matchs.add_widget(MDLabel(text=f'{matchs[i+1][0]} VS {matchs[i+1][1]}',text_color=(1,1,1,1)))
            matchs = DONNEES[championnat][tour]['h']
            for i in range(len(matchs)):
                self.ids.matchs.add_widget(MDLabel(text=f'{matchs[i+1][0]} VS {matchs[i+1][1]}',text_color=(1,1,1,1)))
        else:
            matchs = DONNEES[championnat][tour][sexe]
            for i in range(len(matchs)):
                self.ids.matchs.add_widget(MDLabel(text=f'{matchs[i+1][0]} VS {matchs[i+1][1]}',text_color=(1,1,1,1)))


    print("Accueil")

class Parametres(MDScreen):
    pass

class Regles(MDScreen):
    pass

class Connexion(MDScreen):
    pass

class Inscription(MDScreen):
    pass

class Classements(MDScreen):
    pass

class Ligues(MDScreen):
    pass

if __name__ == "__main__":
    from kivy.utils import platform
    if platform not in ("android", "ios"):
        Window.size = (360, 640)  # simule un téléphone quand on teste sur ordinateur
    App().run()
