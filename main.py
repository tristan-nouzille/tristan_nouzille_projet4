"""""""""""
Ceci est le code source pour le logiciel du tournoi d'Echecs local

"""""""""""
# main.py
# main.py
from view.view import JoueurView
from controller.controller import JoueurController

def main():
    fichier = 'joueurs.json'  # Nom du fichier JSON pour enregistrer les joueurs
    view = JoueurView()
    controller = JoueurController(view, fichier)
    controller.create_joueurs()

if __name__ == "__main__":
    main()


