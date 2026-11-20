import json

from kivy.factory import Factory
from kivy.uix.behaviors import ButtonBehavior
from kivymd.uix.boxlayout import MDBoxLayout


class PlayerButton(ButtonBehavior, MDBoxLayout):
    pass


Factory.register("PlayerButton", cls=PlayerButton)

class Matchs(MDBoxLayout):
    def __init__(self, joueur_1, joueur_2, pays_1, pays_2, nombre_de_sets, resultat):
        super().__init__()
        self.joueur_1 = joueur_1
        self.joueur_2 = joueur_2
        self.pays_1 = pays_1
        self.pays_2 = pays_2
        self.parier_joueur = {1: False, 2: False}
        self.fonction_parier = False
        self.nombre_de_sets = nombre_de_sets
        self.resultat = resultat
        self.pari_possible = True if self.resultat.get('etat') =='prevu' else False        
        self.charger_match()
        self.maj_bouton()


    def charger_match(self):
        self.ids.nom_joueur_1.text = self.joueur_1
        self.ids.nom_joueur_2.text = self.joueur_2
        self.ids.resultat_joueur_1.text = str(self.resultat[1])
        self.ids.resultat_joueur_2.text = str(self.resultat[2])
        self.ids.drapeau_joueur_1.source = self.charger_drapeau(self.pays_1)
        self.ids.drapeau_joueur_2.source = self.charger_drapeau(self.pays_2)
        self.ids.photo_joueur_1.source = self.charger_photo(self.joueur_1)
        self.ids.photo_joueur_2.source = self.charger_photo(self.joueur_2)
        self.ids.etat.text = self.resultat.get('etat')


    def maj_bouton(self):
        if self.pari_possible:
            score_joueur_1 = int(self.score(1))
            score_joueur_2 = int(self.score(2))
            self.ids.moins_joueur_1.disabled = score_joueur_1 <= 0
            self.ids.plus_joueur_1.disabled = score_joueur_1 >= self.nombre_de_sets
            self.ids.moins_joueur_2.disabled = score_joueur_2 <= 0
            self.ids.plus_joueur_2.disabled = score_joueur_2 >= self.nombre_de_sets

        else:
            self.ids.moins_joueur_1.disabled = True
            self.ids.plus_joueur_1.disabled = True
            self.ids.moins_joueur_2.disabled = True
            self.ids.plus_joueur_1.disabled = True


    def modifier_score_pari(self, joueur, operation):
        if not self.pari_possible: return
        match joueur:
            case 1:
                score = int(self.ids.score_joueur_1.text)
            case 2:
                score = int(self.ids.score_joueur_2.text)
            case _:
                return

        match operation:
            case '+':
                score += 1
                if score == self.nombre_de_sets: self.parier(joueur)
            case '-':
                if self.parier_joueur[joueur] and not self.fonction_parier:
                    self.parier_joueur[joueur] = False
                    match joueur:
                        case 1:
                            self.ids.joueur_1.md_bg_color = (0, 0, 0, 0)
                        case 2:
                            self.ids.joueur_2.md_bg_color = (0, 0, 0, 0)
                        case _: return
                score -= 1

        self.ids.score_joueur_1.text = str(score) if joueur == 1 else self.ids.score_joueur_1.text
        self.ids.score_joueur_2.text = str(score) if joueur == 2 else self.ids.score_joueur_2.text

        self.maj_bouton()


    def parier(self, joueur):
        if not self.pari_possible: return
        self.fonction_parier = True
        match joueur:
            case 1:
                if self.parier_joueur[1]:
                    self.ids.joueur_1.md_bg_color = (0, 0, 0, 0)
                    self.modifier_score_pari(1, '-')
                else:
                    self.ids.joueur_1.md_bg_color = (0, 1, 0, 1)  # Vert pour le joueur 1
                    self.ids.score_joueur_1.text = str(self.nombre_de_sets)
                    if self.parier_joueur[2]: self.parier(2)
                self.maj_bouton()
                self.parier_joueur[1] = not self.parier_joueur[1]
            case 2:
                if self.parier_joueur[2]:
                    self.ids.joueur_2.md_bg_color = (0, 0, 0, 0)
                    self.modifier_score_pari(2, '-')
                else:
                    self.ids.joueur_2.md_bg_color = (0, 1, 0, 1)  # Vert pour le joueur 2
                    self.ids.score_joueur_2.text = str(self.nombre_de_sets)
                    if self.parier_joueur[1]: self.parier(1)

                self.maj_bouton()
                self.parier_joueur[2] = not self.parier_joueur[2]
            case _:
                print('Joueur inconnu')
        self.fonction_parier = False


    def charger_drapeau(self, pays='inconnu'):
        try:
            with open(f'images/drapeaux.json', 'r') as f:
                dico_drapeaux = json.load(f)
            return f'images/drapeaux/{dico_drapeaux[pays]}'
        except:
            return 'images/drapeaux/inconu.jpg'


    def charger_photo(self, joueur='inconnu'):
        try:
            with open(f'images/joueurs.json', 'r') as f:
                dico_joueurs = json.load(f)
            return f'images/joueurs/{dico_joueurs[joueur]}'
        except:
            return 'images/joueurs/inconnu.jpg'


    def score(self, joueur):
        match joueur:
            case 1:
                return self.ids.score_joueur_1.text
            case 2:
                return self.ids.score_joueur_2.text
            case _:
                return 'erreur'
