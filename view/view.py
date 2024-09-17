class View:
    
    @staticmethod
    def afficher_menu_principal():
        print('')
        print("=== Gestion des Tournois d'Échecs ===")
        print("1. Créer un nouveau tournoi")
        print("2. Ajouter un joueur")
        print("3. Afficher tous les joueurs")
        print("4. Afficher tous les tournois")
        print("5. Lancer un tournoi")
        print("6. Générer un rapport des joueurs")
        print("7. Générer un rapport des tournois")
        print("8. Quitter")
        print('')

    @staticmethod
    def afficher_message(message):
        print('')
        print(message)
        
    @staticmethod
    def afficher_erreur(message):
        print(f"Erreur : {message}")

    @staticmethod
    def afficher_joueur_disponible(joueur):
        print(f" - Matricule: {joueur['matricule']} Nom: {joueur['prenom']} {joueur['nom']} "
              f"Date de naissance: {joueur['date_naissance']}")

    @staticmethod
    def afficher_tous_les_joueurs(joueurs):
        if not joueurs:
            print("Aucun joueur trouvé.")
            return
        
        print("Liste de tous les joueurs :")
        for joueur in joueurs:
            print(f" - {joueur['matricule']} - {joueur['prenom']} {joueur['nom']} - "
                  f"{joueur['date_naissance']}")
        print('')

    @staticmethod
    def afficher_tous_les_tournois(tournois):
        if not tournois:
            print("Aucun tournoi trouvé.")
            return
        
        print("Liste de tous les tournois :")
        print('')
        for tournoi in tournois:
            print(f"{tournoi['nom']} - {tournoi['lieu']} - Du {tournoi['date_debut']} "
                  f"au {tournoi['date_fin']}")

    def afficher_tous_les_rounds(self, tournoi):
        if not tournoi.rounds_list:
            print("Aucun round disponible pour ce tournoi.")
            return
        
        for round in tournoi.rounds_list:
            print(f"=== {round.nom} ===")
            for match in round.matchs:
                print(f"Match: {match.blanc.nom} VS {match.noir.nom}. Résultat : {match.resultat or 'Non joué'}")
            print('')  # Ligne vide pour séparer les rounds

    @staticmethod
    def afficher_match(tour_nom, match, lancer=False):
        if lancer:
            print('')
            print('================================================================================================')
            print('')
        
            joueur1_nom = f"{match.joueur1.prenom} {match.joueur1.nom}"
            joueur2_nom = f"{match.joueur2.prenom} {match.joueur2.nom}" if match.joueur2 else 'Bye'
        
            couleur_joueur1 = "Blanc" if match.blanc == match.joueur1 else "Noir"
            couleur_joueur2 = "Blanc" if match.blanc == match.joueur2 else "Noir"

            print(f"Match en cours dans le '{tour_nom}': {joueur1_nom} ({couleur_joueur1}) " 
                  f"vs {joueur2_nom} ({couleur_joueur2})")
            print('')
            print('================================================================================================')
            print('')
            
        else:
            # Affichage des détails du match et du résultat
            joueur1_nom = f"{match.joueur1.prenom} {match.joueur1.nom}"
            joueur2_nom = f"{match.joueur2.prenom} {match.joueur2.nom}" if match.joueur2 else 'Bye'
        
            gagnant = 'Non joué'
            if match.resultat == '1':
                gagnant = joueur1_nom
            elif match.resultat == '2':
                gagnant = joueur2_nom
            elif match.resultat == 'N':
                gagnant = 'Nul'
        
            print("================================================================================================")
            print(f"Match: {joueur1_nom} ({'Blanc' if match.blanc == match.joueur1 else 'Noir'}) vs "
                  f"{joueur2_nom} ({'Blanc' if match.blanc == match.joueur2 else 'Noir'}), Gagnant: {gagnant}")
            print("================================================================================================")

    def afficher_rapport_joueurs(self, joueurs):
        print("Rapport des joueurs :")
        for joueur in joueurs:
            print('')
            print(f"{joueur.nom} {joueur.prenom}, né le {joueur.date_naissance.strftime('%d/%m/%Y')}, "
                  f"Matricule : {joueur.matricule}")
            print('')

    def afficher_liste_tournois(self, tournois):
        """Affiche la liste des tournois disponibles et demande à l'utilisateur de choisir un tournoi."""
        if not tournois:
            self.afficher_message("Aucun tournoi disponible.")
            return None
        
        self.afficher_message("=== Liste des Tournois Disponibles ===")
        for index, tournoi in enumerate(tournois):
            self.afficher_message(f"{index + 1}. Nom: {tournoi['nom']}")
            print('')
        
        self.afficher_message("Veuillez entrer le numéro du tournoi pour générer le rapport:")
        print('')
        choix = input("Numéro du tournoi: ")

        try:
            choix_index = int(choix) - 1
            if 0 <= choix_index < len(tournois):
                return tournois[choix_index]
            else:
                self.afficher_message("Numéro de tournoi invalide.")
                return None
        except ValueError:
            self.afficher_message("Entrée invalide. Veuillez entrer un numéro.")
            return None

    def obtenir_contenu_rapport_tournois(self, tournois):
        """Retourne le rapport des tournois sous forme de chaîne de caractères."""
        rapport = []
        if not tournois:
            rapport.append("Aucun tournoi enregistré.")
            return "\n".join(rapport)
    
        rapport.append("=== Rapport du Tournois  ===")
        for tournoi in tournois:
            rapport.append(f"Nom: {tournoi['nom']}, Lieu: {tournoi['lieu']}, "
                           f"Date de début: {tournoi['date_debut']}, "
                           f"Date de fin: {tournoi['date_fin']}, "
                           f"Description: {tournoi['description']}")
        
            rapport.append("Scores des joueurs :")
            scores = tournoi.get('scores', {})
            if isinstance(scores, dict):
                for matricule, score in scores.items():
                    joueur_info = self.get_joueur_info(tournoi, matricule)
                    nom_joueur = f"{joueur_info['prenom']} {joueur_info['nom']}"
                    rapport.append(f"Joueur {nom_joueur}: {score} points")
            else:
                rapport.append("Aucun score disponible.")
        
            rapport.append("Détails des matchs :")
            rounds_list = tournoi.get('rounds_list', [])
            if isinstance(rounds_list, list):
                for round in rounds_list:
                    rapport.append(f"  --- {round['nom']} ---")
                    matchs = round.get('matchs', [])
                    if isinstance(matchs, list):
                        for match in matchs:
                            joueur1 = f"{match['joueur1']['nom']} {match['joueur1']['prenom']}"
                            joueur2 = (
                                f"{match['joueur2']['nom']} {match['joueur2']['prenom']}"
                                if match['joueur2'] 
                                else "Bye"
                            )
                            resultat = match.get('resultat', 'Non joué')
                            if resultat == '1':
                                gagnant = joueur1
                            elif resultat == 'N':
                                gagnant = "Nul"
                            elif resultat == '2':
                                gagnant = joueur2
                            else:
                                gagnant = "Non joué"
                            rapport.append(f"  Match: {joueur1} VS {joueur2}, Gagnant: {gagnant}")
                    else:
                        rapport.append("  Aucun match disponible.")
            else:
                rapport.append("Aucun round disponible.")
        
            rapport.append("Classement des joueurs :")
            if isinstance(scores, dict):
                classement = sorted(scores.items(), key=lambda item: item[1], reverse=True)
                for i, (matricule, score) in enumerate(classement, start=1):
                    joueur_info = self.get_joueur_info(tournoi, matricule)
                    nom_joueur = f"{joueur_info['prenom']} {joueur_info['nom']}"
                    rapport.append(f"{i}. Joueur {nom_joueur}: {score} points")
            else:
                rapport.append("  Aucun classement disponible.")
     
        rapport.append("=========================================================================")
    
        return "\n".join(rapport)
   
    def demander_confirmation(self, message):
        """Affiche un message et demande une confirmation à l'utilisateur (O/N)."""
        # Ou toute autre méthode pour obtenir une entrée de l'utilisateur
        choix = input(message + "(O/N) : ") 
        if choix.strip().lower() in ['o', 'n']:
            return choix.strip().lower()
        return None  # Retourner None si la réponse est invalide

    def get_joueur_info(self, tournoi, matricule):
        """Retourne les informations sur un joueur à partir du matricule dans le tournoi donné."""
        joueurs = tournoi.get('joueurs', [])
        for joueur in joueurs:
            if joueur['matricule'] == matricule:
                return {'prenom': joueur['prenom'], 'nom': joueur['nom']}
        
        return {'prenom': 'Nom inconnu', 'nom': 'Nom inconnu'}






















































































































































































































































































        












































































































































































































































































        























































































































































































































































































































































































































































































































































        












































































































































































































































































        































































































































































































































































































































































































































































































































































        












































































































































































































































































        























































































































































































































































































































































































































































































































































        












































































































































































































































































        









































































































































































































































































