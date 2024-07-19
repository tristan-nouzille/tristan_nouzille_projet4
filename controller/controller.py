from datetime import datetime
import json
from models.models import Joueur, Tournoi
from view.view import View
import math
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
                
    def creer_tournoi(self):
        self.view.afficher_message("Création d'un nouveau tournoi")
        nom = input("Nom du tournoi : ")
        lieu = input("Lieu du tournoi : ")

        is_not_ok = True
        while is_not_ok:
            date_debut_str = input("Date de début (format DD/MM/YYYY) : ")
            try:
                date_debut = datetime.strptime(date_debut_str, '%d/%m/%Y')
                is_not_ok = False
            except ValueError:
                self.view.afficher_erreur("Format de date incorrect. Utilisez DD/MM/YYYY")
                is_not_ok = True

        is_not_ok = True
        while is_not_ok:
            date_fin_str = input("Date de fin (format DD/MM/YYYY) : ")
            try:
                date_fin = datetime.strptime(date_fin_str, '%d/%m/%Y')
                is_not_ok = False
            except ValueError:
                self.view.afficher_erreur("Format de date incorrect. Utilisez DD/MM/YYYY")
                is_not_ok = True

        description = input("Description du tournoi : ")

        joueurs_inscrits = []
        while True:
            ajouter_joueur = input("Voulez-vous ajouter un joueur ? (oui/non) : ")
            if ajouter_joueur.lower() == "oui":
                joueur = self.ajouter_joueur_dans_tournoi()
                if joueur:
                    joueurs_inscrits.append(joueur)
            elif ajouter_joueur.lower() == "non":
                break
            else:
                self.view.afficher_erreur("Choix invalide. Veuillez entrer 'oui' ou 'non'.")

        nombre_tours = max(math.ceil(math.log2(len(joueurs_inscrits))), 4)

        if nombre_tours < 4:
            self.view.afficher_erreur("Le nombre de joueurs inscrits n'est pas suffisant pour un tournoi avec au moins 4 tours. Veuillez ajouter plus de joueurs.")
            return

        tournoi = Tournoi(nom, lieu, date_debut, date_fin, nombre_tours, description)
        tournoi.joueurs_inscrits = joueurs_inscrits
        self.enregistrer_tournoi(tournoi)
        self.view.afficher_message(f"Le tournoi {tournoi.nom} a été créé avec succès avec {nombre_tours} tours!")

    def ajouter_joueur_dans_tournoi(self):
        self.view.afficher_message("Ajout d'un joueur au tournoi")
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
        self.view.afficher_message(f"Le joueur {joueur_ajoute.prenom} {joueur_ajoute.nom} a été ajouté avec succès au tournoi !")
        return joueur_ajoute

    def enregistrer_tournoi(self, tournoi):
        tournois_inscrits = self.charger_tournois_inscrits()
        tournois_inscrits.append(tournoi.to_dict())

        with open('data/tournaments/tournois.json', 'w') as f:
            json.dump(tournois_inscrits, f, indent=4)

    def charger_tournois_inscrits(self):
        try:
            with open('data/tournaments/tournois.json', 'r') as f:
                tournois_data = json.load(f)
                return tournois_data
        except (FileNotFoundError, json.JSONDecodeError):
            return []
        
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














