class View:
    @staticmethod
    def afficher_menu_principal():
        print("=== Gestion des Tournois d'Échecs ===")
        print("1. Créer un nouveau tournoi")
        print("2. Ajouter un joueur")
        print("3. Afficher tous les joueurs")
        print("4. Afficher tous les tournois")
        print("5. Lancer un tournoi")
        print("6. Générer un rapport des joueurs")
        print("7. Générer un rapport des tournois")
        print("8. Générer un rapport des matchs")
        print("9. Quitter")

    @staticmethod
    def afficher_message(message):
        print(message)

    @staticmethod
    def afficher_erreur(message):
        print(f"Erreur : {message}")

    @staticmethod
    def afficher_joueur_disponible(joueur):
        print(f"Matricule: {joueur['matricule']}, Nom: {joueur['prenom']} {joueur['nom']}, Date de naissance: {joueur['date_naissance']}")

    @staticmethod
    def afficher_tous_les_joueurs(joueurs):
        if not joueurs:
            print("Aucun joueur trouvé.")
            return
        print("Liste de tous les joueurs :")
        for joueur in joueurs:
            print(f"{joueur['matricule']} - {joueur['prenom']} {joueur['nom']} - {joueur['date_naissance']} - Points : {joueur['points']}")

    @staticmethod
    def afficher_tous_les_tournois(tournois):
        if not tournois:
            print("Aucun tournoi trouvé.")
            return
        print("Liste de tous les tournois :")
        for tournoi in tournois:
            print(f"{tournoi['nom']} - {tournoi['lieu']} - Du {tournoi['date_debut']} au {tournoi['date_fin']}")

    @staticmethod
    def afficher_match(tour_nom, match, lancer=False):
        if lancer:
            print(f"Match en cours dans le tour '{tour_nom}': {match.joueur1.prenom} {match.joueur1.nom} vs {match.joueur2.prenom if match.joueur2 else 'Bye'}")
        else:
            print(f"Match terminé: {match.resultat}")










































































































































































































































































