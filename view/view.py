# views/view.py

class View:
    @staticmethod
    def afficher_menu_principal():
        print("Bienvenue dans l'application de gestion des tournois d'échecs !")
        print("1. Créer un nouveau tournoi")
        print("2. Ajouter un joueur")
        print("3. Afficher tous les joueurs")
        print("4. Afficher tous les tournois")
        print("5. Quitter")
        print()

    @staticmethod
    def afficher_message(message):
        print(message)

    @staticmethod
    def afficher_erreur(message):
        print(f"Erreur: {message}")













