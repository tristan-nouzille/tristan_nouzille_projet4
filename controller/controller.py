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

     date_debut = self.saisir_date("Date de début")
     date_fin = self.saisir_date("Date de fin")
 
     description = input("Description du tournoi : ")

     joueurs_inscrits = []
     joueurs_disponibles = self.charger_joueurs_inscrits()

     while True:
        self.view.afficher_message("Joueurs disponibles :")
        for joueur in joueurs_disponibles:
            self.view.afficher_message(f"{joueur['prenom']} {joueur['nom']} - Date de naissance : {joueur['date_naissance']} - Matricule : {joueur['matricule']}")

        matricule_joueur = input("Entrez le matricule du joueur à ajouter (ou '0' pour arrêter d'ajouter des joueurs) : ").upper()
        if matricule_joueur == "0":
            break
        else:
            joueur_selectionne = next((joueur for joueur in joueurs_disponibles if joueur['matricule'] == matricule_joueur), None)
            if joueur_selectionne:
                joueur_obj = Joueur(
                    joueur_selectionne['nom'],
                    joueur_selectionne['prenom'],
                    datetime.strptime(joueur_selectionne['date_naissance'], '%d/%m/%Y'),
                    joueur_selectionne['matricule']
                )
                joueurs_inscrits.append(joueur_obj)
                joueurs_disponibles.remove(joueur_selectionne)
            else:
                self.view.afficher_erreur("Matricule de joueur invalide.")
                ajouter_joueur = input("Voulez-vous ajouter un nouveau joueur ? (oui/non) : ")
                if ajouter_joueur.lower() == "oui":
                    joueur_obj = self.ajouter_joueur_dans_tournoi()
                    if joueur_obj:
                        joueurs_inscrits.append(joueur_obj)
                        self.enregistrer_joueur(joueur_obj)
                else:
                    self.view.afficher_erreur("Veuillez entrer un matricule valide.")

     if len(joueurs_inscrits) < 2:
        self.view.afficher_erreur("Le nombre de joueurs inscrits n'est pas suffisant pour un tournoi. Veuillez ajouter plus de joueurs.")
        return

    # Calculer le nombre de tours requis sans arrondi
     nombre_joueurs = len(joueurs_inscrits)
     nombre_tours = int(math.log2(nombre_joueurs))
     if 2 ** nombre_tours < nombre_joueurs:
        nombre_tours += 1  # Assurer que le nombre de tours est suffisant pour tous les joueurs

    # Assurez-vous que le nombre de tours est au moins 4
     nombre_tours = max(nombre_tours, 4)

     tournoi = Tournoi(nom, lieu, date_debut, date_fin, nombre_tours, description)
     tournoi.joueurs_inscrits = joueurs_inscrits
     self.enregistrer_tournoi(tournoi)
     self.view.afficher_message(f"Le tournoi {tournoi.nom} a été créé avec succès avec {nombre_tours} tours !")

    def saisir_date(self, type_date):
        is_not_ok = True
        while is_not_ok:
            date_str = input(f"{type_date} (format DD/MM/YYYY) : ")
            try:
                date = datetime.strptime(date_str, '%d/%m/%Y')
                is_not_ok = False
            except ValueError:
                self.view.afficher_erreur("Format de date incorrect. Utilisez DD/MM/YYYY")
                is_not_ok = True
        return date

    def ajouter_joueur_dans_tournoi(self):
        self.view.afficher_message("Ajout d'un joueur au tournoi")
        nom = input("Nom du joueur : ")
        prenom = input("Prénom du joueur : ")
        date_naissance = self.saisir_date("Date de naissance du joueur")

        matricule = self.saisir_matricule()

        joueur_ajoute = Joueur(nom, prenom, date_naissance, matricule)
        self.view.afficher_message(f"Le joueur {joueur_ajoute.prenom} {joueur_ajoute.nom} a été ajouté avec succès au tournoi !")
        return joueur_ajoute

    def saisir_matricule(self):
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
        return matricule

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
        joueur_ajoute = self.ajouter_joueur_dans_tournoi()
        while True:
            choix = input("Voulez-vous confirmer l'inscription du joueur ? (oui/non) : ")
            if choix.lower() == "oui":
                self.enregistrer_joueur(joueur_ajoute)
                break
            elif choix.lower() == "non":
                break
            else:
                self.view.afficher_erreur("Choix invalide. Veuillez entrer 'oui' ou 'non'.")

    def enregistrer_joueur(self, joueur):
        joueurs_inscrits = self.charger_joueurs_inscrits()
        joueurs_inscrits.append(joueur.to_dict())
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
        return any(joueur['matricule'] == matricule for joueur in joueurs_inscrits)

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
















