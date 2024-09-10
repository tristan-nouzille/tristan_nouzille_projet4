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
        print("8. Quitter")

    @staticmethod
    def afficher_message(message):
        print(message)

    @staticmethod
    def afficher_erreur(message):
        print(f"Erreur : {message}")

    @staticmethod
    def afficher_joueur_disponible(joueur):
        """Affiche un joueur disponible pour être ajouté au tournoi."""
        print(f" - Matricule: {joueur.matricule} Nom: {joueur.prenom} {joueur.nom} "
              f"Date de naissance: {joueur.date_naissance}")

    @staticmethod
    def afficher_tous_les_joueurs(joueurs):
        """Affiche tous les joueurs enregistrés."""
        if not joueurs:
            print("Aucun joueur trouvé.")
            return
        print("Liste de tous les joueurs :")
        for joueur in joueurs:
            print(f" - {joueur.matricule} - {joueur.prenom} {joueur.nom} - "
                  f"{joueur.date_naissance.strftime('%d/%m/%Y')}")
        print('')

    @staticmethod
    def afficher_tous_les_tournois(tournois):
        """Affiche tous les tournois enregistrés."""
        if not tournois:
            print("Aucun tournoi trouvé.")
            return
        print("Liste de tous les tournois :")
        for tournoi in tournois:
            print(f"{tournoi.nom} - {tournoi.lieu} - Du {tournoi.date_debut} "
                  f"au {tournoi.date_fin}")

    def afficher_rounds(self, round):
        """Affiche les matchs d'un round."""
        print(f"Round: {round.nom}")
        for match in round.match_list:
            print(f"  {match.joueur1.nom} vs {match.joueur2.nom}")

    @staticmethod
    def afficher_match(tour_nom, match, lancer=False):
        """Affiche les détails d'un match."""
        if lancer:
            print('')
            print('=================================================================================================')
            print('')
            print(f"Match en cours dans le tour '{tour_nom}': {match.joueur1.prenom} {match.joueur1.nom} vs "
                  f"{match.joueur2.prenom if match.joueur2 else 'Bye'}")
            print('')
            print('=================================================================================================')
            print('')
        else:
            print(f"======> Match terminé: {match.resultat}")

    def afficher_rapport_joueurs(self, joueurs):
        """Affiche un rapport détaillé des joueurs."""
        print("Rapport des joueurs :")
        for joueur in joueurs:
            print('')
            print(f"{joueur.nom} {joueur.prenom}, né le {joueur.date_naissance.strftime('%d/%m/%Y')}, "
                  f"Matricule : {joueur.matricule}")
            print('')

    def afficher_rapport_tournois(self, tournois):
        """Affiche le rapport des tournois avec les scores."""
        if not tournois:
            self.afficher_message("Aucun tournoi enregistré.")
            return

        self.afficher_message("=== Rapport des Tournois ===")
        for tournoi in tournois:
            self.afficher_message(f"Nom: {tournoi.nom}, Lieu: {tournoi.lieu}, "
                                  f"Date de début: {tournoi.date_debut}, "
                                  f"Date de fin: {tournoi.date_fin}, "
                                  f"Description: {tournoi.description}")
            self.afficher_message("Scores des joueurs :")

            if tournoi.scores:
                for matricule, score in tournoi.scores.items():
                    self.afficher_message(f"Joueur Matricule {matricule}: {score} points")
            else:
                self.afficher_message("Aucun score disponible.")

        self.afficher_message("===============================")

    def afficher_rapport_matchs(self, tournois):
        """Affiche un rapport détaillé des matchs des tournois."""
        self.afficher_message("=== Rapport des Matchs ===")
        for tournoi in tournois:
            self.afficher_message(f"Nom: {tournoi.nom}, Lieu: {tournoi.lieu}, "
                                  f"Date de début: {tournoi.date_debut}, "
                                  f"Date de fin: {tournoi.date_fin}, "
                                  f"Description: {tournoi.description}")

            if tournoi.rounds:
                for round in tournoi.rounds:
                    self.afficher_message(f"  --- {round.nom} ---")
                    for match in round.matchs:
                        joueur1 = f"{match.joueur1.nom} {match.joueur1.prenom}"
                        joueur2 = f"{match.joueur2.nom} {match.joueur2.prenom}" if match.joueur2 else "Bye"
                        resultat = match.resultat if match.resultat else 'Non joué'
                        self.afficher_message(f"  Match: {joueur1} VS {joueur2}, Résultat: {resultat}")
            else:
                self.afficher_message("  Aucun round disponible.")

    def afficher_classement(self, tournoi):
        """Affiche le classement des joueurs pour le tournoi donné."""
        print(f"Classement des joueurs pour le tournoi : {tournoi.nom}")

        # Récupérer les joueurs triés par points en ordre décroissant
        classement = sorted(tournoi.joueurs.values(), key=lambda j: j.points, reverse=True)

        # Afficher chaque joueur avec son rang
        for index, joueur in enumerate(classement, start=1):
            # Afficher le rang, le nom du joueur et les points
            print(f"{index} - {joueur.prenom} {joueur.nom} : {joueur.points:.1f} points")



        









































































































































































































































































