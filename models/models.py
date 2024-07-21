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
    def __init__(self, nom, lieu, date_debut, date_fin, nombre_tours=4, description=""):
        self.nom = nom
        self.lieu = lieu
        self.date_debut = date_debut
        self.date_fin = date_fin
        self.nombre_tours = nombre_tours
        self.tours = []
        self.joueurs_inscrits = []
        self.description = description
        
    def ajouter_tour(self, tour):
        self.tours.append(tour)
        
    def generer_paires(self):
        joueurs = sorted(self.joueurs_inscrits, key=lambda j: j.score, reverse=True)
        paires = []
        while len(joueurs) > 1:
            joueur1 = joueurs.pop(0)
            joueur2 = joueurs.pop(0)
            paires.append((joueur1, joueur2))
        return paires 
      
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

    def commencer(self):
        self.date_debut = datetime.now()

    def terminer(self):
        self.date_fin = datetime.now()

    def ajouter_match(self, match):
        self.matchs.append(match)

    def to_dict(self):
        return {
            'nom': self.nom,
            'date_debut': self.date_debut.isoformat() if self.date_debut else None,
            'date_fin': self.date_fin.isoformat() if self.date_fin else None,
            'matchs': [match.to_dict() for match in self.matchs]
        }


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





       
















       










