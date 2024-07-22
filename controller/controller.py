import json
import os
import random
from datetime import datetime
from models.models import Joueur, Tournoi, Tour, Match
from view.view import View

class Controller:
    def __init__(self, model, view):
        self.model = model
        self.view = view
        self.joueurs_path = os.path.join('data', 'Données_des_Participants.json')
        self.tournois_path = os.path.join('data', 'tournois.json')
        # Assurez-vous que les dossiers existent
        os.makedirs(os.path.dirname(self.joueurs_path), exist_ok=True)
        os.makedirs(os.path.dirname(self.tournois_path), exist_ok=True)

    def run(self):
        while True:
            self.view.afficher_menu_principal()
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
                self.lancer_tournoi()
            elif choix == "6":
                self.view.afficher_message("Merci d'avoir utilisé l'application de gestion des tournois d'échecs ! Au revoir !")
                break
            else:
                self.view.afficher_erreur("Choix invalide. Veuillez entrer un numéro valide.")
                
    def creer_tournoi(self):
        self.view.afficher_message("Création d'un nouveau tournoi")
        nom, lieu, date_debut, date_fin, description = self.view.saisir_tournoi()

        joueurs_inscrits = []
        joueurs_disponibles = self.charger_joueurs_inscrits()

        self.afficher_joueurs_disponibles()

        while True:
            matricule_joueur = input("Entrez le matricule du joueur à ajouter (ou '0' pour arrêter d'ajouter des joueurs) : ").upper()
            if matricule_joueur == "0":
                break
            else:
                joueur_selectionne = next((joueur for joueur in joueurs_disponibles if joueur['matricule'] == matricule_joueur), None)
                if joueur_selectionne:
                    joueur_obj = Joueur.from_dict(joueur_selectionne)
                    joueurs_inscrits.append(joueur_obj)
                    joueurs_disponibles.remove(joueur_selectionne)
                else:
                    self.view.afficher_erreur("Matricule de joueur invalide.")
                    ajouter_joueur = input("Voulez-vous ajouter un nouveau joueur ? (oui/non) : ")
                    if ajouter_joueur.lower() == "oui":
                        nom, prenom, date_naissance, matricule = self.view.saisir_joueur()
                        joueur_obj = Joueur(nom, prenom, date_naissance, matricule)
                        joueurs_inscrits.append(joueur_obj)
                        self.enregistrer_joueur(joueur_obj)
                    else:
                        self.view.afficher_erreur("Veuillez entrer un matricule valide.")

        if len(joueurs_inscrits) < 2:
            self.view.afficher_erreur("Le nombre de joueurs inscrits n'est pas suffisant pour un tournoi. Veuillez ajouter plus de joueurs.")
            return

        nombre_tours = self.calculer_nombre_tours(len(joueurs_inscrits))

        tournoi = Tournoi(nom, lieu, date_debut, date_fin, nombre_tours, description)
        tournoi.joueurs_inscrits = joueurs_inscrits

        self.enregistrer_tournoi(tournoi)
        self.view.afficher_message("Tournoi créé avec succès!")

    def ajouter_joueur(self):
        nom, prenom, date_naissance, matricule = self.view.saisir_joueur()
        joueur = Joueur(nom, prenom, date_naissance, matricule)
        self.enregistrer_joueur(joueur)
        self.view.afficher_message(f"Joueur {prenom} {nom} ajouté avec succès!")

    def afficher_tous_les_joueurs(self):
        joueurs = self.charger_joueurs_inscrits()
        self.view.afficher_tous_les_joueurs(joueurs)

    def afficher_tous_les_tournois(self):
        tournois = self.charger_tous_les_tournois()
        self.view.afficher_tous_les_tournois(tournois)

    def lancer_tournoi(self):
     tournois = self.charger_tous_les_tournois()
     self.view.afficher_tous_les_tournois(tournois)

     nom_tournoi = input("Entrez le nom du tournoi à lancer : ")
     tournoi_data = next((t for t in tournois if t['nom'] == nom_tournoi), None)

     if tournoi_data:
        tournoi_obj = Tournoi.from_dict(tournoi_data)
        self.view.afficher_message(f"Lancement du tournoi : {tournoi_obj.nom}")

        for i in range(len(tournoi_obj.tours), tournoi_obj.nombre_tours):
            tour = Tour(f"Tour {i+1}", tournoi_obj.joueurs_inscrits)
            tour.commencer()

            for match in tour.matchs:
                self.view.afficher_match(tour.nom, match.joueur1, match.joueur2)

                resultat = input("Entrez le résultat du match (Joueur1, Joueur2, Egalité) : ")
                match.definir_resultat(resultat)

            tour.terminer()
            tournoi_obj.ajouter_tour(tour)

            self.enregistrer_tournoi(tournoi_obj.to_dict())

        self.view.afficher_message(f"Tournoi {tournoi_obj.nom} terminé !")
     else:
        self.view.afficher_erreur("Tournoi non trouvé.")


    def enregistrer_joueur(self, joueur):
        joueur_data = joueur.to_dict()
        try:
            with open(self.joueurs_path, 'r') as f:
                joueurs = json.load(f)
        except FileNotFoundError:
            joueurs = []

        joueurs.append(joueur_data)
        
        with open(self.joueurs_path, 'w') as f:
            json.dump(joueurs, f, indent=4)

    def charger_joueurs_inscrits(self):
        try:
            with open(self.joueurs_path, 'r') as f:
                joueurs = json.load(f)
            return joueurs
        except FileNotFoundError:
            return []

    def enregistrer_tournoi(self, tournoi):
     tournoi_data = tournoi if isinstance(tournoi, dict) else tournoi.to_dict()
     try:
        with open(self.tournois_path, 'r') as f:
            if os.stat(self.tournois_path).st_size == 0:
                tournois = []
            else:
                tournois = json.load(f)
     except (FileNotFoundError, json.JSONDecodeError):
        tournois = []

    # Supprimer le tournoi existant avec le même nom
     tournois = [t for t in tournois if t['nom'] != tournoi_data['nom']]

     tournois.append(tournoi_data)

     with open(self.tournois_path, 'w') as f:
        json.dump(tournois, f, indent=4)



    def charger_tous_les_tournois(self):
        try:
            with open(self.tournois_path, 'r') as f:
                tournois = json.load(f)
            return tournois
        except FileNotFoundError:
            return []

    def calculer_nombre_tours(self, nombre_joueurs):
        if nombre_joueurs < 4:
            return 1
        elif nombre_joueurs <= 8:
            return 3
        else:
            return 4

    def afficher_joueurs_disponibles(self):
        joueurs_disponibles = self.charger_joueurs_inscrits()
        if joueurs_disponibles:
            self.view.afficher_message("Joueurs disponibles pour inscription :")
            for joueur in joueurs_disponibles:
                self.view.afficher_joueur_disponible(joueur)
        else:
            self.view.afficher_message("Aucun joueur disponible pour inscription.")




















































































































































































































































































































































































































































