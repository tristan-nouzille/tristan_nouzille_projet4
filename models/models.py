
from datetime import datetime


class Joueur:
    def __init__(self, nom, prenom, date_naissance, matricule, points=0):
        self.nom = nom
        self.prenom = prenom
        self.date_naissance = date_naissance
        self.matricule = matricule
        self.points = points
        
    def ajouter_points(self, points):
        self.points += points  # Ajoute des points au total

    def __str__(self):
        return f"{self.prenom} {self.nom} - Points: {self.points}"
    
    @classmethod
    def from_dict(cls, data):
        return cls(
            nom=data['nom'],
            prenom=data['prenom'],
            date_naissance=datetime.strptime(data['date_naissance'], '%d/%m/%Y'),
            matricule=data['matricule'],
            points=data.get('points', 0)
        )

    def to_dict(self):
        return {
            'nom': self.nom,
            'prenom': self.prenom,
            'date_naissance': self.date_naissance.strftime('%d/%m/%Y'),
            'matricule': self.matricule,
            'points': self.points
        }

    @staticmethod
    def validate_matricule(matricule):
        return len(matricule) == 7 and matricule[:2].isalpha() and matricule[2:].isdigit()



class Match:
    def __init__(self, joueur1, joueur2):
        self.joueur1 = joueur1
        self.joueur2 = joueur2
        self.resultat = None
        self.blanc = None
        self.noir = None

    def lancer(self):
        pass  # Logique de lancement du match à ajouter

    @classmethod
    def from_dict(cls, data):
        match = cls(
            joueur1=Joueur.from_dict(data['joueur1']),
            joueur2=Joueur.from_dict(data['joueur2']) if data['joueur2'] else None
        )
        match.resultat = data.get('resultat')
        match.blanc = Joueur.from_dict(data['blanc']) if data.get('blanc') else None
        match.noir = Joueur.from_dict(data['noir']) if data.get('noir') else None
        return match

    def to_dict(self):
        return {
            'joueur1': self.joueur1.to_dict(),
            'joueur2': self.joueur2.to_dict() if self.joueur2 else None,
            'resultat': self.resultat,
            'blanc': self.blanc.to_dict() if self.blanc else None,
            'noir': self.noir.to_dict() if self.noir else None
        }





class Tour:
    def __init__(self, nom, joueurs):
        self.nom = nom
        self.joueurs = joueurs
        self.matchs = []

    @classmethod
    def from_dict(cls, data):
        tour = cls(
            nom=data['nom'],
            joueurs=[Joueur.from_dict(j) for j in data['joueurs']]
        )
        tour.matchs = [Match.from_dict(m) for m in data['matchs']]
        return tour

    def to_dict(self):
        return {
            'nom': self.nom,
            'joueurs': [joueur.to_dict() for joueur in self.joueurs],
            'matchs': [match.to_dict() for match in self.matchs]
        }



class Tournoi:
    def __init__(self, nom, lieu, date_debut, date_fin, rounds, description):
        self.nom = nom
        self.lieu = lieu
        self.date_debut = date_debut
        self.date_fin = date_fin
        self.rounds = rounds
        self.description = description
        self.joueurs = []
        self.tours = []
        self.matchs = []  # Initialisation de l'attribut matchs
        self.rencontres = set()
        
    def ajouter_joueur(self, joueur):
        self.joueurs.append(joueur)  
         
    def a_deja_joue(self, joueur1, joueur2):
        return (joueur1.matricule, joueur2.matricule) in self.rencontres or (joueur2.matricule, joueur1.matricule) in self.rencontres

    def ajouter_match(self, match):
        self.matchs.append(match)  # Utilisation de l'attribut matchs
        # Ajout de la rencontre à l'ensemble
        self.rencontres.add((match.joueur1.matricule, match.joueur2.matricule))
  
    @classmethod
    def from_dict(cls, data):
        tournoi = cls(
            nom=data['nom'],
            lieu=data['lieu'],
            date_debut=datetime.strptime(data['date_debut'], '%d/%m/%Y'),
            date_fin=datetime.strptime(data['date_fin'], '%d/%m/%Y'),
            rounds=data['rounds'],
            description=data['description']
        )
        tournoi.joueurs = [Joueur.from_dict(j) for j in data['joueurs']]
        tournoi.tours = [Tour.from_dict(t) for t in data['tours']]
        tournoi.matchs = [Match.from_dict(m) for m in data['matchs']]  # Ajouter les matchs à partir des données
        return tournoi

    def to_dict(self):
        return {
            'nom': self.nom,
            'lieu': self.lieu,
            'date_debut': self.date_debut.strftime('%d/%m/%Y'),
            'date_fin': self.date_fin.strftime('%d/%m/%Y'),
            'rounds': self.rounds,
            'description': self.description,
            'joueurs': [joueur.to_dict() for joueur in self.joueurs],
            'tours': [tour.to_dict() for tour in self.tours],
            'matchs': [match.to_dict() for match in self.matchs]  # Ajouter les matchs à la conversion
        }

    def ajouter_tour(self, tour):
        self.tours.append(tour)












       
















       































































































































































       
















       















       
















       














       
















       































































































































































       
















       















       
















       


















       
















       































































































































































       
















       















       
















       














       
















       































































































































































       
















       















       
















       



















       
















       































































































































































       
















       















       
















       














       
















       































































































































































       
















       















       
















       
























       
















       































































































































































       
















       















       
















       














       
















       































































































































































       
















       















       
















       


















       
















       































































































































































       
















       















       
















       














       
















       































































































































































       
















       















       
















       



















       
















       































































































































































       
















       















       
















       














       
















       































































































































































       
















       















       
















       





















       
















       































































































































































       
















       















       
















       














       
















       































































































































































       
















       















       
















       


















       
















       































































































































































       
















       















       
















       














       
















       































































































































































       
















       















       
















       



















       
















       































































































































































       
















       















       
















       














       
















       































































































































































       
















       















       
















       
























       
















       































































































































































       
















       















       
















       














       
















       































































































































































       
















       















       
















       


















       
















       































































































































































       
















       















       
















       














       
















       































































































































































       
















       















       
















       



















       
















       































































































































































       
















       















       
















       














       
















       































































































































































       
















       















       
















       




















       
















       































































































































































       
















       















       
















       














       
















       































































































































































       
















       















       
















       


















       
















       































































































































































       
















       















       
















       














       
















       































































































































































       
















       















       
















       



















       
















       































































































































































       
















       















       
















       














       
















       































































































































































       
















       















       
















       
























       
















       































































































































































       
















       















       
















       














       
















       































































































































































       
















       















       
















       


















       
















       































































































































































       
















       















       
















       














       
















       































































































































































       
















       















       
















       



















       
















       































































































































































       
















       















       
















       














       
















       































































































































































       
















       















       
















       





















       
















       































































































































































       
















       















       
















       














       
















       































































































































































       
















       















       
















       


















       
















       































































































































































       
















       















       
















       














       
















       































































































































































       
















       















       
















       



















       
















       































































































































































       
















       















       
















       














       
















       































































































































































       
















       















       
















       
























       
















       































































































































































       
















       















       
















       














       
















       































































































































































       
















       















       
















       


















       
















       































































































































































       
















       















       
















       














       
















       































































































































































       
















       















       
















       



















       
















       































































































































































       
















       















       
















       














       
















       































































































































































       
















       















       
















       










