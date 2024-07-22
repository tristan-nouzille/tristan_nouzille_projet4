import json
from datetime import datetime
import random

class Joueur:
    def __init__(self, nom, prenom, date_naissance, matricule, score=0):
        self.nom = nom
        self.prenom = prenom
        self.date_naissance = date_naissance
        self.matricule = matricule
        self.score = score  # Ajout du score

    def to_dict(self):
        return {
            'nom': self.nom,
            'prenom': self.prenom,
            'date_naissance': self.date_naissance.strftime('%d/%m/%Y'),
            'matricule': self.matricule,
            'score': self.score  # Ajout du score à la sérialisation
        }

    @classmethod
    def from_dict(cls, data):
        return cls(
            data['nom'],
            data['prenom'],
            datetime.strptime(data['date_naissance'], '%d/%m/%Y'),
            data['matricule'],
            data.get('score', 0)  # Ajout du score lors de la désérialisation
        )


class Tournoi:
    def __init__(self, nom, lieu, date_debut, date_fin, nombre_tours, description, joueurs_inscrits, tours=[]):
        self.nom = nom
        self.lieu = lieu
        self.date_debut = date_debut
        self.date_fin = date_fin
        self.nombre_tours = nombre_tours
        self.description = description
        self.joueurs_inscrits = joueurs_inscrits
        self.tours = tours
        self.joueurs_melanges = False  # Ajoutez cet attribut

    def melanger_joueurs(self):
        if not self.joueurs_melanges:
            random.shuffle(self.joueurs_inscrits)
            self.joueurs_melanges = True

    def generer_paires(self):
        joueurs_avec_score = sorted(self.joueurs_inscrits, key=lambda x: x.score, reverse=True)
        paires = []
        joueurs_utilises = set()
        for i in range(0, len(joueurs_avec_score) - 1, 2):
            joueur1 = joueurs_avec_score[i]
            joueur2 = joueurs_avec_score[i + 1]
            if (joueur1, joueur2) not in joueurs_utilises and (joueur2, joueur1) not in joueurs_utilises:
                paires.append((joueur1, joueur2))
                joueurs_utilises.add((joueur1, joueur2))
        return paires

    def ajouter_tour(self, tour):
        self.tours.append(tour)

    def to_dict(self):
        return {
            'nom': self.nom,
            'lieu': self.lieu,
            'date_debut': self.date_debut.strftime('%d/%m/%Y'),
            'date_fin': self.date_fin.strftime('%d/%m/%Y'),
            'description': self.description,
            'joueurs_inscrits': [joueur.to_dict() for joueur in self.joueurs_inscrits],
            'tours': [tour.to_dict() for tour in self.tours]
        }

    @classmethod
    def from_dict(cls, data):
        date_debut = datetime.strptime(data['date_debut'], '%d/%m/%Y')
        date_fin = datetime.strptime(data['date_fin'], '%d/%m/%Y')
        joueurs_inscrits = [Joueur.from_dict(j) for j in data['joueurs_inscrits']]
        tours = [Tour.from_dict(t) for t in data['tours']]
        nombre_tours = int(data['nombre_tours'])  # Convertir en entier
        return cls(data['nom'], data['lieu'], date_debut, date_fin, nombre_tours, data['description'], joueurs_inscrits, tours)

    
class Tour:
    def __init__(self, nom, joueurs):
        self.nom = nom
        self.joueurs = joueurs
        self.matchs = []
        self.date_debut = datetime.now()
        self.date_fin = None

    def commencer(self):
        random.shuffle(self.joueurs)
        self.matchs = [(self.joueurs[i], self.joueurs[i + 1]) for i in range(0, len(self.joueurs) - 1, 2)]

    def ajouter_match(self, match):
        match_id = len(self.matchs) + 1
        match.id = match_id
        self.matchs.append(match)

    def terminer(self):
        self.date_fin = datetime.now()

    def to_dict(self):
        return {
            'nom': self.nom,
            'date_debut': self.date_debut.strftime('%d/%m/%Y %H:%M:%S'),
            'date_fin': self.date_fin.strftime('%d/%m/%Y %H:%M:%S') if self.date_fin else None,
            'matchs': [match.to_dict() for match in self.matchs]
        }


class Match:
    def __init__(self, joueur1, joueur2, match_id=None):
        self.joueur1 = joueur1
        self.joueur2 = joueur2
        self.resultat = None
        self.id = match_id  # Ajout de l'identifiant du match

    def definir_resultat(self, resultat):
        self.resultat = resultat

    def to_dict(self):
        return {
            'joueur1': self.joueur1.to_dict(),
            'joueur2': self.joueur2.to_dict(),
            'resultat': self.resultat,
            'id': self.id  # Ajout de l'identifiant lors de la sérialisation
        }






       
















       































































































































































       
















       















       
















       














       
















       































































































































































       
















       















       
















       










