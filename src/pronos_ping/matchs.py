from kivy.uix.actionbar import BoxLayout
from kivymd.uix.label import MDLabel

KV = """
<Matchs>:
    md_bg_color: [0, 0, 0, 0]
    BoxLayout:
        orientation: 'horizontal'
        MDButton:
            id: joueur1
            BoxLayout:
                orientation: 'horizontal'
                MDLabel:
                    text: ''
                MDLabel:
                    text: '')
            text: ''
            on_release: app.test('Joueur 1')
        MDLabel:
            text: 'VS'
            halign: 'center'
        MDButton:
            id: joueur2

"""

class Matchs():
    def _init_(self, conteneur, joueur1, joueur2, nombre_de_sets):
        conteneur.add_widget(MDLabel(text=f'{joueur1} VS {joueur2}',text_color=(1,1,1,1)))


    def charger_drapeau(self, code):
        pass
        # Mise à jour dynamique de l'URL
        # self.image_drapeau.source = f'https://flagcdn.com{code}.png'
        # self.info_label.text = f'Drapeau actuel : {code.upper()}'
