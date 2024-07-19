from datetime import datetime
import json
from models.models import Joueur
from view.view import View

class Controller:
    def __init__(self, model, view):
        self.model = model
        self.view = view

    def run(self):
        self.view.afficher_menu_principal()
        while True:
            choix = input("Entrez le numéro de votre choix : ")

            if choix == "1":
                self.creer_tournoi()
            elif choix == "2":
                self.ajouter_joueur()
            elif choix == "3":
                self.afficher_tous_les_joueurs()
            elif choix == "4":
                self.afficher_tous_les_tournois()
            elif choix == "5":
                self.view.afficher_message("Merci d'avoir utilisé l'application de gestion des tournois d'échecs ! Au revoir !")
                break
            else:
                self.view.afficher_erreur("Choix invalide. Veuillez entrer un numéro valide.")

    def ajouter_joueur(self):
        self.view.afficher_message("Ajout d'un joueur")
        while True:
            nom = input("Nom du joueur : ")
            prenom = input("Prénom du joueur : ")

            is_not_ok = True
            while is_not_ok:
                date_naissance_str = input("Date de naissance du joueur (format DD/MM/YYYY) : ")
                try:
                    date_naissance = datetime.strptime(date_naissance_str, '%d/%m/%Y')
                    is_not_ok = False
                except ValueError:
                    self.view.afficher_erreur("Format de date incorrect. Utilisez DD/MM/YYYY")
                    is_not_ok = True   

            faux_mat = True
            while faux_mat:
                matricule = input("Matricule du joueur (deux majuscules suivies de cinq chiffres) : ")
                if len(matricule) == 7 and matricule[:2].isalpha() and matricule[:2].isupper() and matricule[2:].isdigit():
                    if self.matricule_existe(matricule):
                        self.view.afficher_erreur("Le matricule existe déjà. Veuillez entrer un matricule unique.")
                    else:
                        faux_mat = False
                else:
                    self.view.afficher_erreur("Format du matricule incorrect. Utilisez deux majuscules suivies de cinq chiffres.")
                    
            joueur_ajoute = Joueur(nom, prenom, date_naissance, matricule)
            while True:
                choix = input("Voulez-vous confirmer l'inscription du joueur ? (oui/non) : ")
                if choix.lower() == "oui":
                    self.enregistrer_joueur(joueur_ajoute)
                    break
                elif choix.lower() == "non":
                    break
                else:
                    self.view.afficher_erreur("Choix invalide. Veuillez entrer 'oui' ou 'non'.")
            break
        
    def enregistrer_joueur(self, joueur):
        joueurs_inscrits = self.charger_joueurs_inscrits()
        joueurs_inscrits.append(joueur.to_dict())  # Convertir l'objet en dictionnaire

        with open('Données_des_Participants.json', 'w') as f:
            json.dump(joueurs_inscrits, f, indent=4)

        self.view.afficher_message(f"Le joueur {joueur.prenom} {joueur.nom} a été enregistré avec succès dans le fichier Données_des_Participants.json.")

    def charger_joueurs_inscrits(self):
        try:
            with open('Données_des_Participants.json', 'r') as f:
                joueurs_data = json.load(f)
                return joueurs_data
        except (FileNotFoundError, json.JSONDecodeError):
            return []

    def matricule_existe(self, matricule):
        joueurs_inscrits = self.charger_joueurs_inscrits()
        for joueur in joueurs_inscrits:
            if joueur['matricule'] == matricule:
                return True
        return False

    def afficher_tous_les_joueurs(self):
        joueurs = self.charger_joueurs_inscrits()
        self.view.afficher_message("Liste de tous les joueurs :")
        for joueur in joueurs:
            self.view.afficher_message(f"{joueur['prenom']} {joueur['nom']} - Date de naissance : {joueur['date_naissance']}")

    def afficher_tous_les_tournois(self):
        tournois = self.model.afficher_tous_les_tournois()
        self.view.afficher_message("Liste de tous les tournois :")
        for tournoi in tournois:
            self.view.afficher_message(f"{tournoi.nom} - Lieu : {tournoi.lieu} - Du {tournoi.date_debut.strftime('%d/%m/%Y %H:%M')} au {tournoi.date_fin.strftime('%d/%m/%Y %H:%M')}")

    def sauvegarder_tout(self):
        self.model.sauvegarder_tournois()

    def charger_tout(self):
        self.model.charger_tournois()














