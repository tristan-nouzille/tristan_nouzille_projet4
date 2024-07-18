import json
from datetime import datetime

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

    @staticmethod
    def from_dict(data):
        return Joueur(data['nom'], data['prenom'], datetime.strptime(data['date_naissance'], '%d/%m/%Y'), data['matricule'])

    @classmethod
    def creer_joueur(cls, nom, prenom, date_naissance, matricule):
        return cls(nom, prenom, date_naissance, matricule)

class Tournoi:
    def __init__(self, nom, lieu, date_debut, date_fin, nombre_tours=4, description=""):
        self.nom = nom
        self.lieu = lieu
        self.date_debut = date_debut
        self.date_fin = date_fin
        self.nombre_tours = nombre_tours
        self.tours = []
        self.joueurs_inscrits = []
        self.description = description

    def to_dict(self):
        return {
            'nom': self.nom,
            'lieu': self.lieu,
            'date_debut': self.date_debut.isoformat(),
            'date_fin': self.date_fin.isoformat(),
            'nombre_tours': self.nombre_tours,
            'tours': [tour.to_dict() for tour in self.tours],
            'joueurs_inscrits': [joueur.to_dict() for joueur in self.joueurs_inscrits],
            'description': self.description
        }

    @staticmethod
    def from_dict(data):
        tournoi = Tournoi(data['nom'], data['lieu'], datetime.fromisoformat(data['date_debut']), datetime.fromisoformat(data['date_fin']), data['nombre_tours'], data['description'])
        tournoi.tours = [Tour.from_dict(t) for t in data['tours']] if 'tours' in data else []
        tournoi.joueurs_inscrits = [Joueur.from_dict(j) for j in data['joueurs_inscrits']] if 'joueurs_inscrits' in data else []
        return tournoi


class Tour:
    def __init__(self, nom):
        self.nom = nom
        self.date_debut = None
        self.date_fin = None
        self.matchs = []

    def to_dict(self):
        return {
            'nom': self.nom,
            'date_debut': self.date_debut.isoformat() if self.date_debut else None,
            'date_fin': self.date_fin.isoformat() if self.date_fin else None,
            'matchs': [match.to_dict() for match in self.matchs]
        }

    @staticmethod
    def from_dict(data):
        tour = Tour(data['nom'])
        tour.date_debut = datetime.fromisoformat(data['date_debut']) if 'date_debut' in data and data['date_debut'] else None
        tour.date_fin = datetime.fromisoformat(data['date_fin']) if 'date_fin' in data and data['date_fin'] else None
        tour.matchs = [Match.from_dict(m) for m in data['matchs']] if 'matchs' in data else []
        return tour


class Match:
    def __init__(self, joueur1, joueur2, score1=None, score2=None):
        self.joueur1 = joueur1
        self.joueur2 = joueur2
        self.score1 = score1
        self.score2 = score2

    def to_dict(self):
        return {
            'joueur1': self.joueur1.to_dict(),
            'joueur2': self.joueur2.to_dict(),
            'score1': self.score1,
            'score2': self.score2
        }

    @staticmethod
    def from_dict(data):
        joueur1 = Joueur.from_dict(data['joueur1'])
        joueur2 = Joueur.from_dict(data['joueur2'])
        return Match(joueur1, joueur2, data.get('score1'), data.get('score2'))







       










