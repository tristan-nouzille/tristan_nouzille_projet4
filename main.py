"""""""""""
Ceci est le code source pour le logiciel du tournoi d'Echecs local

"""""""""""
import random
import json
import os

class Joueurs:
    tous_les_joueurs = []

    def __init__(self, nom, prenom, date_naissance, matricule):
        self.nom = nom
        self.prenom = prenom
        self.date_naissance = date_naissance
        self.matricule = matricule

    @classmethod
    def inscrire(cls):
        nom = input("Entrez le nom : ")
        prenom = input("Entrez le prénom : ")
        date_naissance = input("Entrez la date de naissance : ")
        matricule = input("Entrez le matricule : ")
        joueur = cls(nom, prenom, date_naissance, matricule)
        if joueur not in cls.tous_les_joueurs:
            cls.tous_les_joueurs.append(joueur)
        else:
            print("Ce joueur existe déjà dans la liste.")

    @classmethod
    def afficher_joueurs(cls):
        print("Liste des joueurs inscrits :")
        for i, joueur in enumerate(cls.tous_les_joueurs, 1):
            print(f"{i}. {joueur.nom} {joueur.prenom}")

    @staticmethod
    def melanger_joueurs():
        random.shuffle(Joueurs.tous_les_joueurs)

class Tournoi:
    def __init__(self, nom):
        self.nom = nom
        self.matches = []

    def ajouter_match(self, tours, victoire, nul):
        match = {"tours": tours, "victoire": victoire, "nul": nul}
        self.matches.append(match)

    def afficher_matches(self):
        print(f"Matches du tournoi {self.nom}:")
        for idx, match in enumerate(self.matches, 1):
            print(f"Match {idx}: Tours - {match['tours']}, Victoire - {match['victoire']}, Nul - {match['nul']}")

# Créer une instance de la classe Tournoi
tournoi = Tournoi("Tournoi de football")

# Inscrire des joueurs
nombre_joueurs = int(input("Entrez le nombre de joueurs à inscrire : "))
for _ in range(nombre_joueurs):
    Joueurs.inscrire()

# Afficher les joueurs inscrits
Joueurs.afficher_joueurs()

# Mélanger les joueurs
Joueurs.melanger_joueurs()

# Afficher les joueurs après mélange
print("\nJoueurs après mélange :")
Joueurs.afficher_joueurs()
