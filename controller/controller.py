from Models.models import Joueur
from view.view import JoueurView
import json


class JoueurController:
    def __init__(self, view, fichier):
        self.view = view
        self.fichier = fichier
        self.joueurs = self.charger_joueurs()
    def create_joueurs(self):
        while True:
            joueur_info = self.view.get_joueur_info()
            if joueur_info is None:
                print("Le nom est vide. Arrêt de la création des joueurs.")
                break
            nom, prenom, date_naissance, matricule = joueur_info
            if self.is_matricule_unique(matricule):
                joueur = Joueur(nom, prenom, date_naissance, matricule)
                self.joueurs.append(joueur)  # Ajouter le joueur à la liste
                self.enregistrer_joueurs()
                self.view.display_joueur(joueur)
            else:
                self.view.display_error("Le matricule est déjà utilisé. Veuillez en entrer un autre.")
     
    def is_matricule_unique(self, matricule):
        for joueur in self.joueurs:
            if joueur.matricule == matricule:
                return False
        return True

    def enregistrer_joueurs(self):
        joueurs_dict = [joueur.to_dict() for joueur in self.joueurs]
        with open(self.fichier, 'w') as f:
            json.dump(joueurs_dict, f, indent=4)

    def charger_joueurs(self):
        try:
            with open(self.fichier, 'r') as f:
                joueurs_dict = json.load(f)
                joueurs = [Joueur(joueur['nom'], joueur['prenom'], joueur['date_naissance'], joueur['matricule']) for joueur in joueurs_dict]
        except FileNotFoundError:
            joueurs = []
        return joueurs