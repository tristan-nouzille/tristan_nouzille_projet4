import json
from datetime import datetime
import random

class Joueur:
    def __init__(self, nom, prenom, date_naissance, matricule):
        self.nom = nom
        self.prenom = prenom
        self.date_naissance = date_naissance
        self.matricule = matricule

    def to_dict(self):
        return {
            'nom': self.nom,
            'prenom': self.prenom,
            'date_naissance': self.date_naissance,
            'matricule': self.matricule
        }

    @classmethod
    def from_dict(cls, data):
        return cls(
            data['nom'],
            data['prenom'],
            data['date_naissance'],
            data['matricule']
        )



class Tournoi:
    def __init__(self, nom, lieu, date_debut, date_fin, nombre_tours, description):
        self.nom = nom
        self.lieu = lieu
        self.date_debut = date_debut
        self.date_fin = date_fin
        self.nombre_tours = nombre_tours
        self.description = description
        self.joueurs_inscrits = []
        self.tours = []

    def ajouter_joueur(self, joueur):
        self.joueurs_inscrits.append(joueur)

    def ajouter_tour(self, tour):
        self.tours.append(tour)

    def to_dict(self):
        return {
            'nom': self.nom,
            'lieu': self.lieu,
            'date_debut': self.date_debut.strftime('%d/%m/%Y'),  # Convertir en chaîne de caractères
            'date_fin': self.date_fin.strftime('%d/%m/%Y'),      # Convertir en chaîne de caractères
            'nombre_tours': self.nombre_tours,
            'description': self.description,
            'joueurs': [joueur.to_dict() for joueur in self.joueurs_inscrits],
            'tours': [tour.to_dict() for tour in self.tours]
        }

    @classmethod
    def from_dict(cls, data):
        tournoi = cls(
            data['nom'],
            data['lieu'],
            datetime.strptime(data['date_debut'], '%d/%m/%Y'),  # Convertir en datetime
            datetime.strptime(data['date_fin'], '%d/%m/%Y'),    # Convertir en datetime
            data.get('nombre_tours', 1),  # Utiliser une valeur par défaut de 1 si 'nombre_tours' est manquant
            data['description']
        )
        tournoi.joueurs_inscrits = [Joueur.from_dict(j) for j in data.get('joueurs', [])]
        tournoi.tours = [Tour.from_dict(t) for t in data.get('tours', [])]
        return tournoi




    
class Tour:
    def __init__(self, nom, joueurs):
        self.nom = nom
        self.joueurs = joueurs
        self.matchs = []

    def commencer(self):
        random.shuffle(self.joueurs)  # Mélanger les joueurs avant de créer les matchs
        self.creer_matchs()

    def creer_matchs(self):
        for i in range(0, len(self.joueurs), 2):
            if i + 1 < len(self.joueurs):
                joueur1 = self.joueurs[i]
                joueur2 = self.joueurs[i + 1]
                match = Match(joueur1, joueur2)
                self.matchs.append(match)
            else:
                # Si nombre de joueurs est impair, le dernier joueur est laissé sans adversaire
                joueur1 = self.joueurs[i]
                match = Match(joueur1, None)
                self.matchs.append(match)

    def to_dict(self):
        return {
            'nom': self.nom,
            'matchs': [match.to_dict() for match in self.matchs]
        }

    @classmethod
    def from_dict(cls, data):
        tour = cls(data['nom'], [])
        tour.matchs = [Match.from_dict(m) for m in data.get('matchs', [])]
        return tour




class Match:
    def __init__(self, joueur1, joueur2):
        self.joueur1 = joueur1
        self.joueur2 = joueur2
        self.resultat = None

    def definir_resultat(self, resultat):
        self.resultat = resultat

    def to_dict(self):
        return {
            'joueur1': self.joueur1.to_dict(),
            'joueur2': self.joueur2.to_dict() if self.joueur2 else None,
            'resultat': self.resultat
        }

    @classmethod
    def from_dict(cls, data):
        joueur1 = Joueur.from_dict(data['joueur1'])
        joueur2 = Joueur.from_dict(data['joueur2']) if data['joueur2'] else None
        match = cls(joueur1, joueur2)
        match.resultat = data.get('resultat')
        return match










       
















       































































































































































       
















       















       
















       














       
















       































































































































































       
















       















       
















       


















       
















       































































































































































       
















       















       
















       














       
















       































































































































































       
















       















       
















       



















       
















       































































































































































       
















       















       
















       














       
















       































































































































































       
















       















       
















       










