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
            'date_naissance': self.date_naissance.strftime('%d/%m/%Y'),
            'matricule': self.matricule
        }

    @classmethod
    def from_dict(cls, data):
        return cls(
            data['nom'],
            data['prenom'],
            datetime.strptime(data['date_naissance'], '%d/%m/%Y'),
            data['matricule']
        )


class Tournoi:
    def __init__(self, nom, lieu, date_debut, date_fin, nombre_tours, description):
        self.nom = nom
        self.lieu = lieu
        self.date_debut = datetime.strptime(date_debut, '%d/%m/%Y') if isinstance(date_debut, str) else date_debut
        self.date_fin = datetime.strptime(date_fin, '%d/%m/%Y') if isinstance(date_fin, str) else date_fin
        self.nombre_tours = nombre_tours
        self.description = description
        self.joueurs_inscrits = []
        self.tours = []

    def to_dict(self):
        return {
            'nom': self.nom,
            'lieu': self.lieu,
            'date_debut': self.date_debut.strftime('%d/%m/%Y'),
            'date_fin': self.date_fin.strftime('%d/%m/%Y'),
            'nombre_tours': self.nombre_tours,
            'description': self.description,
            'joueurs_inscrits': [joueur.to_dict() for joueur in self.joueurs_inscrits],
            'tours': [tour.to_dict() for tour in self.tours]
        }

    @classmethod
    def from_dict(cls, data):
        tournoi = cls(
            data['nom'],
            data['lieu'],
            data['date_debut'],
            data['date_fin'],
            data['nombre_tours'],
            data['description']
        )
        tournoi.joueurs_inscrits = [Joueur.from_dict(j) for j in data['joueurs_inscrits']]
        tournoi.tours = [Tour.from_dict(t) for t in data['tours']]
        return tournoi


class Tour:
    def __init__(self, nom, date_debut=None, date_fin=None):
        self.nom = nom
        self.date_debut = date_debut
        self.date_fin = date_fin
        self.matchs = []

    def ajouter_match(self, match):
        self.matchs.append(match)

    def to_dict(self):
        return {
            "nom": self.nom,
            "date_debut": self.date_debut.isoformat() if self.date_debut else None,
            "date_fin": self.date_fin.isoformat() if self.date_fin else None,
            "matchs": [match.to_dict() for match in self.matchs]
        }

    @staticmethod
    def from_dict(data):
        tour = Tour(
            nom=data["nom"],
            date_debut=datetime.fromisoformat(data["date_debut"]) if data["date_debut"] else None,
            date_fin=datetime.fromisoformat(data["date_fin"]) if data["date_fin"] else None
        )
        # Ajouter les matchs à partir des données
        for match_data in data.get("matchs", []):
            tour.ajouter_match(Match.from_dict(match_data))
        return tour

class Match:
    def __init__(self, joueur1, score1, joueur2, score2):
        self.joueur1 = joueur1
        self.score1 = score1
        self.joueur2 = joueur2
        self.score2 = score2

    def to_dict(self):
        return {
            "joueur1": self.joueur1,
            "score1": self.score1,
            "joueur2": self.joueur2,
            "score2": self.score2
        }

    @staticmethod
    def from_dict(data):
        return Match(
            joueur1=data["joueur1"],
            score1=data["score1"],
            joueur2=data["joueur2"],
            score2=data["score2"]
        )


class Match:
    def __init__(self, joueur1, joueur2):
        self.joueur1 = joueur1
        self.joueur2 = joueur2
        self.resultat = None

    def definir_resultat(self, resultat):
        if resultat in ['Joueur1', 'Joueur2', 'Egalité']:
            self.resultat = resultat
        else:
            raise ValueError("Résultat invalide. Utilisez 'Joueur1', 'Joueur2' ou 'Egalité'.")

    def to_dict(self):
        return {
            'joueur1': self.joueur1.to_dict(),
            'joueur2': self.joueur2.to_dict(),
            'resultat': self.resultat
        }





       
















       































































































































































       
















       















       
















       










