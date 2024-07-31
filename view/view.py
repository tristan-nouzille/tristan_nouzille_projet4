# views/view.py
from datetime import datetime
class View:
    def afficher_menu_principal(self):
        print("=== Menu Principal ===")
        print("1. Créer un tournoi")
        print("2. Ajouter un joueur")
        print("3. Afficher tous les joueurs")
        print("4. Afficher tous les tournois")
        print("5. Lancer un tournoi")
        print("6. Quitter")

    def afficher_message(self, message):
        print(message)

    def afficher_erreur(self, message):
        print(f"Erreur: {message}")

    def afficher_tous_les_joueurs(self, joueurs):
        print("=== Liste des joueurs inscrits ===")
        for joueur in joueurs:
            print(f"{joueur['prenom']} {joueur['nom']} (Matricule: {joueur['matricule']})")

    def afficher_tous_les_tournois(self, tournois):
        print("=== Liste des tournois ===")
        for tournoi in tournois:
            print(f"{tournoi['nom']} à {tournoi['lieu']} (Début: {tournoi['date_debut']}, Fin: {tournoi['date_fin']})")

    def afficher_joueur_disponible(self, joueur):
        print(f"{joueur['prenom']} {joueur['nom']} (Matricule: {joueur['matricule']})")

    def afficher_match(self, tour_nom, joueur1, joueur2):
     if joueur2:
        print(f"{tour_nom} - Match: {joueur1.prenom} {joueur1.nom} vs {joueur2.prenom} {joueur2.nom}")
     else:
        print(f"{tour_nom} - Match: {joueur1.prenom} {joueur1.nom} a un bye (aucun adversaire)")



    def saisir_date(self, label):
        while True:
            try:
                date_str = input(f"{label} (format JJ/MM/AAAA) : ")
                date_obj = datetime.strptime(date_str, '%d/%m/%Y')
                return date_obj
            except ValueError:
                self.afficher_erreur("Date invalide. Veuillez entrer une date au format JJ/MM/AAAA.")

    def saisir_joueur(self):
        nom = input("Nom du joueur : ")
        prenom = input("Prénom du joueur : ")
        date_naissance = self.saisir_date("Date de naissance")
        matricule = input("Matricule du joueur : ").upper()
        return nom, prenom, date_naissance, matricule

    def saisir_tournoi(self):
        nom = input("Nom du tournoi : ")
        lieu = input("Lieu du tournoi : ")
        date_debut = self.saisir_date("Date de début")
        date_fin = self.saisir_date("Date de fin")
        description = input("Description du tournoi : ")
        return nom, lieu, date_debut, date_fin, description

    def afficher_match(self, tour_nom, match, lancer=False):
        if lancer:
            print(f"Lancement du match {match.numero} du {tour_nom} : {match.joueur1.prenom} {match.joueur1.nom} vs {match.joueur2.prenom} {match.joueur2.nom}")
        elif match.resultat is not None:
            gagnant = match.joueur1 if match.resultat == '1' else match.joueur2 if match.resultat == '2' else None
            resultat = f"Résultat : {gagnant.prenom} {gagnant.nom}" if gagnant else "Résultat : Match nul"
            print(f"{match.joueur1.prenom} {match.joueur1.nom} vs {match.joueur2.prenom} {match.joueur2.nom}. {resultat}")
        else:
            print(f"{match.joueur1.prenom} {match.joueur1.nom} vs {match.joueur2.prenom} {match.joueur2.nom}. Résultat : Non joué")










































































































































































































































































